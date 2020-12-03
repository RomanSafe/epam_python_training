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

    element_occurrences = 0
    element_type = type(element)

    def _get_collection_items(collection):
        # Receives list or tuple or set and creates a generator from its items.
        for item in collection:
            yield item

    def _get_dictionary_items(dictionary):
        # Creates a generator of dictionary keys and values.
        for key_value in tree.items():
            for item in key_value:
                yield item

    if isinstance(tree, dict):
        iterate_through = _get_dictionary_items
    else:
        iterate_through = _get_collection_items
    for item in iterate_through(tree):
        if isinstance(item, element_type) and item == element:
            element_occurrences += 1
        elif isinstance(item, (list, tuple, set, dict)):
            element_occurrences += find_occurrences(item, element)  # type: ignore

    return element_occurrences


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
