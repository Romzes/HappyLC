# Easy 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

sln = Solution()
print(sln.intersection(nums1=[1,2,3,4,5], nums2=[3,2,1,1,8]))