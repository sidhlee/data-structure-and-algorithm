# Questions Marks

Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between **every pair of two numbers that add up to 10.** If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true
Tags
string manipulationsearchinghash tablefree

## Note

Loop from the beginning of the string and find sum for every pair.

- Check if the character is number
  - Check if prevNum + currentNum == 10
    - then if numQuestions != 3, return false
  - reset numQuestions to 0
  - update prevNum with currentNum
- if the character is "?"
  - increment numQuestions

Edge cases

- start with "???" then numbers add up to 10 -> not possible. eg. in ???19, 1 will reset the counter back to 0
