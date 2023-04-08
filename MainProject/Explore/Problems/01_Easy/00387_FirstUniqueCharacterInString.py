# Easy 387. First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# s consists of only lowercase English letters.

class Solution:
    def firstUniqChar(self, s):
        lng, stat = len(s), {}
        for i, c in enumerate(s): stat[c] = i if c not in stat else lng
        i = min(stat.values())
        return -1 if i == lng else i

sln = Solution()
print(sln.firstUniqChar(s='leetcode'))

sln = Solution()
print(sln.firstUniqChar(s='loveleetcode'))

sln = Solution()
print(sln.firstUniqChar(s='aabb'))

sln = Solution()
print(sln.firstUniqChar(s='aadadaad'))