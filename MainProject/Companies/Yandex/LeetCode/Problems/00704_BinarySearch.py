from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: return m
            if target < nums[m]: r = m-1
            else: l = m+1
        return -1

sln = Solution()  # Example 1
print(sln.search(nums=[-1,0,3,5,9,12], target=9))  # Output: 4
# Explanation: 9 exists in nums and its index is 4

sln = Solution()  # Example 2
print(sln.search(nums=[-1,0,3,5,9,12], target=2))  # Output: -1
# Explanation: 2 does not exist in nums so return -1
