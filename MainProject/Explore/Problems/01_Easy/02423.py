# Easy 2423. Remove Letter To Equalize Frequency
# You are given a 0-indexed string word, consisting of lowercase English letters.
# You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.
# Note:
#     The frequency of a letter x is the number of times it occurs in the string.
#     You must remove exactly one letter and cannot chose to do nothing.

from collections import Counter

class Solution:
    def equalFrequency(self, word):
        if word is None or len(word) == 0: return False
        cnt1 = Counter(word)
        if len(cnt1) in (1, len(word)): return True  # word из одной буквы или все буквы по одному разу
        cnt2 = Counter(cnt1.values())
        if len(cnt2) == 1 or len(cnt2) > 2: return False
        numbers = list(cnt2.keys())
        mn, mx = min(numbers), max(numbers)
        return (mn == 1 and cnt2[mn] == 1) or (mx == mn+1 and cnt2[mx] == 1)

########## TEST ########################################################################################################
sln = Solution()
print(sln.equalFrequency('word'))
