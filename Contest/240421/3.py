from collections import deque


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        steps = [[0, 1], [1, 0]]
        seen = set()
        ans = 0
        stack = deque([[0, 0, 0]])
        while stack:
            i, j, cur = stack.popleft()

