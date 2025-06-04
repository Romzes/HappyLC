# 973 (Medium) K Closest Points to Origin
"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Constraints:
  1 <= k <= points.length <= 10^4
  -10^4 <= xi, yi <= 10^4
"""

from typing import List
import heapq

# Runtime=48 ms  Beats=89.94%  Memory=22.43 MB  Beats=69.37%
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []  # min-heap
        for i, p in enumerate(points):
            d = -(p[0]**2 + p[1]**2)
            t = (d, i)
            if len(hp) < k:
                hp.append(t)
                if len(hp) == k: heapq.heapify(hp)
                continue
            if d <= hp[0][0]: continue
            heapq.heappushpop(hp, t)
        return [points[t[1]] for t in hp]


sln = Solution()
points = [[1,3],[-2,2]]
print(sln.kClosest(points=points, k=1))  # output: [[-2,2]]

sln = Solution()
points = [[3,3],[5,-1],[-2,4]]
print(sln.kClosest(points=points, k=2))  # output: [[3,3],[-2,4]]