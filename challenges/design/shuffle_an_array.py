from typing import List
from random import randrange

"""
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.

Example 1:

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

Constraints:

1 <= nums.length <= 50
-106 <= nums[i] <= 106
All the elements of nums are unique.
At most 104 calls in total will be made to reset and shuffle.

Hide Hint #1
The solution expects that we always use the original array to shuffle() else some of the test cases fail.
(Credits; @snehasingh31)
"""


class FirstSolution:
    """
    2022-07-23 15:08:34
    Runtime: 267 ms (45%)
    Memory Usage: 17.6 MB (40%)
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        result = self.nums.copy()
        for i in range(len(result)):
            j = randrange(i, len(result))
            result[i], result[j] = result[j], result[i]

        return result


class SecondSolution:
    """
    Runtime: 213 ms (71%)
    Memory Usage: 17.5 MB (73%)

    Create a copy at the instantiation time and shuffle them in place.
    This one creates the list only once whereas the first solution creates new lists every time shuffle is called.

    Read the constraint:
    "At most 104 calls in total will be made to reset and shuffle."
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original_nums = nums.copy()

    def reset(self) -> List[int]:
        return self.original_nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = randrange(i, len(self.nums))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums
