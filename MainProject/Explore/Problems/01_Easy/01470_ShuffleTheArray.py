# Easy 1470. Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution:
    def shuffle(self, nums, n):
        res = len(nums) * [None]
        for i in range(len(nums)//2):
            res[2*i] = nums[i]; res[2*i+1] = nums[n+i]
        return res

########## TEST ########################################################################################################
sln = Solution()
nums = [1,2,3,4]
print(sln.shuffle(nums, len(nums)//2))