import sqlite3
from collections.abc import Iterator
from typing import Any


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
            table_name: the name of table in the database to operate;
            conn: connection object;
            cursor: the database cursor object.

        Raises:
            StopIteration if there are no further items for iteration (iterator is
            exhausted).

    """

    def __init__(self, database_name: str, table_name: str) -> None:
        """Initialises class instance.

        Args:
            database_name: the name of database to connect;
            table_name: the name of table in the database to operate.

        """

        self.table_name = table_name
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def __len__(self) -> int:
        """Counts current amount of rows in the initialised table of the database.

        Returns:
            amount of rows in the table.

        """

        self.cursor.execute("SELECT count(*) FROM {}".format(self.table_name))
        return self.cursor.fetchone()[0]

    def __getitem__(self, value: Any) -> tuple:
        """Makes table rows accessible through square brackets notation.

        Args:
            value: value of the row we are looking for.

        Returns:
            single data row.

        """

        self.cursor.execute(
            "SELECT * FROM {} WHERE name=?".format(self.table_name), (value,)
        )
        return self.cursor.fetchone()

    def __contains__(self, name: Any) -> bool:
        """Makes possible membership testing using search through names column.

        Args:
            name: the name we are looking for in name column.

        Returns:
            True if name is in column, otherwise False.

        """

        self.cursor.execute(
            "SELECT * FROM {} WHERE name=?".format(self.table_name), (name,)
        )
        return self.cursor.fetchone()

    def __iter__(self) -> Iterator:
        """Creates an iterator object.

        Returns:
            the iterator object itself.

        """

        self.cursor.execute("SELECT name FROM {}".format(self.table_name))
        return self

    def __next__(self) -> str:
        """Fetch and return the next row after executing a SELECT statement in __iter__
            method.

        Raises:
            StopIteration: if there are no further items.

        Returns:
            content of received row.

        """

        while row := self.cursor.fetchone():
            return row[0]
        raise StopIteration

    def close(self) -> None:
        """Closes current connection. This method must be called after termination of
        all operations with database.

        """

        self.conn.close()
