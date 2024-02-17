"""
1642 (Medium) Furthest Building You Can Reach
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
While moving from building i to building i+1 (0-indexed),
  If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
  If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
Constraints:
  1 <= heights.length <= 10^5
  1 <= heights[i] <= 10^6
  0 <= bricks <= 10^9
  0 <= ladders <= heights.length
"""
from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        hq = []
        for i in range(1, n):
            # (i-1) дошли
            d = heights[i] - heights[i-1]
            if d <= 0: continue
            if len(hq) < ladders:
                heapq.heappush(hq, d)
            else:
                bricks -= heapq.heappushpop(hq, d)
                if bricks < 0: return i-1
        return n-1

sln = Solution()
print(sln.furthestBuilding(heights=[4,2,7,6,9,14,12], bricks=5, ladders=1))

sln = Solution()
print(sln.furthestBuilding(heights=[4,12,2,7,3,18,20,3,19], bricks=10, ladders=2))

sln = Solution()
print(sln.furthestBuilding(heights=[14,3,19,3], bricks=17, ladders=0))