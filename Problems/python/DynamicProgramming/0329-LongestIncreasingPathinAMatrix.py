"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
"""
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, self.dfs(i, j, ans, matrix))

        return res

    def dfs(self, i, j, ans, mat) -> int:
        if ans[i][j] == 0:
            cur = mat[i][j]
            steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            max_val = 0
            for step in steps:
                row = i + step[0]
                col = j + step[1]
                if 0 <= row < len(mat) and 0 <= col < len(mat[0]) and cur < mat[row][col]:
                    max_val = max(max_val, self.dfs(row, col, ans, mat))
            max_val += 1
            ans[i][j] = max_val

        return ans[i][j]
