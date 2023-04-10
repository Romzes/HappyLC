# Medium 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Constraints: strs[i] consists of lowercase English letters.

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for s in strs: d[''.join(sorted(s))].append(s)  # sorted(s) return list[char]
        return list(d.values())

sln = Solution()
print(sln.groupAnagrams(strs=['']))

sln = Solution()
print(sln.groupAnagrams(strs=['a']))

sln = Solution()
print(sln.groupAnagrams(strs=['eat','tea','tan','ate','nat','bat']))


