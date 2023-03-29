import pytest
from count_triplets import count_triplets
from utils.parser import parse_list

"""
1, 1, 2, 2, 4, 4 -> 024, 025, 034, 035, 124, 125, 134, 135
"""


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (([1, 2, 2, 4], 2), 2),
        (([1, 3, 9, 9, 27, 81], 3), 6),
        (([1, 5, 5, 25, 125], 5), 4),
        (([1] * 100, 1), 161700),
    ],
)
def test_sorted(test_input, expected):
    assert count_triplets(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (([4, 2, 2, 1], 2), 0),
        (([4, 2, 1, 2], 2), 0),
        (([4, 2, 1, 4, 2, 1], 2), 0),
        (([1, 2, 4, 1], 2), 1),
        (([4, 1, 2, 4], 2), 1),
    ],
)
def test_unsorted(test_input, expected):
    assert count_triplets(*test_input) == expected


def test_case_10():
    """
    {
        1: 9911
        1000000000: 9939
        100000: 10161
        100: 9890
        10: 10081
        10000000: 10094
        100000000: 9814
        1000: 10090
        1000000: 10034
        10000: 9986
    }

    Ordered:
    {
        1: 9911,
        10: 10081,
        100: 9890,
        1000: 10090,
        10000: 9986,
        100000: 10161,
        1000000: 10034,
        10000000: 10094,
        100000000: 9814,
        1000000000: 9939,
    }

    """
    test_case_10_list = parse_list(
        "challenges/dictionary_and_hashmaps/count_triplets/test_case_10.txt",
        to_int=True,
    )

    assert len(test_case_10_list) == 100000
    assert count_triplets(test_case_10_list, 10) == 1339347780085
