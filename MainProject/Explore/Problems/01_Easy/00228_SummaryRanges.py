"""
228. (Easy) Summary Ranges
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b
Constraints:
  0 <= nums.length <= 20
  -2^31 <= nums[i] <= 2^31 - 1
  All the values of nums are unique.
  nums is sorted in ascending order.
"""

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        # nums.sort()
        ranges = []; i0 = 0; v0 = nums[0]
        for i, v in enumerate(nums):
            if v != v0 + (i - i0):
                ranges.append(self.rng(u1=v0, u2=nums[i-1]))
                i0 = i; v0 = v
        ranges.append(self.rng(u1=v0, u2=nums[-1]))
        return ranges

    def rng(self, u1, u2):
        return f'{u1}->{u2}' if u1 < u2 else str(u1)


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        # nums.sort()
        ranges = []
        for v in nums:
            if ranges and ranges[-1][1] == v-1: ranges[-1][1] = v
            else: ranges.append([v, v])
        for i in range(len(ranges)): ranges[i] = self.rng(u1=ranges[i][0], u2=ranges[i][1])
        return ranges

    def rng(self, u1, u2):
        return f'{u1}->{u2}' if u1 < u2 else str(u1)

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Runtime = 23 ms , Beats 99.51% of users with Python3
        if not nums: return []
        # nums.sort()
        ranges = []
        for i, v in enumerate(nums):
            if i == 0 or v-1 != nums[i-1]: ranges.append([v, v])
            else: ranges[-1][1] = v
        for i, r in enumerate(ranges): ranges[i] = self.rng(u1=r[0], u2=r[1])
        return ranges

    def rng(self, u1, u2):
        return f'{u1}->{u2}' if u1 < u2 else str(u1)


sln = Solution()
print(sln.summaryRanges(nums=[]))

sln = Solution()
print(sln.summaryRanges(nums=[0,1,2,4,5,7]))

sln = Solution()
print(sln.summaryRanges(nums=[0,2,3,4,6,8,9]))