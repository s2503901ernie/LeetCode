"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.


Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 10^6
"""
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        eff = [[float('inf') for _ in range(n)] for _ in range(m)]
        eff[0][0] = 0
        stack = [[0, 0]]
        while stack:
            cur = stack.pop(0)
            i, j = cur[0], cur[1]
            neighbors = self.get_neighbors(i, j, m, n)
            for neighbor in neighbors:
                x, y = neighbor[0], neighbor[1]
                new_eff = max(eff[i][j], abs(heights[i][j] - heights[x][y]))
                if eff[x][y] > new_eff:
                    eff[x][y] = new_eff
                    stack.append([x, y])

        return eff[-1][-1]

    def get_neighbors(self, i, j, m, n):
        neighbors = []
        if i - 1 >= 0:
            neighbors.append([i-1, j])
        if i + 1 < m:
            neighbors.append([i+1, j])
        if j - 1 >= 0:
            neighbors.append([i, j-1])
        if j + 1 < n:
            neighbors.append([i, j+1])
        return neighbors
