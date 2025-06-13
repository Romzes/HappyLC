# 340 (Medium) Longest Substring with At Most K Distinct Characters
"""
Given a string s and an integer k, return the length of the longest of s that contains at most k distinct characters.

Constraints:
  1 <= s.length <= 5 * 10^4
  0 <= k <= 50
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        j, res = 0, 1
        last = {s[0]: 0}  # last-index
        for i in range(1, len(s)):
            # s[j,..,i-1] содержит <= k уникальных символов
            last[s[i]] = i
            while len(last) > k:
                # last[s[i]] = k+1 => j нужно сдвинуть вправо так, чтобы на отрезке s[j,..,i] стало ровно k уникальных символов
                if j == last[s[j]]: last.pop(s[j])
                j += 1
            res = max(res, i - j + 1)
        return res

sln = Solution()
print(sln.lengthOfLongestSubstringKDistinct(s='a', k=1))  # Output: 1

sln = Solution()
print(sln.lengthOfLongestSubstringKDistinct(s='eceba', k=2))  # Output: 3

sln = Solution()
print(sln.lengthOfLongestSubstringKDistinct(s='aa', k=1))  # Output: 2