"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    """Takes an element and finds the number of occurrences of this element in the tree.

    Args:
        tree: a dictionary (tree), that can contains multiple nested structures.
        Tree can only contains basic structures like: str, list, tuple, dict, set,
        int, bool.

        element: one of basic date structures listed above.

    Returns:
        the number of occurrences of the element in the tree.

    """

    if isinstance(tree, dict):
        tree = tree.values()  # type: ignore
    elif isinstance(tree, (str, bool, int)):
        return 0
    return sum(
        1 if item == element else find_occurrences(item, element) for item in tree
    )


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
