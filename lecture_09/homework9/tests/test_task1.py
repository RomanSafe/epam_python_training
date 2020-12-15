from lecture_09.homework9.tasks.task1 import merge_sorted_files


def test_merge_sorted_files():
    assert (
        list(
            merge_sorted_files(
                [
                    "lecture_09/homework9/tests/file1.txt",
                    "lecture_09/homework9/tests/file2.txt",
                    "lecture_09/homework9/tests/file3.txt",
                ]
            )
        )
        == [0, 1, 1, 2, 3, 4, 5, 6, 7]
    )
