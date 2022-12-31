"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
"""
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.m, self.n = len(grid), len(grid[0])
        steps = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0 or grid[i][j] == 1:
                    steps += 1
                if grid[i][j] == 1:
                    start = (i, j)
        self.dfs(start[0], start[1], grid, steps)

        return self.ans

    def dfs(self, i, j, grid, steps):
        if grid[i][j] == -1 or grid[i][j] == 3:
            return
        if grid[i][j] == 2:
            if steps == 0:
                self.ans += 1
            return
        grid[i][j] = 3 if grid[i][j] == 0 else 1
        togo = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for go in togo:
            nx, ny = i + go[0], j + go[1]
            if nx < 0 or nx == self.m or ny < 0 or ny == self.n or grid[nx][ny] == 1:
                continue
            self.dfs(nx, ny, grid, steps - 1)
        grid[i][j] = 0 if grid[i][j] == 3 else 1
