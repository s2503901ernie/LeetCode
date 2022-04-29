"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        stack = []
        seen = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    seen[i][j] = True
                    stack.append([i, j])

        while stack:
            cur = stack.pop(0)
            i, j = cur[0], cur[1]
            neighbors = self.get_neighbors(i, j, m, n)
            for neighbor in neighbors:
                x, y = neighbor[0], neighbor[1]
                if seen[x][y] is False:
                    mat[x][y] = mat[i][j] + 1
                    seen[x][y] = True
                    stack.append([x, y])

        return mat

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
