"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from typing import List


class Solution:
    """dfs"""
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        seen = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if seen[i][j] or grid[i][j] == 0:
                    continue
                ans = max(ans, self.dfs(grid, i, j, seen, m, n))

        return ans

    def dfs(self, grid, i, j, seen, m, n):
        if seen[i][j] is True or grid[i][j] == 0:
            return 0
        area = 1
        seen[i][j] = True
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for move in moves:
            r, c = i + move[0], j + move[1]
            if 0 <= r < m and 0 <= c < n and seen[r][c] is False and grid[r][c] == 1:
                area += self.dfs(grid, r, c, seen, m, n)

        return area


class Solution2:
    """bfs"""
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        seen = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if seen[i][j] == True or grid[i][j] == 0:
                    continue
                ans = max(ans, self.bfs(grid, i, j, seen, m, n))

        return ans

    def bfs(self, grid, i, j, seen, m, n):
        stack = [[i, j]]
        area = 0
        while stack:
            cur = stack.pop(0)
            i, j = cur[0], cur[1]
            if seen[i][j] or grid[i][j] == 0:
                continue
            area += 1
            seen[i][j] = True
            moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for move in moves:
                x, y = i + move[0], j + move[1]
                if 0 <= x < m and 0 <= y < n and seen[x][y] is False and grid[x][y] == 1:
                    stack.append([x, y])

        return area

