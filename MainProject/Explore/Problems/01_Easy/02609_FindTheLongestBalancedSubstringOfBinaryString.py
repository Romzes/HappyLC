# 2609. Find the Longest Balanced Substring of a Binary String
"""
You are given a binary string s consisting only of zeroes and ones.
A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring.
Notice that the empty substring is considered a balanced substring.
Return the length of the longest balanced substring of s.
A substring is a contiguous sequence of characters within a string.

Constraints:
  1 <= s.length <= 50
  '0' <= s[i] <= '1'
"""

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        longest = 0
        counts = {'0': 0, '1': 0}
        for i, c in enumerate(s):
            counts[c] = 1 if i == 0 or s[i-1] != c else counts[c] + 1
            if c == '1':
                if counts['1'] <= counts['0']: longest = max(longest, 2*counts['1'])
        return longest

# Runtime = 2 ms  Beats 76.11%  ;  Memory = 17.90 MB  Beats 28.33%
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        longest = cnt0 = cnt1 = 0
        for i, c in enumerate(s):
            if c == '0':
                if i == 0 or s[i-1] == '1': cnt0, cnt1 = 1, 0
                else: cnt0 += 1
                continue
            # c = '1'
            cnt1 += 1
            if cnt1 <= cnt0: longest = max(longest, 2*cnt1)

        return longest


sln = Solution()
print(sln.findTheLongestBalancedSubstring(s='01000111'))  # Output: 6

sln = Solution()
print(sln.findTheLongestBalancedSubstring(s='00111'))  # Output: 4

sln = Solution()
print(sln.findTheLongestBalancedSubstring(s='111'))  # Output: 0

