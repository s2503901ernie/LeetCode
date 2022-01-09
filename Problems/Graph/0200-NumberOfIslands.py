"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for row in range(m):
            for col in range(n):
                ans += self.dfs(row, col, grid)

        return ans

    def dfs(self, row, col, grid):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != "1":
            return 0
        grid[row][col] = "*"
        self.dfs(row - 1, col, grid)
        self.dfs(row + 1, col, grid)
        self.dfs(row, col - 1, grid)
        self.dfs(row, col + 1, grid)

        return 1


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] != "1":
                    continue
                ans += self.dfs(row, col, grid)

        return ans

    def dfs(self, row, col, grid):
        queue = [[row, col]]
        while queue:
            current = queue.pop()
            row, col = current[0], current[1]
            if grid[row][col] != "1":
                continue
            grid[row][col] = "A"
            neighbors = self.get_neighbors(row, col, grid)
            for neighbor in neighbors:
                queue.append(neighbor)

        return 1

    def get_neighbors(self, row, col, grid):
        neighbors = []
        if row > 0 and grid[row - 1][col] == "1":
            neighbors.append([row - 1, col])
        if col > 0 and grid[row][col - 1] == "1":
            neighbors.append([row, col - 1])
        if row < len(grid) - 1 and grid[row + 1][col] == "1":
            neighbors.append([row + 1, col])
        if col < len(grid[row]) - 1 and grid[row][col + 1] == "1":
            neighbors.append([row, col + 1])

        return neighbors
