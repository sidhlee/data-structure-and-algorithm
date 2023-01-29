def BracketCombinations_binary_decision_tree(num):
    """
    2023-01-24 06:52:20
    """

    def inner(num_open=num, num_closed=num):
        # Ran out of either of brackets -> 1 decision from here
        if num_open <= 0 or num_closed <= 0:
            return 1
        # If we have more remaining open bracket, we can branch out into 2 cases
        if num_open > num_closed:
            return inner(num_open - 1, num_closed) + inner(num_open, num_closed - 1)
        # If we have the same number of remaining brackets,
        # we can only branch into using closed bracket
        else:
            return inner(num_open, num_closed - 1)

    return inner()


def bracket_combinations_math(num):
    """
    000111
    001011
    001101
    010011
    010101
    - must start with 0 and end with 1
    - at any given index, there cannot be more 1s than 0s.

    Permutation on all elements = (2 * num)! -> 6!
    2 sets of 3 interchangeable numbers = num! * num! -> 3! * 3!

    1/2 of permutation is invalid (starting with 1)

    """
    return None


bracket_combinations = BracketCombinations_binary_decision_tree
