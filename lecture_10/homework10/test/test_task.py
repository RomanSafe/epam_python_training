import os.path
import sqlite3
from pathlib import Path

import pytest

from lecture_10.homework10.task.task import (
    add_info_to_db,
    collect_year_growth,
    create_report,
    fetch_markup,
    get_comp_pages_html,
    get_companies_info,
    get_companies_links,
    get_exchange_rate,
    get_main_pages_html,
    main,
    write_json,
)


@pytest.mark.asyncio
async def test_main(event_loop):
    await event_loop.run_until_complete(main())


def test_main_result():
    directory_path = Path(os.path.dirname(__file__))
    files_iterator = directory_path.glob("*.json")
    file_count = 0
    for _ in files_iterator:
        file_count += 1
    assert file_count == 4


@pytest.fixture
def get_db_cursor():
    database_name = os.path.join(os.path.dirname(__file__), "s&p_500.sqlite")
    with sqlite3.connect(database_name) as conn:
        yield conn.cursor()


def test_main_amount_of_companies(get_db_cursor):
    cursor = get_db_cursor()
    cursor.execute("SELECT count(*) FROM name;")
    assert cursor.fetchone()[0] == 438
