# 40 (Medium) Combination Sum II
"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Constraints:
  1 <= candidates.length <= 30
  2 <= candidates[i] <= 40
  All elements of candidates are distinct.
  1 <= target <= 40
"""

from typing import List

# без рекурсии - быстрее
# Runtime = 3ms  Beats 91.46%  ;  Memory = 17.92 MB  Beats 34.99%
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res_list = []
        indexes = [0]  # indexes = [i_1 < i_2 < ... < i_k] чтобы все комбинации были уникальными
        s = candidates[0]
        while True:
            if s < target and indexes[-1] < len(candidates)-1:
                indexes.append(indexes[-1] + 1)
                s += candidates[indexes[-1]]
                continue

            if s == target:
                res_list.append([candidates[i] for i in indexes])  # добавляется очередная комбинация

            # target <= s, candidates отсортированы => indexes[-1] не увеличиваем, а делаем шаги назад - backtracking
            s -= candidates[indexes.pop()]
            while indexes and candidates[indexes[-1]] == candidates[-1]:
                s -= candidates[indexes.pop()]  # индексы на этих позициях нельзя увеличивать => удаляем их

            if not indexes: break  # больше нельзя делать шаг назад => выходим

            j = indexes[-1]
            while candidates[j] == candidates[indexes[-1]]: indexes[-1] += 1  # чтобы все комбинации были уникальными
            s = s - candidates[j] + candidates[indexes[-1]]

        return res_list


# есть рекурсия - проще код, есть оптимизации, сортируется массив candidates, уменьшается кол-во рекурсивных вызовов
# Runtime = 3 ms  Beats 91.46%  ;  Memory = 17.74 MB  Beats 83.19%
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.comb = []  # comb = [candidates[i_1], ... candidates[i_k]], где i_1 < i_2 < ... < i_k чтобы все комбинации были уникальными
        self.res_list = []
        self.backtrack(start_ind=0, rest=target)
        return self.res_list

    def backtrack(self, start_ind, rest):
        # start_ind = index of candidates ; rest остаток суммы до target
        if rest == 0:
            self.res_list.append(self.comb[::])  # добавляется очередная комбинация
            return
        for i in range(start_ind, len(self.candidates)):
            c = self.candidates[i]
            if start_ind < i and c == self.candidates[i-1]:
                continue  # чтобы все комбинации были уникальными. важно, что candidates отсортированы.
            next_rest = rest - c
            if next_rest < 0: return  # candidates отсортированы => выход из цикла
            self.comb.append(c)
            self.backtrack(start_ind=i+1, rest=next_rest)
            self.comb.pop()


sln = Solution()
print(sln.combinationSum2(candidates=[10,1,2,7,6,1,5], target=8))  # Output: [ [1,1,6] , [1,2,5] , [1,7], [2,6] ]

sln = Solution()
print(sln.combinationSum2(candidates=[2,5,2,1,2], target=5))  # Output: [ [1,2,2] , [5] ]

sln = Solution()
candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(sln.combinationSum2(candidates, target=30))