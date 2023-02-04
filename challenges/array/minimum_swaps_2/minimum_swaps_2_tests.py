import pytest
from minimum_swaps_2 import minimum_swaps


@pytest.mark.parametrize(
    "test_input,expected",
    [([4, 3, 1, 2], 3), ([2, 3, 4, 1, 5], 3), ([1, 3, 5, 2, 4, 6, 7], 3)],
)
def test__success(test_input, expected):
    assert minimum_swaps(test_input) == expected
