# Medium 1456. Maximum Number of Vowels in a Substring of Given Length
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# Constraints:
#   1 <= s.length <= 105
#   s consists of lowercase English letters.
#   1 <= k <= s.length

class Solution:
    def maxVowels(self, s, k):
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        curr_cnt = 0
        for i in range(k):
            if s[i] in vowels: curr_cnt += 1
        if curr_cnt == k: return k  # optimization
        max_cnt = curr_cnt
        for i in range(k, len(s)):
            if s[i-k] in vowels: curr_cnt -= 1
            if s[i] in vowels: curr_cnt += 1
            max_cnt = max(max_cnt, curr_cnt)
            if max_cnt == k: return k  # optimization
        return max_cnt

sln = Solution()
print(sln.maxVowels(s='abciiidef', k=3))

sln = Solution()
print(sln.maxVowels(s='aeiou', k=2))

sln = Solution()
print(sln.maxVowels(s='leetcode', k=3))