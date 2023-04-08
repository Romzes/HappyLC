# Easy 387. First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s):
        stat = {}
        for i, c in enumerate(s):
            if c not in stat: stat[c] = i
            else: stat.pop(c)
        return min(stat.values()) if len(stat) > 0 else -1

sln = Solution()
print(sln.firstUniqChar(s='leetcode'))

sln = Solution()
print(sln.firstUniqChar(s='loveleetcode'))

sln = Solution()
print(sln.firstUniqChar(s='aabb'))