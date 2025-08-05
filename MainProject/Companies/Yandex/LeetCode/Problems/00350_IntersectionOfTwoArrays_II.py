from typing import List
from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        # len(nums1) <= len(nums2)
        dict2 = defaultdict(int)  # nums2 {v: cnt}
        for v in nums2: dict2[v] += 1
        res_list = []
        for v in nums1:
            cnt = dict2.get(v)
            if not cnt: continue  # cnt is None or cnt == 0
            res_list.append(v)
            dict2[v] = cnt - 1
        return res_list

sln = Solution()  # Example 1
print(sln.intersect(nums1=[1,2,2,1], nums2=[2,2]))  # Output: [2,2]

sln = Solution()  # Example 2
print(sln.intersect(nums1=[4,9,5], nums2=[9,4,9,8,4]))  # Output: [4,9]
