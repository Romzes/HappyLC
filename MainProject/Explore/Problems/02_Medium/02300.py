# Medium 2300. Successful Pairs of Spells and Potions
# You are given two positive integer arrays spells and potions, of length n and m respectively,
# where spells[i] represents the strength of the i-th spell and potions[j] represents the strength of the j-th potion.
# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the i-th spell.

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        res = len(spells) * [None]
        for i, s in enumerate(spells): res[i] = self.count(potions, p=success/s)
        return res

    def count(self, potions, p):
        if potions[-1] < p: return 0
        if p <= potions[0]: return len(potions)
        j1, j2 = 0, len(potions)-1
        i = j2  # p <= potions[i]
        while j1 <= j2:
            mi = int((j1 + j2) / 2)
            mv = potions[mi]
            if mv < p: j1 = mi+1
            else: j2, i = mi-1, mi
        return len(potions)-i

sln = Solution()
# print(sln.count(potions=[10,20,30,30,40], p=41))
print(sln.successfulPairs(spells=[3,12,4,6,20], potions=[6,1,4,7], success=35))
