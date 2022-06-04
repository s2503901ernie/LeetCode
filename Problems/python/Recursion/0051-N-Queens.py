"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        self.dfs(0, [-1 for _ in range(n)], [], ans)

        return ans

    def dfs(self, cur, nums, path, ans):
        if cur == len(nums):
            ans.append(path)
            return
        for i in range(len(nums)):
            nums[cur] = i
            if self.is_valid(cur, nums) is True:
                tmp = "." * len(nums)
                self.dfs(cur + 1, nums, path + [tmp[:i] + 'Q' + tmp[i+1:]], ans)

    def is_valid(self, cur, nums):
        for i in range(cur):
            if abs(nums[i] - nums[cur]) == cur - i or nums[cur] == nums[i]:
                return False
        return True
