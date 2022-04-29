"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        stack = []
        seen = [[False for _ in range(n)] for _ in range(m)]
        tmp = 0
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    stack.append([i, j])
                    seen[i][j] = True
                    tmp += 1
                elif grid[i][j] == 0:
                    seen[i][j] = True
                    tmp += 1
        if tmp == m * n:
            return 0

        while stack:
            for _ in range(len(stack)):
                cur = stack.pop(0)
                i, j = cur[0], cur[1]
                dirs = self.get_dirs(i, j, m, n, seen)
                for dir in dirs:
                    x, y = dir[0], dir[1]
                    seen[x][y] = True
                    stack.append([x, y])
            count += 1

        count -= 1
        for i in range(m):
            for j in range(n):
                if seen[i][j] is False:
                    return -1
        return count

    def get_dirs(self, i, j, m, n, seen):
        dirs = []
        if i - 1 >= 0 and seen[i - 1][j] is False:
            dirs.append([i - 1, j])
        if i + 1 < m and seen[i + 1][j] is False:
            dirs.append([i + 1, j])
        if j - 1 >= 0 and seen[i][j - 1] is False:
            dirs.append([i, j - 1])
        if j + 1 < n and seen[i][j + 1] is False:
            dirs.append([i, j + 1])

        return dirs
