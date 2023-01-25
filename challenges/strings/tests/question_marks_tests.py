from unittest import TestCase
from challenges.strings.question_marks import QuestionMarks


class QuestionMarksTests(TestCase):
    def test__false__no_add_upto_ten(self):
        self.assertEqual(QuestionMarks("aa6?9"), "false")

    def test__false__no_three_question_marks_between_nums(self):
        self.assertEqual(QuestionMarks("9???1???9??1???9"), "false")

    def test__true__three_question_marks_with_letters_in_between(self):
        self.assertEqual(QuestionMarks("acc?7??sss?3rr1??????5"), "true")
        self.assertEqual(QuestionMarks("5??aaaaaaaaaaaaaaaaaaa?5?a??5"), "true")

    def test__true(self):
        self.assertEqual(QuestionMarks("9???1???9???1???9"), "true")

    def test__pair_without_question_mark(self):
        self.assertEqual(QuestionMarks("9???191???9"), "false")
