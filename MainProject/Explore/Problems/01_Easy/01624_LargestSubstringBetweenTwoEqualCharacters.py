# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters.
# If there is no such substring return -1.
# A substring is a contiguous sequence of characters within a string.
# Constraints:
#   1 <= s.length <= 300
#   s contains only lowercase English letters.


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos = {}
        mx = 0
        for i, c in enumerate(s):
            i0 = pos.get(c)
            if i0 is None: pos[c] = i
            else: mx = max(mx, i-i0)
        return mx-1

import string
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos = {c: -1 for c in string.ascii_lowercase}
        mx = 0
        for i, c in enumerate(s):
            i0 = pos[c]
            if i0 == -1: pos[c] = i
            else: mx = max(mx, i-i0)
        return mx-1

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos = 26*[-1]; mx = 0
        for i, c in enumerate(s):
            ci = ord(c) - ord('a'); i0 = pos[ci]
            if i0 == -1: pos[ci] = i
            else: mx = max(mx, i-i0)
        return mx-1

sln = Solution()
print(sln.maxLengthBetweenEqualCharacters(s='aa'))

sln = Solution()
print(sln.maxLengthBetweenEqualCharacters(s='abca'))

sln = Solution()
print(sln.maxLengthBetweenEqualCharacters(s='cbzxy'))

# print(ord('c')-ord('a'))
# print(len(string.ascii_lowercase))