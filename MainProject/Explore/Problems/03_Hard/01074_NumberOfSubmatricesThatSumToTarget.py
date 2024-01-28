"""
1074 (Hard) Number of Submatrices That Sum to Target
Given a matrix and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
Constraints:
  1 <= matrix.length <= 100
  1 <= matrix[0].length <= 100
  -1000 <= matrix[i] <= 1000
  -10^8 <= target <= 10^8
"""
from typing import List
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pref = [(n+1)*[0] for _ in range(m+1)]
        for i in range(1, m+1):
            s = 0
            for j in range(1, n+1):
                s += matrix[i-1][j-1]
                pref[i][j] = s + pref[i-1][j]

        res = 0
        for i1 in range(1, m+1):
            for i2 in range(i1, m+1):
                for j1 in range(1, n+1):
                    for j2 in range(j1, n+1):
                        if target == pref[i2][j2] - pref[i1-1][j2] - pref[i2][j1-1] + pref[i1-1][j1-1]:
                            res += 1
        return res

from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if m > n:
            matrix_t = [m*[0] for _ in range(n)]
            for i in range(m):
                for j in range(n): matrix_t[j][i] = matrix[i][j]
            matrix = matrix_t; m, n = n, m

        pref = [(n+1)*[0] for _ in range(m+1)]
        for i in range(1, m+1):
            s = 0
            for j in range(1, n+1):
                s += matrix[i-1][j-1]
                pref[i][j] = s + pref[i-1][j]

        res = 0
        s_arr = (n+1) * [0]
        for i1 in range(1, m+1):
            for i2 in range(i1, m+1):
                s_dict = defaultdict(list)
                for j in range(1, n+1):
                    s_arr[j] = pref[i2][j] - pref[i1-1][j]
                    s_dict[s_arr[j]].append(j)
                for j1 in range(1, n+1):
                    j_indexes = s_dict.get(s_arr[j1-1] + target)
                    if not j_indexes: continue
                    for k in range(len(j_indexes)-1, -1, -1):
                        j2 = j_indexes[k]
                        if j1 <= j2: res += 1
                        else: continue
        return res

sln = Solution()
matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0
print(sln.numSubmatrixSumTarget(matrix, target))

sln = Solution()
matrix = [[1,-1],[-1,1]]
target = 0
print(sln.numSubmatrixSumTarget(matrix, target))

sln = Solution()
matrix = [[904]]
target = 0
print(sln.numSubmatrixSumTarget(matrix, target))