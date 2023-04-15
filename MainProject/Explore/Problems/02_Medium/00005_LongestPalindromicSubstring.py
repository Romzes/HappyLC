# Medium 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s):
        max_mi = max_lng = -1
        for mi in range(len(s)):
            lng = self.find_pln_lng(s, i=mi, j=mi)
            if max_lng < lng: max_mi = mi; max_lng = lng
            lng = self.find_pln_lng(s, i=mi, j=mi+1)
            if max_lng < lng: max_mi = mi; max_lng = lng
        half = int(max_lng/2)
        return s[max_mi-half:max_mi+half+1] if max_lng % 2 == 1 else s[max_mi-half+1:max_mi+half+1]

    def find_pln_lng(self, s, i, j):
        lng = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            lng = j - i + 1; i -= 1; j += 1
        return lng

sln = Solution()
print(sln.longestPalindrome(s='a'))

sln = Solution()
print(sln.longestPalindrome(s='bb'))

sln = Solution()
print(sln.longestPalindrome(s='babad'))

sln = Solution()
print(sln.longestPalindrome(s='cbbd'))

sln = Solution()
print(sln.longestPalindrome(s='zabccbaz'))
