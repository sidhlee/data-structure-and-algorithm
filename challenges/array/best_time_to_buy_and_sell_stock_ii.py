"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""

from typing import List


class Solution:
    def maxProfit_look_back(self, prices: List[int]) -> int:
        """
        Runtime: 86 ms (58%)
        Memory Usage: 15 MB (98%)

        starting from index 1 and looking back is a good way to avoid index out of range exception
        when you're comparing neighboring values in the same array.
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    def maxProfit_two_pointers_with_while(self, prices: List[int]) -> int:
        """
        2022-06-21T12:01:28.389Z
        Runtime: 111 ms (27%)
        Memory Usage: 15.1 MB (68%)

        If you know you're going to loop through the entire list, use for loop
        Also, you can incrementally add to the profit in each iteration.
        If you're going to wait until the peak, you need pointer to save the bottom index 😔
        """
        i = 0
        j = 1
        profit = 0
        while j < len(prices):
            if prices[i] > prices[j]:
                i += 1
                j += 1
            else:
                if j == len(prices) - 1:
                    profit += prices[j] - prices[i]
                    j += 1
                elif prices[j] > prices[j + 1]:
                    profit += prices[j] - prices[i]
                    i = j + 1
                    j = i + 1
                else:
                    j += 1

        return profit
