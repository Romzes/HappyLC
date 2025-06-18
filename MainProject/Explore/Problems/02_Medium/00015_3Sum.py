# 15 (Medium) 3Sum
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Constraints:
  3 <= nums.length <= 3000
  -10^5 <= nums[i] <= 10^5
"""

from typing import List

# Runtime = 2390 ms  Beats 5.01%  ;  Memory = 19.88 MB  Beats 99.82%
# !!! Runtime = O(n^2)  ;  Memory = O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        min_indexes = {}
        for i, a in enumerate(nums):
            if a not in min_indexes: min_indexes[a] = i

        res = set()
        # 0 <= i < j < k <= n-1
        for j in range(1, n-1):
            for k in range(j+1, n):
                a = -(nums[j] + nums[k])
                i = min_indexes.get(a)
                if i is None or i >= j: continue
                elem = (nums[i], nums[j], nums[k])
                if elem in res: continue
                res.add(elem)
        return list(res)


sln = Solution()
print(sln.threeSum(nums=[-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]

sln = Solution()
print(sln.threeSum(nums=[0,1,1]))  # Output: []

sln = Solution()
print(sln.threeSum(nums=[0,0,0]))  # Output: [[0,0,0]]