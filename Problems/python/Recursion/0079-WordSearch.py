"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != word[0]:
                    continue
                self.helper(row, col, board, word, ans)
                if 'word' in ans:
                    return True

        return False

    def helper(self, row, col, board, word, ans):
        if board[row][col] != word[0]:
            return
        current = board[row][col]
        board[row][col] = None
        if not word[1:]:
            ans['word'] = True
            return
        neighbors = self.get_neighbors(row, col, board)
        for neighbor in neighbors:
            self.helper(neighbor[0], neighbor[1], board, word[1:], ans)
        board[row][col] = current

    @staticmethod
    def get_neighbors(row, col, board):
        neighbors = []
        if row > 0 and board[row - 1][col] is not None:
            neighbors.append([row - 1, col])
        if row < len(board) - 1 and board[row + 1][col] is not None:
            neighbors.append([row + 1, col])
        if col > 0 and board[row][col - 1] is not None:
            neighbors.append([row, col - 1])
        if col < len(board[row]) - 1 and board[row][col + 1] is not None:
            neighbors.append([row, col + 1])

        return neighbors


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ans = self.dfs(i, j, 0, board, word)
                    if ans:
                        return True
        return False

    def dfs(self, i, j, cur, b, word):
        cur += 1
        if cur == len(word):
            return True
        if b[i][j] == '#':
            return False
        tmp = b[i][j]
        b[i][j] = '#'
        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for step in steps:
            row, col = i + step[0], j + step[1]
            if 0 <= row < len(b) and 0 <= col < len(b[0]) and b[row][col] == word[cur]:
                if self.dfs(row, col, cur, b, word):
                    return True

        b[i][j] = tmp

