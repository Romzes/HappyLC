# Medium 2405. Optimal Partition of String
# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
# Return the minimum number of substrings in such a partition.
# Note that each character should belong to exactly one substring in a partition.
# Constraints: s consists of only English lowercase letters.

class Solution:
    def partitionString(self, s):
        cnt, chars = 1, set()
        for c in s:
            if c in chars:
                chars.clear()
                cnt += 1
            chars.add(c)
        return cnt

sln = Solution()
print(sln.partitionString(s='aaabcc'))