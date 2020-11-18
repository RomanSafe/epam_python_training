"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.


>>> my_precious_logger("error: file not found")
# stderr
'error: file not found'


>>> my_precious_logger("OK")
# stdout
'OK'

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests

You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout

"""
from sys import stderr, stdout


def my_precious_logger(text: str) -> None:
    """Receives a string and write it to stderr if line starts with "error" and to the
    stdout otherwise.

    Args:
        text: for writing to stderr or stdout.

    """
    if not text.endswith("\n"):
        text = text + "\n"
    if text.startswith("error"):
        stderr.write(text)
    else:
        stdout.write(text)
