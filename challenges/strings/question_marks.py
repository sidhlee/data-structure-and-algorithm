import re


def QuestionsMarks_fail(strParam):
    # code goes here
    strParam = re.sub("[a-zA-Z]", "", strParam)
    pair_sum = 0
    question_marks = 0
    is_pair = False
    for char in strParam:
        if char.isnumeric():
            if pair_sum == 0:
                pair_sum += int(char)
            elif pair_sum + int(char) == 10:
                if question_marks != 3:
                    return "false"
                is_pair = True
            else:
                pair_sum = 0
        elif pair_sum > 0:
            question_marks += 1
        else:
            question_marks = 0

    return is_pair


QuestionMarks = QuestionsMarks_fail
