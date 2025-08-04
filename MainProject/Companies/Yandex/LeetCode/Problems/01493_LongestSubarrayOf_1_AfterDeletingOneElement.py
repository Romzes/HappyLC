from typing import List

# two-pointers: !!! SLOW !!! Runtime = 87 ms  Beats 10.52%
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = 0
        cnt0 = 1-nums[0]
        max0 = 1
        res = 0
        while True:
            # инвариант: 0 <= i <= j <= n-1 , cnt0 = кол-во нулей на отрезке nums[i:j]
            if cnt0 <= max0:
                res = max(res, j-i+1-cnt0)
                j += 1
                if j == n: break
                cnt0 += 1-nums[j]
            else:
                # max0 < cnt0
                cnt0 -= 1 - nums[i]
                i += 1  # гарантировано: i <= n-1
        if res == n: res = n-1  # один элемент обязательно должны удалить
        return res

# Runtime = 28 ms  Beats 90.43%  FAST
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        total1 = prev1 = res = 0
        for v in nums:
            # инвариант:  (total1-prev1) 1, 0, prev1 1, nums[i] = v
            if v == 1:
                prev1 += 1
                total1 += 1
                res = max(res, total1)
            else:  # v == 0
                prev1, total1 = 0, prev1
        if res == n: res = n-1  # один элемент обязательно должны удалить
        return res


sln = Solution()  # Example 1
print(sln.longestSubarray(nums=[1,1,0,1]))  # Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

sln = Solution()  # Example 2
print(sln.longestSubarray(nums=[0,1,1,1,0,1,1,0,1]))  # Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

sln = Solution()  # Example 3
print(sln.longestSubarray(nums=[1,1,1]))  # Output: 2
# Explanation: You must delete one element.
