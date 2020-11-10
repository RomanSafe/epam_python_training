"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document

"""
from string import punctuation
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Gets 10 longest words consisting from largest amount of unique symbols and
    returns them in a list.

    Args:
        file_path: the pathname (absolute or relative to the current working directory)
        of the file to be opened.

    Returns:
        List of 10 longest unique words.

    """
    counter = {}
    with open(file_path, encoding="unicode-escape") as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip(punctuation)
                if word not in counter:
                    counter[word] = len(frozenset(word))
    return sorted(counter, key=lambda item: counter[item], reverse=True)[:10]


def get_rarest_char(file_path: str) -> str:
    """Gets rarest symbol for document and returns it.

    Args:
        file_path: the pathname (absolute or relative to the current working directory)
        of the file to be opened.

    Returns:
        rarest symbol.

    """
    counter = {}
    with open(file_path, encoding="unicode-escape") as file:
        for line in file:
            symbols_ = tuple(line)
            for symbol in symbols_:
                if symbol not in counter:
                    counter[symbol] = 1
                else:
                    counter[symbol] += 1
    return min(counter, key=lambda item: counter[item])


def count_punctuation_chars(file_path: str) -> int:
    """Counts punctuation characters and returns their amount.

    Args:
        file_path: the pathname (absolute or relative to the current working directory)
        of the file to be opened.

    Returns:
        amount of punctuation characters.

    """
    counter = 0
    with open(file_path, encoding="unicode-escape") as file:
        for line in file:
            symbols_ = tuple(line)
            for symbol in symbols_:
                if symbol in punctuation:
                    counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    """Counts non ascii characters and returns their amount.

    Args:
        file_path: the pathname (absolute or relative to the current working directory)
        of the file to be opened.

    Returns:
        amount of non ascii characters.

    """
    counter = 0
    with open(file_path, encoding="unicode-escape") as file:
        for line in file:
            symbols_ = tuple(line)
            for symbol in symbols_:
                if not symbol.isascii():
                    counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Gets the most common non ascii character from a text document and returns it.

    Args:
        file_path: the pathname (absolute or relative to the current working directory)
        of the file to be opened.

    Returns:
        the most common non ascii character.

    """
    counter = {}
    with open(file_path, encoding="unicode-escape") as file:
        for line in file:
            symbols_ = filter(lambda symbol: not symbol.isascii(), tuple(line))
            for symbol in symbols_:
                if symbol not in counter:
                    counter[symbol] = 1
                else:
                    counter[symbol] += 1
    return max(counter, key=lambda item: counter[item])
