from itertools import islice


class KeyValueStorage:
    """Wrapper class for a file that works as key-value storage.

    Each key-value pair in the file is separated by "=" symbol, example:
        name=kek
        last_name=top
        song_name=shadilay
        power=9001

    Values can be strings or integer numbers. If a value can be treated both as a
    number and a string, it is treated as number.
    In case of attribute clash, existing built-in attributes take precedence.

    Warning:
        To save all changes in attributes in file-storage you should call
        instance_name.rewrite_file() method, otherwise they would be lost after
        programme termination.

    Attribute:
        path: path to a file-storage.

    Raises:
        ValueError: when value cannot be assigned to an attribute (for example when
        there's a line `1=something`).

    """

    def rewrite_file(self) -> None:
        """Saves all changes in attributes in the file-storage.

        How to use:
            instance_name.rewrite_file()

        If you haven't called this method all changes in attributes would be lost after
        programme termination.

        """

        with open(self.path, "w", encoding="utf-8") as file:
            for key, value in islice(self.__dict__.items(), 1, None):
                file.write(f"{key}={value}\n")

    def __init__(self, path: str) -> None:
        """Creates attributes from path and key-value pairs, received from a
            file-storage.

        If some value contains of numbers it is converted to int type.
        In case of attribute clash, existing built-in attributes take precedence.

        Args:
            path: path to a file-storage.

        Raises:
            ValueError: when value cannot be assigned to an attribute (for example when
            there's a line `1=something`).

        """

        self.path = path
        with open(path) as file:
            for line in file:
                key, value = line.rstrip().split("=")
                if key.isdigit():
                    raise ValueError(f"{key} cannot be assigned to an attribute")
                elif key in dir(type(self)):
                    continue
                elif value.isdigit():
                    value = int(value)  # type: ignore
                self.__dict__[key] = value

    def __getitem__(self, key: str) -> str:
        """Makes attributes accessible through square brackets notation.

        Args:
            key: attribute name.

        Returns:
            attribute's value.

        """

        return self.__dict__[key]
