from typing import List

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


class Solution:
    """
    Runtime: 1154 ms (85%)
    Memory Usage: 25 MB (85%)

    Finding min | max -> sliding window!
    - keep track of min price and max profit while looping through the prices
    - subtract min price from the current price ot update max profit
    """

    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = float("inf"), 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)
        return max_profit

    def maxProfit_start_from_second(self, prices: List[int]) -> int:
        """
        2022-09-24 19:04:22
        Runtime: 1181 ms (85%)
        Memory Usage: 25 MB (86%)

        Since there will be at least one price,
        set the first price as the lowest then
        iterate from the second price.

        sliding window -> update the result as we go!
        """
        profit = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            lowest = min(lowest, prices[i])
            profit = max(profit, prices[i] - lowest)
        return profit

    def maxProfit_easier(self, prices: List[int]) -> int:
        """
        2022-11-07 08:01:28
        - Look back if the list is guaranteed to have at least one item

        [7, 5, 8, 2, 1, 2, 3]
        - loop starting from second item. min_price = first item
        - Only two cases to consider
            - if i is greater than min_price, update profit with (i) - min_price
            - else update min_price
        """
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > min_price:
                max_profit = max(max_profit, prices[i] - min_price)
            else:
                min_price = prices[i]
        return max_profit

    def maxProfit_simple_and_easy(self, prices: List[int]) -> int:
        """
        2022-12-08 08:20:11
        """
        bottom = prices[0]
        mx = 0
        for p in prices:
            mx = max(
                mx, p - bottom
            )  # update max if current price - bottom is greater than max
            bottom = min(bottom, p)  # update bottom if current price is lower
        return mx

    def maxProfit_better_naming(self, prices: List[int]) -> int:
        """
        2023-01-05 06:38:15
        Also uses slicing the looping list
        """
        bottom = prices[0]
        mx_profit = 0
        for p in prices[1:]:
            mx_profit = max(mx_profit, p - bottom)
            bottom = min(bottom, p)
        return mx_profit

    def maxProfit_explicit_condition(self, prices: List[int]) -> int:
        """
        2023-04-04 08:09:55
        easier to read
        """
        mx_profit = 0
        mn_price = float("inf")
        for price in prices:
            profit = price - mn_price
            if price > mn_price and profit > mx_profit:
                mx_profit = profit
            elif price < mn_price:
                mn_price = price
        return mx_profit
