from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}  # {nums-value: nums-index}
        for i, val in enumerate(nums):
            # в index_map все индексы < i
            j = index_map.get(target - val)
            if j is not None: return [j, i]  # j < i
            index_map[val] = i


sln = Solution()  # Example 1
print(sln.twoSum(nums=[2,7,11,15], target=9))  # Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, return [0,1]

sln = Solution()  # Example 2
print(sln.twoSum(nums=[3,2,4], target=6))  # Output: [1,2]

sln = Solution()  # Example 3
print(sln.twoSum(nums=[3,3], target=6))  # Output: [0,1]

