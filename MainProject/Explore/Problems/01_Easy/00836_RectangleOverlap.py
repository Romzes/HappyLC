# 836 (Easy) Rectangle Overlap
"""
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2],
where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner.
Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive.
To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
"""

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 17.78 MB  Beats 48.97%
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        b = (rec1[2] <= rec2[0]) or (rec2[2] <= rec1[0]) or (rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
        return not b


sln = Solution()
print(sln.isRectangleOverlap(rec1=[0,0,2,2], rec2=[1,1,3,3]))  # Output: true

sln = Solution()
print(sln.isRectangleOverlap(rec1=[0,0,1,1], rec2=[1,0,2,1]))  # Output: false

sln = Solution()
print(sln.isRectangleOverlap(rec1=[0,0,1,1], rec2=[2,2,3,3]))  # Output: false