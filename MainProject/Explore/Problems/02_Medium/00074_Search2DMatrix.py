# 74 (Medium) Search a 2D Matrix
"""
You are given an m x n integer matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n) = log(m) + log(n)) time complexity.

Constraints:
  m == matrix.length
  n == matrix[i].length
  1 <= m, n <= 100
  -10^4 <= matrix[i][j], target <= 10^4
"""

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 17.98 MB  Beats 99.09%
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])  # matrix = m-rows X n-cols
        l, r = 0, m*n-1
        while l <= r:
            mid = int((l+r) // 2)
            m_row, m_col = divmod(mid, n)
            v = matrix[m_row][m_col]
            if v == target: return True
            if target < v: r = mid-1
            else: l = mid+1
        return False


sln = Solution()
print(sln.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3))  # Output: true

sln = Solution()
print(sln.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13))  # Output: false