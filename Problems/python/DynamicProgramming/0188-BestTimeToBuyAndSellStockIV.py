"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        if k >= len(prices) // 2:
            ans = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    ans += prices[i] - prices[i - 1]
            return ans

        dp = [0 for _ in range(len(prices))]
        for _ in range(k):
            pre = 0
            for i in range(1, len(prices)):
                profit = prices[i] - prices[i - 1]
                pre = max(pre + profit, dp[i])
                dp[i] = max(pre, dp[i - 1])

        return dp[-1]
