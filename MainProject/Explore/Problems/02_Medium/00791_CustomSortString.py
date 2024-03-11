"""
791. Custom Sort String
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted.
More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.
Constraints:
  1 <= order.length <= 26
  1 <= s.length <= 200
  order and s consist of lowercase English letters.
  All the characters of order are unique.
"""

# Runtime = 43 ms , Beats 8.63 % of users with Python3
# Memory = 16.57 MB , Beats 61.09 % of users with Python3
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ord_map = {}
        arr = len(order) * [None]
        chars = []
        for i, c in enumerate(order):
            ord_map[c] = i
            arr[i] = [0, c]
        for c in s:
            i = ord_map.get(c)
            if i is not None: arr[i][0] += 1
            else: chars.append(c)
        return ''.join(i * c for i, c in arr if i > 0) + ''.join(chars)

# Runtime = 38 ms , Beats 39.07 % of users with Python3
# Memory = 16.45 MB , Beats 91.57 % of users with Python3
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ord_map = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda c: ord_map.get(c, 100)))

# Runtime = 31 ms , Beats 81.50 % of users with Python3
# Memory = 16.44 MB , Beats 91.47 % of users with Python3
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ord_arr = 26 * [100]
        ord_a = ord('a')
        for i, c in enumerate(order): ord_arr[ord(c) - ord_a] = i
        return ''.join(sorted(s, key=lambda c: ord_arr[ord(c) - ord_a]))

sln = Solution()
print(sln.customSortString(order='cba', s='abcd'))

sln = Solution()
print(sln.customSortString(order='bcafg', s='abcd'))