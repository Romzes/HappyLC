"""
1750 (Medium) Minimum Length of String After Deleting Similar Ends
Given a string s consisting only of characters 'a', 'b', and 'c'.
You are asked to apply the following algorithm on the string any number of times:
  Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
  Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
  The prefix and the suffix should not intersect at any index.
  The characters from the prefix and suffix must be the same.
  Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).
Constraints:
  1 <= s.length <= 10^5
  s only consists of characters 'a', 'b', and 'c'.
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s)-1
        while i < j and s[i] == s[j]:
            c = s[i]
            while i <= j and s[i] == c: i += 1
            while i <= j and s[j] == c: j -= 1
        return max(j-i+1, 0)

sln = Solution()
print(sln.minimumLength(s='ca'))

sln = Solution()
print(sln.minimumLength(s='cabaabac'))

sln = Solution()
print(sln.minimumLength(s='aabccabba'))