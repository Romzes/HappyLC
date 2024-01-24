"""
581 (Medium) Shortest Unsorted Continuous Subarray
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order,
then the whole array will be sorted in non-decreasing order.
Return the shortest such subarray and output its length.
Follow up: Can you solve it in O(n) time complexity?
Constraints:
  1 <= nums.length <= 10^4
  -10^5 <= nums[i] <= 10^5
"""

from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        i1 = N; i2 = None  # subarray = nums[i1 ; i2]
        stack_stop = False; j = 0  # вершина монотонно неубывающего стека
        max_v = nums[0]
        for i in range(1, N):
            v = nums[i]
            max_v = max(max_v, v)
            if not stack_stop:
                if v > nums[i-1]: j = i
                else: stack_stop
            if max_v <= v: continue
            i2 = i
            if i1 > 0 and nums[j] > v:
                while j >= 0 and nums[j] > v: j -= 1
                i1 = min(i1, j+1)
        return 0 if i2 is None else i2-i1+1



sln = Solution()
print(sln.findUnsortedSubarray(nums=[1, 2, 4, 5, 3]))

sln = Solution()
print(sln.findUnsortedSubarray(nums=[2,6,4,8,10,9,15]))

sln = Solution()
print(sln.findUnsortedSubarray(nums=[1,2,3,4]))

sln = Solution()
print(sln.findUnsortedSubarray(nums=[1]))