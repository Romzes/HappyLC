"""
289. (Medium) Game of Life
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
  Any live cell with fewer than two live neighbors dies as if caused by under-population.
  Any live cell with two or three live neighbors lives on to the next generation.
  Any live cell with more than three live neighbors dies, as if by over-population.
  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
Given the current state of the m x n grid board, return the next state.
Follow up:
  Could you solve it in-place?
  Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
  In this question, we represent the board using a 2D array.
  In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border).
  How would you address these problems?
Constraints:
  m == board.length
  n == board[i].length
  1 <= m, n <= 25
  board[i][j] is 0 or 1.
"""

from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board); n = len(board[0])
        vectors = (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)
        for i in range(m):
            for j in range(n):
                b = board[i][j]; cnt1 = 0
                for v in vectors:
                    i1, j1 = i+v[0], j+v[1]
                    if not (0 <= i1 < m) or not (0 <= j1 < n): continue
                    if board[i1][j1] & 1 == 1: cnt1 += 1
                if (b == 1 and 2 <= cnt1 <= 3) or (b == 0 and cnt1 == 3):
                    board[i][j] = 2 | b  # 1=0b01 -> 3=0b11 , 0=0b00 -> 2=0b10
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

sln = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sln.gameOfLife(board)
print(board)

sln = Solution()
board = [[1,1],[1,0]]
sln.gameOfLife(board)
print(board)