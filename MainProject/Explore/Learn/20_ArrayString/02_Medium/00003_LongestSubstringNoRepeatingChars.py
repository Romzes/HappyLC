# Medium 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s):
        chars = {}; i1 = mx = 0
        for i, c in enumerate(s):
            ci = chars.get(c, -1)
            if ci >= i1: i1 = ci+1
            chars[c] = i
            mx = max(mx, i - i1 + 1)
        return mx

sln = Solution()
print(sln.lengthOfLongestSubstring(s='abcabcbb'))

sln = Solution()
print(sln.lengthOfLongestSubstring(s='bbbbb'))

sln = Solution()
print(sln.lengthOfLongestSubstring(s='pwwkew'))


