from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums - DISTINCT values
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: return m
            if nums[l] <= nums[m]:
                # Условие сравнения <=, а не nums[l] < nums[m] . Чтобы правильно обработать случай nums=[3,1], target=1
                if nums[l] <= target <= nums[m]: return self.search_core(nums, target, l=l, r=m-1)
                l = m+1
            else: # nums[l] > nums[m]
                if nums[m] <= target <= nums[r]: return self.search_core(nums, target, l=m+1, r=r)
                r = m-1
        return -1

    def search_core(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: return m
            if target < nums[m]: r = m-1
            else: l = m+1
        return -1


sln = Solution()  # Example 1
print(sln.search(nums=[4,5,6,7,0,1,2], target=0))  # Output: 4

sln = Solution()  # Example 2
print(sln.search(nums=[4,5,6,7,0,1,2], target=3))  # Output: -1

sln = Solution()  # Example 3
print(sln.search(nums=[1], target=0))  # Output: -1

sln = Solution()  # Example 3
print(sln.search(nums=[3,1], target=1))  # Output: 1
