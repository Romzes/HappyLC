"""
451 (Medium) Sort Characters By Frequency
Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.
Constraints:
  1 <= s.length <= 5 * 10^5
  s consists of uppercase and lowercase English letters and digits.
"""
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(item[1]*item[0] for item in sorted(Counter(s).items(), key=lambda item: item[1], reverse=True))

sln = Solution()
print(sln.frequencySort(s='tree'))

sln = Solution()
print(sln.frequencySort(s='cccaaa'))

sln = Solution()
print(sln.frequencySort(s='Aabb'))

print(8*'a')