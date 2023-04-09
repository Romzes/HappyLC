# Easy 350. Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1, nums2):
        d1, d2 = {}, {}
        for v in nums1: d1[v] = d1.get(v, 0) + 1
        for v in nums2: d2[v] = d2.get(v, 0) + 1
        res = []
        for v, c1 in d1.items():
            c2 = d2.get(v)
            if c2: res.extend(min(c1, c2)*[v])
        return res

sln = Solution()
print(sln.intersect(nums1=[1,2,2,1], nums2=[2,2]))

sln = Solution()
print(sln.intersect(nums1=[4,9,5], nums2=[9,4,9,8,4]))
