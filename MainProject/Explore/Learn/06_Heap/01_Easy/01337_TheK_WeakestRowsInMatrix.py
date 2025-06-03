"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row.
A row i is weaker than a row j if one of the following is true:
  The number of soldiers in row i is less than the number of soldiers in row j.
  Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Constraints:
  m == mat.length
  n == mat[i].length
  2 <= n, m <= 100
  1 <= k <= m
  matrix[i][j] is either 0 or 1.
"""

from typing import List
import heapq

# Runtime=0 ms  Beats=100.00%  Memory=18.40 MB  Beats=26.83%
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hp = []  # min heap
        mul = 1000
        for i, row in enumerate(mat):
            v = -(mul*row.count(1) + i)
            t = (v, i)
            if len(hp) < k:
                hp.append(t)
                if len(hp) == k: heapq.heapify(hp)
                continue
            if v <= hp[0][0]: continue
            heapq.heappushpop(hp, t)
        hp.sort(key=lambda t: -t[0])
        return [t[1] for t in hp]


# Runtime=0 ms  Beats=100.00%   Memory=18.19 MB  Beats=70.67%
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hp = []  # min heap
        mul = 1000
        for i, row in enumerate(mat):
            v = -(mul*row.count(1) + i)
            if len(hp) < k:
                hp.append(v)
                if len(hp) == k: heapq.heapify(hp)
                continue
            if v <= hp[0]: continue
            heapq.heappushpop(hp, v)
        for i in range(k): hp[i] = -hp[i]
        hp.sort()
        return [v % mul for v in hp]


sln = Solution()
mat = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
]
k = 3
print(sln.kWeakestRows(mat=mat, k=k))  # output = [2,0,3]

sln = Solution()
mat = [
    [1,0,0,0],
    [1,1,1,1],
    [1,0,0,0],
    [1,0,0,0]
]
k = 2
print(sln.kWeakestRows(mat=mat, k=k))  # output = [0,2]