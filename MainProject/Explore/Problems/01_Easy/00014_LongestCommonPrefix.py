# Easy 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Constraints:
#   1 <= strs.length <= 200

class Solution:
    def longestCommonPrefix(self, strs):
        i = -1; work = True
        while work:
            i += 1
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    work = False
                    break
        return strs[0][0:i]

class Solution:
    def longestCommonPrefix(self, strs):
        min_lng = min(len(s) for s in strs)
        for i in range(min_lng):
            for s in strs:
                if s[i] != strs[0][i]: return s[0:i]
        return strs[0][0:min_lng]

sln = Solution()
print(sln.longestCommonPrefix(strs=['flower', 'flow', 'flight']))

sln = Solution()
print(sln.longestCommonPrefix(strs=['dog', 'racecar', 'car']))
