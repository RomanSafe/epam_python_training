import asyncio
import json
import os
import re
import sqlite3
import time
import urllib.parse
from collections.abc import AsyncGenerator, Iterable, Mapping
from itertools import chain, islice
from multiprocessing import Pool
from typing import Any, List, Tuple

import aiohttp
import aiosqlite
import requests
from bs4 import BeautifulSoup, SoupStrainer


async def fetch_markup(session: aiohttp.ClientSession, url: str, **kwargs) -> str:
    """Fetches html text from given url.

    Args:
        session: to use for request;
        url: address to fetch html from.

    Returns:
        text of response.

    """

    async with session.get(url, **kwargs) as response:
        return await response.text()


async def get_main_pages_html(
    session: aiohttp.ClientSession, url: str
) -> AsyncGenerator[asyncio.Future[str], None]:
    """Gets html from main pages.

    Args:
        session: to use for request;
        url: address to fetch html from.

    Returns:
        AsyncGenerator[asyncio.Future[str], None]

    """

    async def async_range(*args) -> AsyncGenerator[int, None]:
        # Asynchronous range iterator.
        for i in range(*args):
            yield i

    for html in asyncio.as_completed(
        [
            asyncio.create_task(fetch_markup(session, url.format(page_num)))
            async for page_num in async_range(1, 11)
        ]
    ):
        yield html


def get_companies_links(markup: str) -> List[str]:
    """Parse html and get urls of companies.

    Args:
        markup: of a page.

    Returns:
        list of companies' urls.

    """

    url = "https://markets.businessinsider.com"
    result = []
    page_links = SoupStrainer(href=re.compile("/stocks/"), class_=False)
    for reference in BeautifulSoup(markup, "html.parser", parse_only=page_links):
        company_url = urllib.parse.urljoin(url, reference["href"])
        result.append(company_url)
    return result


async def get_comp_pages_html(
    session: aiohttp.ClientSession, companies_links: Iterable[str]
) -> AsyncGenerator[asyncio.Future[str], None]:
    """Gets html from pages of companies.

    Args:
        session: to use for request;
        companies_links: to download html from.

    Returns:
        AsyncGenerator[str, None]

    """

    async def async_items(iterable):
        for i in iterable:
            yield i

    for html in asyncio.as_completed(
        [
            asyncio.create_task(fetch_markup(session, url))
            async for url in async_items(companies_links)
        ]
    ):
        yield html


def get_companies_info(markup: str) -> tuple:
    """Parses html and get info about companies.

    Args:
        markup: for parsing.

    Returns:
        company_code, name, price, p_e, potential_profit.

    """

    price_section = SoupStrainer("div", class_="price-section__row")
    soup = BeautifulSoup(markup, "html.parser", parse_only=price_section)
    name_tag = soup.find("span", class_="price-section__label")
    name = name_tag.string.strip()
    company_code = name_tag.next_sibling.next_sibling.span.string.strip(", ")
    price = float(
        name_tag.parent.next_sibling.next_sibling.span.string.replace(",", "")
    )

    snapshot_section = BeautifulSoup(
        markup, "html.parser", parse_only=SoupStrainer("div", class_="snapshot")
    )
    script_tag = snapshot_section.find("script")
    if script_tag:
        script_text = str(script_tag.string)
        high52weeks = float(
            re.search(r"high52weeks: (\d+[.]?\d*),", script_text)  # type: ignore
            .group(1)
            .replace(",", "")
        )
        low52weeks = float(
            re.search(r"low52weeks: (\d+[.]?\d*),", script_text)  # type: ignore
            .group(1)
            .replace(",", "")
        )
    potential_profit = round(((high52weeks - low52weeks) / low52weeks * 100), 2)
    p_e = snapshot_section.find("div", class_="snapshot__header", text="P/E Ratio")
    if p_e:
        p_e = float(p_e.parent.contents[0].strip().replace(",", ""))
    else:
        p_e = 0
    return company_code, name, price, p_e, potential_profit


def get_exchange_rate(currency_code: str = "R01235") -> float:
    """Gets the cost of given currency in Russian rubles for the last market day.

    Args:
        currency_code: [description]. Defaults to "R01235"(US dollar).

    Returns:
        price of given currency in Russian rubles.

    """

    xml = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text
    rubles_per_unit = BeautifulSoup(
        xml, "html.parser", parse_only=SoupStrainer("valute", id=currency_code)
    ).value.string
    return float(rubles_per_unit.string.replace(",", "."))


def collect_year_growth(markup) -> List[Tuple[float, str]]:
    """Collects year growth of shares from main page table.

    Args:
        markup: html of main page.

    Returns:
        List[Tuple[float, str]]

    """

    results = []
    rows = BeautifulSoup(
        markup,
        "html.parser",
        parse_only=SoupStrainer("table", class_="table table-small"),
    ).find_all("tr")[1:]
    for row in islice(rows, 1, None):
        columns = row.find_all("td")
        name = columns[0].text.strip()
        growth = float(columns[-2].find_all("span")[-1].string.replace("%", ""))
        results.append((growth, name))
    return results


