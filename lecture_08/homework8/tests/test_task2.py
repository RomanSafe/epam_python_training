import pytest

from lecture_08.homework8.tasks.task2 import TableData


@pytest.fixture
def operate_database():
    presidents = TableData(
        database_name="lecture_08/homework8/tests/example.sqlite",
        table_name="presidents",
    )
    yield presidents
    presidents.close()


def test_table_data_true(operate_database):
    presidents = operate_database
    print("Yeltsin" in presidents)

    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert len(presidents) == 3
    assert "Yeltsin" in presidents


def test_table_data_false(operate_database):
    presidents = operate_database
    print("Medvedev" in presidents)

    assert "Medvedev" not in presidents


def test_table_data_iterator(operate_database):
    presidents = operate_database
    string_with_presidents = ""
    for president in presidents:
        print(president)
        string_with_presidents += president

    assert string_with_presidents == "Big Man TyroneTrumpYeltsin"
