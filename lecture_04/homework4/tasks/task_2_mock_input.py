"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


>>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen

"""
import urllib.request
from http.client import HTTPException
from urllib.error import URLError


def count_dots_on_i(url: str) -> int:
    """Accepts an url as input and count how many letters "i" are present in the HTML
    by this url.

    Args:
        url: address of web-page on the Internet.

    Raises:
        ValueError: in case of any network error.

    Returns:
        amount of letters "i" are present in the HTML by this URL.

    """
    result = 0
    try:
        with urllib.request.urlopen(url) as response:
            for byte_line in response:
                str_line = byte_line.decode("utf-8")
                for symbol in str_line:
                    if symbol == "i":
                        result += 1
    except (ConnectionError, ValueError, HTTPException, URLError):
        raise ValueError(f"Unreachable {url}") from None

    return result


if __name__ == "__main__":
    print(count_dots_on_i("https://example.com/"))
