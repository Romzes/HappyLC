# 395 (Medium) Longest Substring with At Least K Repeating Characters
"""
Given a string s and an integer k,
return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
if no such substring exists, return 0.

Constraints:
  1 <= s.length <= 10^4
  s consists of only lowercase English letters.
  1 <= k <= 10^5
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k <= 1: return len(s)
        counter = {}
        buf = len(s) * [0]
        for i in range(len(s), -1, -1):
            c = s[i]
            counter[c] = counter.get(c, 0) + 1
            buf[i] = counter[c]
        

sln = Solution()
print(sln.longestSubstring(s='aaabb', k=3))  # Output: 3

sln = Solution()
print(sln.longestSubstring(s='ababbc', k=2))  # Output: 5

sln = Solution()
print(sln.longestSubstring(s='ababacb', k=3))  # Output: 5

sln = Solution()
print(sln.longestSubstring(s='aaabbb', k=3))  # Output: 6

sln = Solution()
print(sln.longestSubstring(s='bbaaacbd', k=3))  # Output: 3