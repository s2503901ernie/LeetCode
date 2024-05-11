from collections import defaultdict, deque


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        dirs = [[0, 1], [1, 0], [1, 1]]
        for i in range(n - 1):
            for j in range(n - 1):
                d = defaultdict(int)
                d[grid[i][j]] += 1
                for dd in dirs:
                    x, y = i + dd[0], j + dd[1]
                    d[grid[x][y]] += 1
                if d['B'] >= 3 or d['W'] >= 3:
                    return True
        return False

