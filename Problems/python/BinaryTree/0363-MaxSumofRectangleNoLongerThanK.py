"""
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.



Example 1:


Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-10^5 <= k <= 10^5

"""
import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n - 1):
                matrix[i][j + 1] += matrix[i][j]
        ans = -float('inf')
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = [matrix[i][y2] - (matrix[i][y1 - 1] if y1 > 0 else 0)
                       for i in range(m)]
                ans = max(ans, self.max_sub(arr, k))

        return ans

    def max_sub(self, arr, k) -> int:
        res = -float('inf')
        cur = 0
        prefix = [float('inf')]
        for val in arr:
            bisect.insort(prefix, cur)
            cur += val
            i = bisect.bisect_left(prefix, cur - k)
            res = max(res, cur - prefix[i])

        return res


