"""
356 (Medium) Line Reflection
Given n points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.
In other words, answer whether or not if there exists a line that after reflecting all points over the given line,
the original points' set is the same as the reflected ones.
Note that there can be repeated points.
Constraints:
  n == points.length
  1 <= n <= 10^4
  -10^8 <= points[i][j] <= 10^8
"""
from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        d = {}
        for p in points:
            k = (p[0], p[1])
            if k not in d: d[k] = 1
        x0 = sum(k[0] for k in d) / len(d)
        for k1 in d:
            if k1[0] == x0 or d[k1] == 0: continue
            k2 = (2*x0-k1[0], k1[1])
            cnt2 = d.get(k2)
            if cnt2 is None: return False
            d[k1] -= 1
            d[k2] -= 1
        for k, cnt in d.items():
            if cnt != 0 and k[0] != x0: return False
        return True

sln = Solution()
points = [[1,1],[-1,1]]
print(sln.isReflected(points))

sln = Solution()
points = [[1,1],[-1,-1]]
print(sln.isReflected(points))
