import pytest
from new_year_chaos import new_year_chaos


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([5, 1, 2, 3, 7, 8, 6], "Too chaotic"),
        ([2, 1, 5, 3, 4], 3),
        ([2, 5, 1, 3, 4], "Too chaotic"),
        ([1, 2, 5, 3, 4, 7, 8, 6], 4),
    ],
)
def test__either_bribe_or_get_bribed(
    capsys: pytest.CaptureFixture, test_input, expected
):
    new_year_chaos(test_input)
    captured = capsys.readouterr()
    assert captured.out.strip() == str(expected)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([1, 2, 5, 3, 7, 8, 6, 4], 7),
        ([3, 2, 1], 3),
        ([2, 3, 0, 5, 1, 4], 6),
        ([2, 1, 5, 6, 3, 4, 9, 8, 11, 7, 10], 11),
    ],
)
def test__get_bribed_and_bribe(capsys: pytest.CaptureFixture, test_input, expected):
    new_year_chaos(test_input)
    captured = capsys.readouterr()
    assert captured.out.strip() == str(expected)
