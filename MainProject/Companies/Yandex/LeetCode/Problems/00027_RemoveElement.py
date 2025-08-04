from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for a in nums:
            if a != val:
                nums[k] = a
                k += 1
        return k


sln = Solution()  # Example 1
nums = [3,2,2,3]
print(sln.removeElement(nums, val=3))  # Output: 2
print(nums)

sln = Solution()  # Example 2
nums = [0,1,2,2,3,0,4,2]
print(sln.removeElement(nums, val=2))  # Output: 5
print(nums)
