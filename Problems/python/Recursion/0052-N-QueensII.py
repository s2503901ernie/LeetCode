"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.



Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 9
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        nums = [-1 for _ in range(n)]
        self.dfs(0, nums, 0)

        return self.ans

    def dfs(self, cur, nums, path):
        if path == len(nums):
            self.ans += 1
            return
        for i in range(len(nums)):
            nums[cur] = i
            if self.is_valid(cur, nums) is True:
                self.dfs(cur + 1, nums, path + 1)

    def is_valid(self, cur, nums):
        for i in range(cur):
            if abs(nums[i] - nums[cur]) == cur - i or nums[cur] == nums[i]:
                return False
        return True
