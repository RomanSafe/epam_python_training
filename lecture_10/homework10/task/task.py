import asyncio
import datetime
import json
import os
import re
import sqlite3
import urllib.parse
from string import punctuation

import aiohttp
from bs4 import BeautifulSoup
from tqdm.asyncio import trange


async def get_connection_and_create_table(
    db_name: str, script: str
) -> sqlite3.Connection:
    """Creates Connection object and new database table.

    Args:
        db_name: name of database to connect;
        script: script of SQL statements.

    Returns:
        Connection object for futher work with database.

    """

    connection = sqlite3.connect(db_name)
    with connection:
        connection.executescript(script)
    return connection


async def fetch_markup(session: aiohttp.ClientSession, url: str, **kwargs) -> str:
    """Fetches html text from given url.

    Args:
        session: to use for request;
        url: address to fetch html text from.

    Returns:
        html text of response.

    """

    async with session.get(url, **kwargs) as response:
        return await response.text()


async def get_exchange_rate(
    session: aiohttp.ClientSession,
    date: datetime.date = datetime.date.today(),
    currency_code: str = "R01235",
) -> float:
    """Gets the cost of given currency in Russian rubles for the last market day.

    Args:
        session: to use for request;
        date: for getting of exchange rate. Defaults to datetime.date.today().
        currency_code: [description]. Defaults to "R01235"(US dollar).

    Returns:
        price of given currency in Russian rubles.

    """

    rubles_per_usd = None
    one_day = datetime.timedelta(days=1)
    while rubles_per_usd is None:
        date_text = date.strftime("%d/%m/%Y")
        markup = await fetch_markup(
            session,
            "http://www.cbr.ru/scripts/XML_dynamic.asp",
            params={
                "date_req1": date_text,
                "date_req2": date_text,
                "VAL_NM_RQ": currency_code,
            },
        )
        soup = BeautifulSoup(markup, "html.parser")
        rubles_per_usd = soup.find("value")
        if rubles_per_usd:
            return float(rubles_per_usd.string.replace(",", "."))
        date = date - one_day


async def collect_year_growth(
    connection: sqlite3.Connection, soup: BeautifulSoup
) -> None:
    """Collects year growth from main page table and save it to the database.

    Args:
        connection: database connection to use;
        soup: BeautifulSoup object to parse.

    """

    #  I looked through img tag because target span tag don't have unique attributes.
    for tag in soup.find_all("img", alt=True):
        short_name = tag["alt"].strip()
        tags_parent = tag.parent.previous_sibling.previous_sibling
        growth = float(
            tags_parent.find("span", text=re.compile("%")).string.replace("%", "")
        )
        try:
            with connection:
                connection.execute(
                    "INSERT INTO s_and_p_500(short_name, year_growth) VALUES (?, ?);",
                    (short_name, growth),
                )
        except sqlite3.IntegrityError:
            pass


async def collect_info_from_companies_pages(
    connection: sqlite3.Connection,
    session: aiohttp.ClientSession,
    soup: BeautifulSoup,
    url: str,
    rubles_per_usd: float,
) -> None:
    """Collects information from pages of companies and save them to the database.

    Args:
        connection: to the database;
        session: to use for request;
        soup: BeautifulSoup object to parse;
        url: of the site;
        rubles_per_usd: price of one US dollar in Russian rubles.

    """

    for reference in soup.find_all(href=re.compile("/stocks/"), class_=False):
        company_url = urllib.parse.urljoin(url, reference["href"])
        short_name = reference.string.strip()
        company_page = await fetch_markup(session, company_url)
        soup = BeautifulSoup(company_page, "html.parser").body

        stock_tag = soup.find("span", class_="price-section__category")
        company_code = stock_tag.span.string.strip(punctuation)

        name = str(soup.find("span", class_="price-section__label").string.strip())

        price = float(
            soup.find("span", class_="price-section__current-value").string.replace(
                ",", ""
            )
        )

        p_e = soup.find("div", class_="snapshot__header", string="P/E Ratio")
        if p_e:
            p_e = float(p_e.parent.contents[0].strip().replace(",", ""))

        script_text = soup.find("script", text=re.compile("high52weeks:"))
        if script_text:
            script_text = str(script_text.string)
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
        try:
            with connection:
                connection.execute(
                    f"""UPDATE s_and_p_500
                    SET (company_code, name, price, p_e,
                    potential_profit) = (?, ?, ?, ?, ?)
                    WHERE short_name = '{short_name}';""",
                    (
                        company_code,
                        name,
                        round(price * rubles_per_usd, 2),
                        p_e,
                        potential_profit,
                    ),
                )
        except sqlite3.IntegrityError:
            pass


async def create_report(
    connection: sqlite3.Connection, report_name: str, main_property: str, statement: str
) -> None:
    """Creates a report in json format, based on information received from database after
        execution of a statement.

    Args:
        connection: to the database;
        report_name: descriptive name of report;
        main_property: of report;
        statement: SELECT SQL statement to execute.

    """

    report_base = [
        {key: value for key, value in zip(("code", "name", main_property), row)}
        for row in connection.execute(statement)
    ]
    with open(
        os.path.join(os.path.dirname(__file__), f"{report_name}.json"),
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(report_base, file, indent=4)


async def main() -> None:
    """Runs whole coroutines."""

    connection = await get_connection_and_create_table(
        db_name=os.path.join(os.path.dirname(__file__), "s&p_500.sqlite"),
        script="""DROP TABLE IF EXISTS s_and_p_500;
        CREATE TABLE s_and_p_500 (short_name text UNIQUE, year_growth real,
        company_code text, name text UNIQUE, price real, p_e real,
        potential_profit real);
        """,
    )
    async with aiohttp.ClientSession() as session:
        rubles_per_usd = await get_exchange_rate(session)
        url = "https://markets.businessinsider.com/index/components/s&p_500?p={}"
        async for page_num in trange(1, 11):
            markup = await fetch_markup(session, url.format(page_num))
            soup = BeautifulSoup(markup, "html.parser")
            await collect_year_growth(connection, soup)
            await collect_info_from_companies_pages(
                connection, session, soup, url, rubles_per_usd
            )
    with connection:
        await create_report(
            connection,
            report_name="most_expensive_shares_top_10",
            main_property="price",
            statement="""SELECT company_code, name, price
            FROM s_and_p_500
            ORDER BY price DESC
            LIMIT 10;""",
        )

        await create_report(
            connection,
            report_name="lowest_p_e_top_10",
            main_property="P/E",
            statement="""SELECT company_code, name, p_e
            FROM s_and_p_500
            WHERE p_e > 0
            ORDER BY p_e ASC NULLS LAST
            LIMIT 10;""",
        )

        await create_report(
            connection,
            report_name="strongest_growth_top_10",
            main_property="growth",
            statement="""SELECT company_code, name, year_growth
            FROM s_and_p_500
            ORDER BY year_growth DESC
            LIMIT 10;""",
        )

        await create_report(
            connection,
            report_name="biggest_potential_profit_top_10",
            main_property="potential profit",
            statement="""SELECT company_code, name, potential_profit
            FROM s_and_p_500
            ORDER BY potential_profit DESC
            LIMIT 10;""",
        )
    connection.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
