def BracketCombinations_binary_decision_tree(num):
    """
    2023-01-24 06:52:20
    """

    def inner(num_open, num_closed):
        if num_open <= 0 or num_closed <= 0:
            return 1
        if num_open >= num_closed:
            return inner(num_open - 1, num_closed) + inner(num_open, num_closed - 1)
        else:
            return inner(num_open, num_closed - 1)

    return inner(num - 1, num - 1)


def bracket_combinations_math(num):
    """
    000111
    001011
    001101
    010011
    010101
    - must start with 0 and end with 1
    - at any given index, there cannot be more 1s than 0s.

    [0] 1 - only 0
    [1] 2 - 0 | 1
    [2]
    """
    return None


bracket_combinations = bracket_combinations_math
