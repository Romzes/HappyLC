# Medium 2300. Successful Pairs of Spells and Potions
# You are given two positive integer arrays spells and potions, of length n and m respectively,
# where spells[i] represents the strength of the i-th spell and potions[j] represents the strength of the j-th potion.
# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the i-th spell.

# BinSearch
class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        for i, s in enumerate(spells): spells[i] = self.count(potions, min_p=success/s)
        return spells  # spells as result

    def count(self, potions, min_p):
        # potions: asc sorted list[int]
        # return: number of elements potions >= min_p
        if potions[-1] < min_p: return 0
        if min_p <= potions[0]: return len(potions)
        j1, j2 = 0, len(potions)-1
        i = j2  # min index potions[i] >= min_p
        while j1 <= j2:
            mi = int((j1 + j2) / 2)
            mv = potions[mi]
            if mv < min_p: j1 = mi+1
            else: j2, i = mi-1, mi
        return len(potions)-i

class Solution:
    def successfulPairs(self, spells, potions, success):
        res = len(spells) * [0]
        spells2 = [(i, s) for i, s in enumerate(spells)]
        spells2.sort(key=lambda item: -item[1])
        potions.sort()
        pi = 0
        for i, s in spells2:
            min_p = success/s
            while pi < len(potions) and potions[pi] < min_p: pi += 1
            res[i] = len(potions) - pi
            if res[i] == 0: break
        return res

sln = Solution()
# print(sln.count(potions=[10,20,30,30,40], p=41))
print(sln.successfulPairs(spells=[3,12,4,6,20], potions=[6,1,4,7], success=35))
