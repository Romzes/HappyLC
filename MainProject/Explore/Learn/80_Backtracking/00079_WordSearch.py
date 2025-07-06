# 79 (Medium) Word Search
"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Constraints:
  m == board.length
  n = board[i].length
  1 <= m, n <= 6
  1 <= word.length <= 15
  board and word consists of only lowercase and uppercase English letters.
"""

from typing import List

# Runtime = 5610ms  Beats 17.60%  ;  Memory = 17.86MB  Beats 64.69%
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board
        self.M, self.N = len(board), len(board[0])
        self.cell_path = set()
        for r in range(self.M):
            for c in range(self.N):
                self.cell_path.clear()
                if self.find_word(r, c, w_ind=0): return True
        return False

    def find_word(self, r, c, w_ind):
        if r < 0 or self.M <= r or c < 0 or self.N <= c: return False
        if self.board[r][c] != self.word[w_ind]: return False
        cell = (r, c)
        if cell in self.cell_path: return False
        if w_ind == len(self.word) - 1: return True
        self.cell_path.add(cell)
        for r2, c2 in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if self.find_word(r=r2, c=c2, w_ind=w_ind+1): return True
        self.cell_path.remove(cell)
        return False


sln = Solution()
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
print(sln.exist(board, word='ABCCED'))  # Output: true

sln = Solution()
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
print(sln.exist(board, word='SEE'))  # Output: true

sln = Solution()
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
print(sln.exist(board, word='ABCB'))  # Output: false