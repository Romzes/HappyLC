# 223 (Medium) Rectangle Area
"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Constraints:
  -10^4 <= ax1 <= ax2 <= 10^4
  -10^4 <= ay1 <= ay2 <= 10^4
  -10^4 <= bx1 <= bx2 <= 10^4
  -10^4 <= by1 <= by2 <= 10^4
"""

# Runtime = 0ms  Beats 100.00%  ;  Memory = 18.09MB  Beats 17.00%
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        s = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        x1, x2 = max(ax1, bx1), min(ax2, bx2)
        y1, y2 = max(ay1, by1), min(ay2, by2)
        return s - (x2-x1) * (y2-y1) if x1 < x2 and y1 < y2 else s


sln = Solution()
print(sln.computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2))  # Output: 45

sln = Solution()
print(sln.computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2))  # Output: 16