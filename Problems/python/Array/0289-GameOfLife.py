"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.



Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.


Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        transfer = [[False for _ in row] for row in board]
        for i in range(len(board)):
            for j in range(len(board[i])):
                neighbors = self.get_neighbors(i, j, board)
                live = 0
                for neighbor in neighbors:
                    x = neighbor[0]
                    y = neighbor[1]
                    if board[x][y] == 1:
                        live += 1
                if board[i][j] == 1:
                    if live < 2:
                        transfer[i][j] = True
                    if live > 3:
                        transfer[i][j] = True
                else:
                    if live == 3:
                        transfer[i][j] = True
        for i in range(len(board)):
            for j in range(len(board[i])):
                if transfer[i][j] is True:
                    if board[i][j] == 0:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0

    def get_neighbors(self, i, j, board):
        neighbors = []
        final = []
        neighbors.append([i - 1, j - 1])
        neighbors.append([i - 1, j])
        neighbors.append([i - 1, j + 1])
        neighbors.append([i, j - 1])
        neighbors.append([i, j + 1])
        neighbors.append([i + 1, j - 1])
        neighbors.append([i + 1, j])
        neighbors.append([i + 1, j + 1])
        for neighbor in neighbors:
            i = neighbor[0]
            j = neighbor[1]
            if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1:
                continue
            else:
                final.append(neighbor)

        return final
