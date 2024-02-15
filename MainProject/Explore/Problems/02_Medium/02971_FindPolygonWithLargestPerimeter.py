"""
2971 (Medium) Find Polygon With the Largest Perimeter
You are given an array of positive integers nums of length n.
A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.
Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak
where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.
The perimeter of a polygon is the sum of lengths of its sides.
Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.
Constraints:
  3 <= n <= 10^5
  1 <= nums[i] <= 10^9
"""
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_p = -1
        s = nums[0] + nums[1]
        for i in range(2, len(nums)):
            if nums[i] < s: max_p = s + nums[i]
            s += nums[i]
        return max_p

sln = Solution()
print(sln.largestPerimeter(nums=[5,5,5]))

sln = Solution()
print(sln.largestPerimeter(nums=[1,12,1,2,5,50,3]))

sln = Solution()
print(sln.largestPerimeter(nums=[5,5,50]))