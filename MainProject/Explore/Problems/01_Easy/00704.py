# Easy 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums, target):
        return self.search_range(nums, target, i1=0, i2=len(nums)-1)

    def search_range(self, nums, target, i1, i2):
        if i1 > i2: return -1
        # mi = i1 + int((i2 - i1)/2)
        mi = int((i1 + i2)/2)
        mv = nums[mi]
        if target == mv: return mi
        if target < mv: return self.search_range(nums, target, i1=i1, i2=mi-1)
        if mv < target: return self.search_range(nums, target, i1=mi+1, i2=i2)

class Solution:
    def search(self, nums, target):
        i1, i2 = 0, len(nums)-1
        while i1 <= i2:
            mi = int((i1 + i2) / 2)
            mv = nums[mi]
            if target == mv: return mi
            if target < mv: i2 = mi-1
            else: i1 = mi+1
        return -1

sln = Solution()
print(sln.search(nums=[1,2,3,4,50], target=-10))
