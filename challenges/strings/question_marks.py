def QuestionsMarks_linear(strParam: str):
    """
    2023-01-20 06:46:41
    """
    pair_sum = 0
    question_marks = 0
    has_pair = False
    for i, char in enumerate(strParam):
        if char.isnumeric():
            if pair_sum == 0:
                pair_sum += int(char)
            elif pair_sum + int(char) == 10:
                if question_marks != 3:
                    return "false"
                has_pair = True
                question_marks = 0  # reset
                # if there is a single number between question marks, reuse it
                next_is_qm = i < len(strParam) - 1 and strParam[i + 1] == "?"
                pair_sum = int(char) if next_is_qm else 0
        elif char == "?":
            question_marks = question_marks + 1 if pair_sum > 0 else 0

    return "true" if has_pair else "false"


def question_marks_simpler(string: str):
    """
    2023-01-20 06:46:48
    """
    num = 11  # no single number can be added to this and make 10
    question_marks = 0
    has_pair = False
    for char in string:
        if char.isnumeric():
            if num + int(char) == 10:
                if question_marks != 3:
                    return "false"
                has_pair = True
            # always update the number because we only care about single numbers
            num = int(char)
            # once we see a number, reset the question marks back to 0
            question_marks = 0
        elif char == "?":
            question_marks += 1
    return "true" if has_pair else "false"


def question_marks_unnecessary_conditions(strParam):
    """
    2023-01-25 07:24:40

    The requirement says "3 question marks between every pair of two numbers that add up to 10."
    So, we don't need to look behind to check if it was a question mark.

    WE JUST NEED TO FIND A PAIR OF NUMBER THAT ADD UP TO 10!!!
    """

    num_before_q = 0  # initializing with 0 won't affect the result
    num_q = 0
    has_pair = False
    for i, c in enumerate(strParam):
        if c.isnumeric():
            if strParam[i - 1] == "?" and num_before_q + int(c) == 10:
                if num_q != 3:
                    return "false"
                has_pair = True
                num_before_q = int(c)
            if i + 1 < len(strParam) and strParam[i + 1] == "?":
                num_before_q = int(c)
            num_q = 0
        elif c == "?":
            num_q += 1

    return has_pair


def question_marks_better(strParam):
    """
    2023-01-26 06:59:13
    readable
    """
    prevNum = 11  # so that the sum with any single digit number cannot be 10
    questions = 0
    has_pair = False
    for c in strParam:
        if c.isnumeric():
            currNum = int(c)
            if prevNum + currNum == 10:
                if questions != 3:
                    return "false"
                has_pair = True
            questions = 0
            prevNum = currNum
        elif c == "?":
            questions += 1

    return "true" if has_pair else "false"


QuestionMarks = question_marks_better
