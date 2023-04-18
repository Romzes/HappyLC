class Solution:
    def mergeAlternately(self, word1, word2):
        l1 = len(word1); l2 = len(word2); mrg = []
        for i in range(min(l1, l2)): mrg.append(word1[i]); mrg.append(word2[i])
        if l1 < l2:
            for i in range(l1, l2): mrg.append(word2[i])
        if l2 < l1:
            for i in range(l2, l1): mrg.append(word1[i])
        return ''.join(mrg)

class Solution:
    def mergeAlternately(self, word1, word2):
        l1 = len(word1); l2 = len(word2); mrg = (l1 + l2)*[None]; j = 0
        for i in range(min(l1, l2)): mrg[j]= word1[i]; mrg[j+1] = word2[i]; j += 2
        if l1 < l2:
            for i in range(l1, l2): mrg[j] = word2[i]; j += 1
        if l2 < l1:
            for i in range(l2, l1): mrg[j] = word1[i]; j += 1
        return ''.join(mrg)

sln = Solution()
print(sln.mergeAlternately(word1='abc', word2='pqr'))

sln = Solution()
print(sln.mergeAlternately(word1='ab', word2='pqrs'))

sln = Solution()
print(sln.mergeAlternately(word1='abcd', word2='pq'))