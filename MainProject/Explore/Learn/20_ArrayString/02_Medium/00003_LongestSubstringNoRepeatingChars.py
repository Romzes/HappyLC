# Medium 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Runtime = 11 ms  Beats 95.34%  ;  Memory = 17.86 MB  Beats 52.94%
class Solution:
    def lengthOfLongestSubstring(self, s):
        res = 0
        prev_ind, prev_chars = 0, {}
        for i, c in enumerate(s):
            c_ind = prev_chars.get(c, -1)
            if prev_ind <= c_ind: prev_ind = c_ind+1
            prev_chars[c] = i
            res = max(res, i - prev_ind + 1)
        return res


sln = Solution()
print(sln.lengthOfLongestSubstring(s='abcabcbb'))  # Output: 3

sln = Solution()
print(sln.lengthOfLongestSubstring(s='bbbbb'))  # Output: 1

sln = Solution()
print(sln.lengthOfLongestSubstring(s='pwwkew'))  # Output: 3


