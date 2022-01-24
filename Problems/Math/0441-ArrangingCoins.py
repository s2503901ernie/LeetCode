"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.



Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.


Constraints:

1 <= n <= 2^31 - 1
"""


class Solution1:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        i = 1
        while n >= 0:
            n -= i
            i += 1
            ans += 1
        if n < 0:
            return ans - 1
        else:
            return ans


class Solution2:
    def arrangeCoins(self, n: int) -> int:
        return int(((8 * n + 1) ** 0.5 - 1) / 2)