async def add_info_to_db(
    method,
    sql_statement,
    *args,
    db_name=os.path.join(os.path.dirname(__file__), "s&p_500.sqlite"),
) -> None:
    """Adds collected info to database.

    Args:
        method: "executescript" or "executemany" or "execute";
        sql_statement: to execute;
        db_name: Defaults to os.path.join(os.path.dirname(__file__),
        "s&p_500.sqlite").

    """

    async with aiosqlite.connect(db_name) as db:
        if method == "executescript":
            await db.executescript(sql_statement)
        elif method == "executemany":
            await db.executemany(sql_statement, *args)
        elif method == "execute":
            await db.execute(sql_statement, *args)
        await db.commit()


async def create_report(report_name: str, main_property: str, statement: str) -> None:
    """Creates a report in json format, based on information received from database after
        execution of a statement.

    Args:
        connection: to the database;
        report_name: descriptive name of report;
        main_property: of report;
        statement: SELECT SQL statement to execute.

    """

    async def get_query_results(
        statement, db_name=os.path.join(os.path.dirname(__file__), "s&p_500.sqlite")
    ) -> AsyncGenerator[sqlite3.Row, None]:
        """Gets query results from database.

        Args:
            statement: sqlite syntax;
            db_name: Defaults to os.path.join(os.path.dirname(__file__),
            "s&p_500.sqlite").

        Yields:
            request of database.

        """

        async with aiosqlite.connect(db_name) as db:
            async with db.execute(statement) as cursor:
                async for row in cursor:
                    yield row

    report_base = [
        {key: value for key, value in zip(("code", "name", main_property), row)}
        async for row in get_query_results(statement)
    ]
    with Pool(processes=1) as pool:
        pool.apply_async(write_json, report_name, report_base)  # type: ignore


def write_json(report_name: str, report_base: List[Mapping[str, Any]]) -> None:
    """Converts report_base to json and writes to a file.

    Args:
        report_name: name of report;
        report_base: name of report_base.

    """

    with open(
        os.path.join(os.path.dirname(__file__), f"{report_name}.json"),
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(report_base, file, indent=4)


async def main() -> None:
    """Runs main programmes' logic."""

    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        print("collect html form main pages, start")
        url = "https://markets.businessinsider.com/index/components/s&p_500?p={}"
        main_pages_html = [
            await html async for html in get_main_pages_html(session, url)
        ]
        p2 = time.time()
        print(f"collection of main_pages_html lasted: {p2 - start_time}")
        with Pool() as pool:
            companies_links = set(
                chain(*pool.map_async(get_companies_links, main_pages_html).get())
            )
        p3 = time.time()
        print(f"collection of companies_links lasted: {p3 - p2}")
        comp_pages_html = [
            await html async for html in get_comp_pages_html(session, companies_links)
        ]
        p4 = time.time()
        print(f"collection of comp_pages_html lasted: {p4 - p3}")
        with Pool() as pool:
            companies_info = pool.map_async(get_companies_info, comp_pages_html).get()
            exchange_rate = (pool.apply_async(get_exchange_rate).get(),)
            year_growth = chain(
                *pool.map_async(collect_year_growth, main_pages_html).get()
            )
        p5 = time.time()
        print("parsing of comp_pages_html,")
        print("receiving of usd price,")
        print(f"collecting_year_growth lasted: {p5 - p4}")
        await asyncio.create_task(
            add_info_to_db(
                "executescript",
                """DROP TABLE IF EXISTS s_and_p_500;
                CREATE TABLE s_and_p_500 (company_code text, name text UNIQUE,
                price real, p_e real, potential_profit real, year_growth real);
                """,
            )
        )
        await asyncio.create_task(
            add_info_to_db(
                "executemany",
                """INSERT INTO s_and_p_500 (company_code, name, price, p_e,
                potential_profit)
                VALUES (?, ?, ?, ?, ?);
                """,
                companies_info,
            )
        )
        await asyncio.create_task(
            add_info_to_db(
                "executemany",
                """UPDATE s_and_p_500
                SET year_growth = ?
                WHERE name LIKE (?||'%');
                """,
                year_growth,
            )
        )
        await asyncio.create_task(
            add_info_to_db(
                "execute",
                """UPDATE s_and_p_500
                SET price = round(price * ?, 2);
                """,
                exchange_rate,
            )
        )
        p6 = time.time()
        print(f"save information to db lasted: {p6 - p5}")

        tasks = [
            create_report(
                report_name="most_expensive_shares_top_10",
                main_property="price",
                statement="""SELECT company_code, name, price
                    FROM s_and_p_500
                    ORDER BY price DESC
                    LIMIT 10;""",
            ),
            create_report(
                report_name="lowest_p_e_top_10",
                main_property="P/E",
                statement="""SELECT company_code, name, p_e
                    FROM s_and_p_500
                    WHERE p_e > 0
                    ORDER BY p_e ASC NULLS LAST
                    LIMIT 10;""",
            ),
            create_report(
                report_name="strongest_growth_top_10",
                main_property="growth",
                statement="""SELECT company_code, name, year_growth
                    FROM s_and_p_500
                    ORDER BY year_growth DESC
                    LIMIT 10;""",
            ),
            create_report(
                report_name="biggest_potential_profit_top_10",
                main_property="potential profit",
                statement="""SELECT company_code, name, potential_profit
                    FROM s_and_p_500
                    ORDER BY potential_profit DESC
                    LIMIT 10;""",
            ),
        ]
        await asyncio.gather(*tasks)
        p7 = time.time()
        print(f"generate json lasted: {p7 - p6}")
        print(f"total {p7 - start_time}")


asyncio.run(main())
