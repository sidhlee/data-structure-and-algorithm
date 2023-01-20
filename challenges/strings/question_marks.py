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


QuestionMarks = question_marks_simpler
