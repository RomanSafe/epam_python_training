"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    directory_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """If there are no tokenizer, it will counts lines in all files in directory_path
        with given file_extension.

    If given tokenizer, it counts tokens.

    Using:
        For dir with two files from hw1.py:
        >>> universal_file_counter(test_dir, "txt")
        6
        >>> universal_file_counter(test_dir, "txt", str.split)
        6

    Args:
        directory_path: Path object pointing to directory for count;
        file_extension: type of files for search in directory_path;
        tokenizer: optional function for work with lines of found files. Defaults to
        None.

    Returns:
        amount of lines or tokens in found files.

    """

    files_iterator = directory_path.glob(f"*.{file_extension}")
    token_count = 0
    for file_path in files_iterator:
        with file_path.open() as file:
            if tokenizer:
                token_iterable = map(tokenizer, (line for line in file))
                for item in token_iterable:
                    token_count += len(item)
            else:
                for _ in file:
                    token_count += 1
    return token_count
