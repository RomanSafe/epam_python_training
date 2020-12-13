import keyword


class KeyValueStorage:
    """Wrapper class for a file that works as key-value storage.

    Each key-value pair in the file is separated by "=" symbol, example:
        name=kek
        last_name=top
        song_name=shadilay
        power=9001

    Values can be strings or integer numbers. If a value can be treated both as a
    number and a string, it is treated as number.

    Warning:
        To save all changes in attributes in file-storage you should call
        instance_name.rewrite_file() method, otherwise they would be lost after
        programme termination.

    Attribute:
        __path: path to a file-storage.

    Raises:
        ValueError: if given name cannot be assigned to an attribute;
        ValueError: in case of attribute clash with existing built-in attributes.

    """

    def rewrite_file(self) -> None:
        """Saves all changes in attributes in the file-storage.

        How to use:
            instance_name.rewrite_file()

        If you haven't called this method all changes in attributes would be lost after
        programme termination.

        """

        with open(self.__path, "w", encoding="utf-8") as file:
            for key, value in self.__dict__.items():
                if not key.startswith("_"):
                    file.write(f"{key}={value}\n")

    def _validate_name(self, name: str) -> None:
        """Checks if given name match attribute name rules.

        Args:
            name: attribute name for validation.

        Raises:
            ValueError: if given name cannot be assigned to an attribute;
            ValueError: in case of attribute clash with existing built-in attributes.

        """

        if not name.isidentifier() or keyword.iskeyword(name):
            raise ValueError(f"{name} cannot be assigned to an attribute")
        elif name in dir(self):
            raise ValueError(
                f"{name} attribute clash with existing built-in attributes"
            )

    def __init__(self, path: str) -> None:
        """Creates attributes from path and key-value pairs, received from a
            file-storage.

        If some value contains of numbers it is converted to int type.

        Args:
            __path: path to a file-storage.

        Raises:
            ValueError: if given name cannot be assigned to an attribute;
            ValueError: in case of attribute clash with existing built-in attributes.

        """

        self.__path = path
        with open(self.__path) as file:
            for line in file:
                key, value = line.rstrip().split("=", maxsplit=1)
                self._validate_name(key)
                if value.isdigit():
                    value = int(value)  # type: ignore
                self.__dict__[key] = value

    def __setattr__(self, name, value) -> None:
        """Checks new attribute name and set it up.

        Args:
            name: attribute name;
            value: attribute value.

        Raises:
            ValueError: if given name cannot be assigned to an attribute;
            ValueError: in case of attribute clash with existing built-in attributes.

        """

        self._validate_name(name)
        object.__setattr__(self, name, value)

    def __getitem__(self, name: str) -> str:
        """Makes attributes accessible through square brackets notation.

        Args:
            name: attribute name.

        Returns:
            attribute's value.

        """

        return self.__dict__[name]

    def __setitem__(self, name, value) -> None:
        """Checks new attribute name and assign it through square brackets notation.

        Args:
            name: attribute name;
            value: attribute value.

        Raises:
            ValueError: if given name cannot be assigned to an attribute;
            ValueError: in case of attribute clash with existing built-in attributes.

        """

        self._validate_name(name)
        self.__dict__[name] = value

    def __delitem__(self, name) -> None:
        """Removes attribute with given name if is. Implements deletion through square
            brackets notation.

        Args:
            name: attribute name.

        """

        del self.__dict__[name]
