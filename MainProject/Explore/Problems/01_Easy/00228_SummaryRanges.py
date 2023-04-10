# Easy 228. Summary Ranges
# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
#     "a->b" if a != b
#     "a" if a == b

class Solution:
    def summaryRanges(self, nums):
        if not nums: return []
        # nums.sort()
        ranges, i0, v0 = [], 0, nums[0]
        for i, v in enumerate(nums):
            if v != v0 + (i - i0):
                ranges.append(self.rng(u1=v0, u2=nums[i-1]))
                i0, v0 = i, v
        ranges.append(self.rng(u1=v0, u2=nums[-1]))
        return ranges

    def rng(self, u1, u2):
        return f'{u1}->{u2}' if u1 < u2 else str(u1)


sln = Solution()
print(sln.summaryRanges(nums=[]))

sln = Solution()
print(sln.summaryRanges(nums=[0,1,2,4,5,7]))

sln = Solution()
print(sln.summaryRanges(nums=[0,2,3,4,6,8,9]))