"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.



Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1


Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = 1
                else:
                    obstacleGrid[i][j] = 0

        stone = False
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                stone = True
            if stone is True:
                obstacleGrid[i][0] = 0
        stone = False
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j] == 0:
                stone = True
            if stone is True:
                obstacleGrid[0][j] = 0

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 0:
                    continue
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[-1][-1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            ans[0][0] = 1
        else:
            return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    if i > 0:
                        ans[i][j] += ans[i-1][j]
                    if j > 0:
                        ans[i][j] += ans[i][j-1]

        return ans[-1][-1]
