from typing import List

# Runtime = 349 ms  Beats 98.51%  ;  Memory = 20.66 MB  Beats 69.42%
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_list = []
        nums.sort()
        n = len(nums)  # n >= 3
        # ищем тройки (i, j, k): 0 <= i < j < k <= n-1
        for i in range(n-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue  # чтобы НЕ было повторений
            trg = -nums[i]
            j, k = i+1, n-1
            while j < k:
                s = nums[j] + nums[k]
                if s < trg: j += 1
                elif s > trg: k -= 1
                else:
                    arr = [nums[i], nums[j], nums[k]]
                    if len(res_list) == 0 or arr != res_list[-1]:
                        res_list.append(arr)  # чтобы НЕ было повторений
                    j += 1
                    k -= 1
        return res_list


sln = Solution()  # Example 1
print(sln.threeSum(nums=[-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]
# Explanation:  The distinct triplets are [-1,0,1] and [-1,-1,2]. Notice that the order of the output and the order of the triplets does not matter.

sln = Solution()  # Example 2
print(sln.threeSum(nums=[0,1,1]))  # Output: []
# Explanation: The only possible triplet does not sum up to 0.

sln = Solution()  # Example 3
print(sln.threeSum(nums=[0,0,0]))  # Output: [[0,0,0]]

sln = Solution()
print(sln.threeSum(nums=[-4,-1,-1,0,1,2]))  # Output: [[-1,-1,2],[-1,0,1]]
