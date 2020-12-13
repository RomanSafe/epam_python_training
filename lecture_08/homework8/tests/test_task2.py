from lecture_08.homework8.tasks.task2 import TableData


def test_table_data_true():
    presidents = TableData(
        database_name="lecture_08/homework8/tests/example.sqlite",
        table_name="presidents",
    )

    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert len(presidents) == 3
    assert "Yeltsin" in presidents


def test_table_data_false():
    presidents = TableData(
        database_name="lecture_08/homework8/tests/example.sqlite",
        table_name="presidents",
    )

    assert "Medvedev" not in presidents


def test_table_data_iterator():
    presidents = TableData(
        database_name="lecture_08/homework8/tests/example.sqlite",
        table_name="presidents",
    )
    string_with_presidents = ""
    for president in presidents:
        string_with_presidents += president[0]

    assert string_with_presidents == "Big Man TyroneTrumpYeltsin"
