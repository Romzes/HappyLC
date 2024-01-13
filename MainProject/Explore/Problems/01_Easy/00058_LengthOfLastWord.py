"""
58. (Easy) Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
Constraints:
  1 <= s.length <= 10^4
  s consists of only English letters and spaces ' '.
  There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lng = 0; state = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                lng += 1
                state = 1
            elif state == 1:
                break
        return lng

sln = Solution()
print(sln.lengthOfLastWord(s='Hello World'))

sln = Solution()
print(sln.lengthOfLastWord(s='   fly me   to   the moon  '))

sln = Solution()
print(sln.lengthOfLastWord(s='luffy is still joyboy'))