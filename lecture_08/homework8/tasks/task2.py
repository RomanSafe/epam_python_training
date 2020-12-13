import sqlite3
from collections.abc import Callable, Iterator
from typing import Any, Optional


class TableData:
    """wrapper class TableData for database table.

    It acts as collection object (implements Collection protocol).

    Example of work:
        if presidents = TableData(
            database_name='example.sqlite', table_name='presidents'
        )
        then
        -`len(presidents)` will give current amount of rows in presidents table in
        database;

        -`presidents['Yeltsin']` return single data row for president with name Yeltsin;

        -`'Yeltsin' in presidents` return True if president with same name exists in
        table, otherwise False;

        -object implements iteration protocol. i.e. you could use it in for loops:
         for president in presidents:
            print(president)  # would print all presidents' names row by row.

        -all above mentioned calls reflect most recent data.

        Attributes:
            database_name: the name of database to connect;
            table_name: the name of table in the database to operate.

    """

    def connect_to_database(method: Callable) -> Callable:  # type: ignore
        """Wrapper to reflect most recent data from the database.

        It supply given method with a new connection and cursor object.

        Args:
            method: method to decorate.

        Returns:
            Decorated method.

        """

        def wrapper(self, *args, **kwargs) -> Any:
            """Connects to the database, creates a cursor object and keeps connection
                opened till the decorated method will complete it's work.

            Returns:
                results of wrapped method's execution.

            """

            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
            return method(self, cursor, *args, **kwargs)

        return wrapper

    def __init__(self, database_name: str, table_name: str) -> None:
        """Initialises class instance.

        Args:
            database_name: the name of database to connect;
            table_name: the name of table in the database to operate.

        """

        self.database_name = database_name
        self.table_name = table_name

    @connect_to_database
    def __len__(self, cursor: sqlite3.Cursor) -> int:
        """Counts current amount of rows in the initialised table of the database.

        Args:
            cursor: Cursor instance.

        Returns:
            amount of rows in the table.

        """

        cursor.execute("SELECT count(*) FROM {}".format(self.table_name))
        return cursor.fetchone()[0]

    @connect_to_database
    def __getitem__(self, cursor: sqlite3.Cursor, value: Any) -> Optional[tuple]:
        """Makes table rows accessible through square brackets notation.

        Args:
            cursor: Cursor instance;
            value: value of the row we are looking for.

        Returns:
            single data row.

        Raises:
            KeyError: if value not in the database.

        """

        cursor.execute(
            "SELECT * FROM {} WHERE name=?".format(self.table_name), (value,)
        )
        row = cursor.fetchone()
        if row:
            return row
        raise KeyError(f"{value} not in the database")

    def __contains__(self, name: Any) -> bool:
        """Makes possible membership testing using search through names column.

        Args:
            name: the name we are looking for in name column.

        Returns:
            True if name is in column, otherwise False.

        """

        try:
            return bool(self[name])
        except KeyError:
            return False

    @connect_to_database
    def __iter__(self, cursor: sqlite3.Cursor) -> Iterator:
        """Creates an iterator object.

        Args:
            cursor: Cursor instance.

        Returns:
            the iterator object itself.

        """

        yield from cursor.execute("SELECT name FROM {}".format(self.table_name))
