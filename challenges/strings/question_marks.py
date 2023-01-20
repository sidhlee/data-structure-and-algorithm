def QuestionsMarks_linear(strParam: str):
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


QuestionMarks = QuestionsMarks_linear
