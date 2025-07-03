# 408 (Easy) Valid Word Abbreviation
"""
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
The lengths should not have leading zeros.
For example, a string such as "substitution" could be abbreviated as (but not limited to):
    "s10n" ("s ubstitutio n")
    "sub4u4" ("sub stit u tion")
    "12" ("substitution")
    "su3i1u2on" ("su bst i t u ti on")
    "substitution" (no substrings replaced)

The following are not valid abbreviations:
    "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
    "s010n" (has leading zeros)
    "s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
A substring is a contiguous non-empty sequence of characters within a string.

Constraints:
    1 <= word.length <= 20
    word consists of only lowercase English letters.
    1 <= abbr.length <= 10
    abbr consists of lowercase English letters and digits.
    All the integers in abbr will fit in a 32-bit integer.
"""

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 17.78MB  Beats 61.58%
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        j = 0  # word-index
        num_ind = None
        for i, c in enumerate(abbr):
            if not c.isdigit():
                if len(word) <= j or c != word[j]: return False
                j += 1
                continue
            # c = digit
            if i == 0 or not abbr[i-1].isdigit():
                # первая цифра подмассива
                if c == '0': return False  # цифра начинается с 0
                num_ind = i
            if i == len(abbr)-1 or not abbr[i+1].isdigit():
                # последняя цифра подмассива
                j += int(abbr[num_ind:i+1])
        return j == len(word)


sln = Solution()
print(sln.validWordAbbreviation(word='internationalization', abbr='i12iz4n'))  # Output: true
# Explanation: The word 'internationalization' can be abbreviated as 'i12iz4n' ('i nternational iz atio n')

sln = Solution()
print(sln.validWordAbbreviation(word='apple', abbr='a2e'))  # Output: false
# Explanation: The word 'apple' cannot be abbreviated as 'a2e'

sln = Solution()
print(sln.validWordAbbreviation(word='internationalization', abbr='i5a11o1'))  # Output: true

sln = Solution()
print(sln.validWordAbbreviation(word='hi', abbr='1'))  # Output: false


