from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # {sorted(s) = string-key: List[str]}
        for s in strs: groups[str(sorted(s))].append(s)
        return [arr for arr in groups.values()]


sln = Solution()  # Example 1
print(sln.groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
""" Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
"""

sln = Solution()  # Example 2
print(sln.groupAnagrams(strs=[""]))  # Output: [[""]]

sln = Solution()  # Example 3
print(sln.groupAnagrams(strs=["a"]))  # Output: [["a"]]