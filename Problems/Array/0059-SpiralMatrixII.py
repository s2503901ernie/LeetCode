"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        row_start = 0
        col_start = 0
        i = 0
        j = 0
        count = 1
        while row_start < n and col_start < n:
            for j in range(col_start, n):
                ans[i][j] = count
                count += 1
            for i in range(row_start + 1, n):
                ans[i][j] = count
                count += 1
            for j in range(n - 2, col_start - 1, -1):
                ans[i][j] = count
                count += 1
            for i in range(n - 2, row_start, -1):
                ans[i][j] = count
                count += 1
            n -= 1
            row_start += 1
            col_start += 1

        return ans
