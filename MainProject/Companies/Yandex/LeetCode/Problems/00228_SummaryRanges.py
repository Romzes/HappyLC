from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res_list = []
        for i, v in enumerate(nums):
            if i == 0 or nums[i-1] < v-1: beg = v
            if i == len(nums)-1 or v+1 < nums[i+1]:
                end = v
                rng = str(beg) if beg == end else f'{beg}->{end}'
                res_list.append(rng)
        return res_list

sln = Solution()  # Example 1
print(sln.summaryRanges(nums=[0,1,2,4,5,7]))  # Output: ["0->2","4->5","7"]

sln = Solution()  # Example 2
print(sln.summaryRanges(nums=[0,2,3,4,6,8,9]))  # Output: ["0","2->4","6","8->9"]
