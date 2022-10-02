"""
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.



Example 1:

Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.
Example 2:

Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 10^9 + 7.


Constraints:

1 <= n, k <= 30
1 <= target <= 1000
"""


class Solution1:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        d = {}
        return self.dfs(n, k, target, d) % (10 ** 9 + 7)

    def dfs(self, n, k, target, d):
        if n == 0:
            return 1 if target == 0 else 0
        if (n, target) in d:
            return d[(n, target)]
        cur = 0
        start = max(0, target - k)
        for t in range(start, target):
            cur += self.dfs(n - 1, k, t, d)
        d[(n, target)] = cur

        return cur


class Solution2:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        m = 10 ** 9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for t in range(j, target + 1):
                    dp[i][t] = (dp[i][t] + dp[i - 1][t - j])
        return dp[-1][-1] % m
