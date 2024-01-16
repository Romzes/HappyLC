"""
2981. (Medium) Find Longest Special Substring That Occurs Thrice I
You are given a string s that consists of lowercase English letters.
A string is called special if it is made up of only a single character.
For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.
Return the length of the longest special substring of s which occurs at least thrice,
or -1 if no special substring occurs at least thrice.
A substring is a contiguous non-empty sequence of characters within a string.
Constraints:
  3 <= s.length <= 50
  s consists of only lowercase English letters.
"""

class Solution:
    def maximumLength(self, s: str) -> int:
        res = -2; stat = {}
        for i, c in enumerate(s):
            if i == 0 or c != s[i-1]:  # first
                j = i
                if c not in stat: stat[c] = []
            if i == len(s)-1 or c != s[i+1]:  # last
                lng = i-j+1  # lng >= 1
                for k in range(lng):
                    # length = k+1
                    arr = stat[c]
                    if k == len(arr): arr.append(0)
                    arr[k] += lng-k
        for arr in stat.values():
            for k in range(len(arr)-1, -1, -1):
                if arr[k] >= 3: res = max(res, k)
        return res+1

sln = Solution()
print(sln.maximumLength(s='ababaa'))

sln = Solution()
print(sln.maximumLength(s='aaaa'))

sln = Solution()
print(sln.maximumLength(s='abcdef'))

sln = Solution()
print(sln.maximumLength(s='abcaba'))