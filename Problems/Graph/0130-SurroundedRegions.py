"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:

Input: board = [["X"]]
Output: [["X"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""


class Solution:
    def solve1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        # BFS
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            self.bfs(i, 0, board)
            self.bfs(i, n - 1, board)
        for j in range(n):
            self.bfs(0, j, board)
            self.bfs(m - 1, j, board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def bfs(self, row, col, board):
        queue = [[row, col]]
        while queue:
            current = queue.pop(0)
            row, col = current[0], current[1]
            if board[row][col] == 'X' or board[row][col] == 'A':
                continue
            board[row][col] = 'A'
            neighbors = self.get_neighbors(row, col, board)
            for neighbor in neighbors:
                queue.append(neighbor)

    def get_neighbors(self, row, col, board):
        neighbors = []
        if row > 0 and board[row - 1][col] == 'O':
            neighbors.append([row - 1, col])
        if col > 0 and board[row][col - 1] == 'O':
            neighbors.append([row, col - 1])
        if row < len(board) - 1 and board[row + 1][col] == 'O':
            neighbors.append([row + 1, col])
        if col < len(board[row]) - 1 and board[row][col + 1] == 'O':
            neighbors.append([row, col + 1])

        return neighbors

    def solve2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        # DFS
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            self.dfs(i, 0, board)
            self.dfs(i, n - 1, board)
        for j in range(n):
            self.dfs(0, j, board)
            self.dfs(m - 1, j, board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def dfs(self, row, col, board):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[row]) or board[row][col] != 'O':
            return

        board[row][col] = 'A'
        self.dfs(row - 1, col, board)
        self.dfs(row + 1, col, board)
        self.dfs(row, col - 1, board)
        self.dfs(row, col + 1, board)
