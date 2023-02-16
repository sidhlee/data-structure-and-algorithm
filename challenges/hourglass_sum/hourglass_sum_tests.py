import pytest
from hourglass_sum import hourglass_sum


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            [
                [1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 2, 4, 4, 0],
                [0, 0, 0, 2, 0, 0],
                [0, 0, 1, 2, 4, 0],
            ],
            19,
        ),
        (
            [
                [1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 9, 2, -4, -4, 0],
                [0, 0, 0, -2, 0, 0],
                [0, 0, -1, -2, -4, 0],
            ],
            13,
        ),
        (
            [
                [-9, -9, -9, 1, 1, 1],
                [0, -9, 0, 4, 3, 2],
                [-9, -9, -9, 1, 2, 3],
                [0, 0, 8, 6, 6, 0],
                [0, 0, 0, -2, 0, 0],
                [0, 0, 1, 2, 4, 0],
            ],
            28,
        ),
    ],
)
def test(test_input, expected):
    assert hourglass_sum(test_input) == expected
