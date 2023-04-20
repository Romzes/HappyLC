# Easy 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Constraints:
#   1 <= strs.length <= 200

class Solution:
    def longestCommonPrefix(self, strs):
        min_lng = min(len(s) for s in strs); pref_lng = 0
        for i in range(min_lng):
            eq = True
            for s in strs:
                if s[i] != strs[0][i]:
                    eq = False
                    break
            if eq: pref_lng += 1
            else: break
        return strs[0][0:pref_lng]

sln = Solution()
print(sln.longestCommonPrefix(strs=['flower', 'flow', 'flight']))

sln = Solution()
print(sln.longestCommonPrefix(strs=['dog', 'racecar', 'car']))
