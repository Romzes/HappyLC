"""
205 (Easy) Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
Constraints:
  1 <= s.length <= 5 * 10^4
  t.length == s.length
  s and t consist of any valid ascii character.
"""

# Runtime 30 ms , Beats 98.69% of users with Python3
# Memory 16.76 MB , Beats 76.59% of users with Python3
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}; d2 = {}
        for i in range(len(s)):
            if s[i] not in d1 and t[i] not in d2:
                d1[s[i]] = t[i]
                d2[t[i]] = s[i]
            elif d1.get(s[i]) != t[i] or d2.get(t[i]) != s[i]:
                return False
        return True

# Runtime 36 ms , Beats 89.96% of users with Python3
# Memory 16.71 MB , Beats 76.59% of users with Python3
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_map = {}; t_set = set()
        for i in range(len(s)):
            cs, ct = s[i], t[i]
            if cs not in st_map:
                if ct in t_set: return False
                st_map[cs] = ct
                t_set.add(ct)
            elif st_map[cs] != ct: return False
        return True

sln = Solution()
print(sln.isIsomorphic(s='badc', t='baba'))

sln = Solution()
print(sln.isIsomorphic(s='egg', t='add'))

sln = Solution()
print(sln.isIsomorphic(s='foo', t='bar'))

sln = Solution()
print(sln.isIsomorphic(s='paper', t='title'))