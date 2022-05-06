"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.



Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2


Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                ans += self.helper(i, j, m, n, grid)

        return ans

    def helper(self, i, j, m, n, grid):
        stack = [[i, j]]
        ans = 1
        while stack:
            cur = stack.pop(0)
            i, j = cur[0], cur[1]
            grid[i][j] = 1
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                ans *= 0
            dirs = self.get_dirs(i, j, m, n, grid)
            for d in dirs:
                stack.append([d[0], d[1]])

        return ans

    def get_dirs(self, i, j, m, n, grid):
        dirs = []
        if i - 1 >= 0 and grid[i-1][j] == 0:
            dirs.append([i-1, j])
        if i + 1 < m and grid[i+1][j] == 0:
            dirs.append([i+1, j])
        if j - 1 >= 0 and grid[i][j-1] == 0:
            dirs.append([i, j-1])
        if j + 1 < n and grid[i][j+1] == 0:
            dirs.append([i, j+1])

        return dirs
