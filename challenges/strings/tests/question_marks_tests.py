from unittest import TestCase
from challenges.strings.question_marks import QuestionMarks


class QuestionMarksTests(TestCase):
    def test__false(self):
        self.assertEqual(QuestionMarks("9???1???9??1???9"), "false")

    def test__true(self):
        self.assertEqual(QuestionMarks("5??aaaaaaaaaaaaaaaaaaa?5?a??5", "true"))
