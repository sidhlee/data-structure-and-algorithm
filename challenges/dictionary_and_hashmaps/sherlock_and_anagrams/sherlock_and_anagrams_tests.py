import pytest
from sherlock_and_anagrams import sherlock_and_anagrams


@pytest.mark.parametrize(
    "test_input,expected",
    [("abba", 4), ("abcd", 0), ("ifailuhkqq", 3), ("kkkk", 10), ("cdcd", 5)],
)
def test(test_input, expected):
    assert sherlock_and_anagrams(test_input) == expected
