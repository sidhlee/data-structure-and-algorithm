import pytest
from array_manipulation import array_manipulation


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]]), 10),
        ((5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]), 200),
        ((4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]]), 882),
        ((3, [[1, 1, 10], [3, 3, 30], [2, 2, 20]]), 30),
    ],
)
def test(test_input, expected):
    assert array_manipulation(*test_input) == expected


"""
10 [10, 10, 0,  0,  0, 0, 0, 0, 0, 0]
 9 [10, 19, 9,  0,  0, 0, 0, 0, 0, 0]
11 [10, 19, 20, 11, 0, 0, 0, 0, 0, 0]
"""
