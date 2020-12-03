from lecture_07.homework7.tasks.task1 import find_occurrences

example_tree = {
    0: [("RED",), "BLUE", [], (), {}],
    (1, 2): {
        "simple_key": [False, "list", 800, {"RED", "set"}],
    },
    "RED": {
        "abc": ("BLUE",),
        ("j", "h", "l"): "RED",
        5: {
            "key2": "RED",
            ("tuple", "as", "key"): [{"strings", "in", "set"}, {True: "RED"}],
        },
    },
    ("RED",): "RED",
}


def test_find_occurrences():
    assert find_occurrences(example_tree, "RED") == 8
