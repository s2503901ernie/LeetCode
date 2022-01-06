"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        O(mn) time
        O(1) space
        """
        row_length = len(matrix)
        col_length = len(matrix[0])
        for i in range(row_length):
            for j in range(col_length):
                if matrix[i][j] is None:
                    continue
                elif matrix[i][j] == 0:
                    for row in range(row_length):
                        if matrix[row][j] != 0:
                            matrix[row][j] = None
                    for col in range(col_length):
                        if matrix[i][col] != 0:
                            matrix[i][col] = None
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    matrix[i][j] = 0


    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        O(mn) time
        O(m+n) space
        """
        board = {"row": set(), "col": set()}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    board["row"].add(i)
                    board["col"].add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in board["row"] or j in board["col"]:
                    matrix[i][j] = 0
