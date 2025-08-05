from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for v in nums: s ^= v
        return s


sln = Solution()  # Example 1
print(sln.singleNumber(nums=[2,2,1]))  # Output: 1

sln = Solution()  # Example 2
print(sln.singleNumber(nums=[4,1,2,1,2]))  # Output: 4

sln = Solution()  # Example 3
print(sln.singleNumber(nums=[1]))  # Output: 1
