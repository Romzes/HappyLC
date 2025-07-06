# 39 (Medium) Combination Sum
"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Constraints:
  1 <= candidates.length <= 30
  2 <= candidates[i] <= 40
  All elements of candidates are distinct.
  1 <= target <= 40
"""

""" A general approach to backtracking questions in Java (Subsets, Permutations, Combination Sum, Palindrome)
https://leetcode.com/problems/combination-sum/solutions/16502/a-general-approach-to-backtracking-quest-dexx/
Problem   78  https://leetcode.com/problems/subsets/
Problem   90  https://leetcode.com/problems/subsets-ii/
Problem   46  https://leetcode.com/problems/permutations/
Problem   47  https://leetcode.com/problems/permutations-ii/
Problem   39  https://leetcode.com/problems/combination-sum/
Problem   40  https://leetcode.com/problems/combination-sum-ii/
Problem  131  https://leetcode.com/problems/palindrome-partitioning/
"""

from typing import List

# без рекурсии - самый быстрый !!!
# Runtime = 0 ms  Beats 100.00%  ;  Memory = 17.66 MB  Beats 98.05%
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res_list = []
        indexes = [0]  # indexes = [i_1 <= i_2 <= ... <= i_k] чтобы все комбинации были уникальными
        s = candidates[0]
        while True:
            if s < target:
                indexes.append(indexes[-1])
                s += candidates[indexes[-1]]
                continue

            if s == target:
                res_list.append([candidates[i] for i in indexes])  # добавляется очередная комбинация

            # target <= s, candidates отсортированы => indexes[-1] не увеличиваем, а делаем шаги назад - backtracking
            s -= candidates[indexes.pop()]
            while indexes and indexes[-1] == len(candidates)-1:
                s -= candidates[indexes.pop()]  # индексы на этих позициях нельзя увеличивать => удаляем их

            if not indexes: break  # больше нельзя делать шаг назад => выходим

            j = indexes[-1]
            indexes[-1] += 1
            s = s - candidates[j] + candidates[indexes[-1]]

        return res_list


# есть рекурсия - самый простой код, без оптимизации, даже НЕ сортируется массив candidates
# не все backtracking-задачи можно оптимизировать, иногда полезным и наглядным является самый простой вариант
# Runtime = 11 ms  Beats 58.34%  ;  Memory = 17.77 MB  Beats 87.29%
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.comb = []  # comb = [candidates[i_1], ... candidates[i_k]], где i_1 <= i_2 <= ... <= i_k чтобы все комбинации были уникальными
        self.res_list = []
        self.backtrack(start_ind=0, rest=target)
        return self.res_list

    def backtrack(self, start_ind, rest):
        # start_ind = index of candidates ; rest остаток суммы до target
        if rest < 0: return
        if rest == 0:
            self.res_list.append(self.comb[::])  # добавляется очередная комбинация
            return
        for i in range(start_ind, len(self.candidates)):
            self.comb.append(self.candidates[i])
            self.backtrack(start_ind=i, rest=rest-self.candidates[i])
            self.comb.pop()


# есть рекурсия - проще код, есть оптимизации, сортируется массив candidates, уменьшается кол-во рекурсивных вызовов
# Runtime = 3 ms  Beats 97.56%  ;  Memory = 17.63 MB  Beats 98.05%
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.comb = []  # comb = [candidates[i_1], ... candidates[i_k]], где i_1 <= i_2 <= ... <= i_k чтобы все комбинации были уникальными
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
            next_rest = rest - c
            if next_rest < 0: return  # candidates отсортированы => выход из цикла
            self.comb.append(c)
            self.backtrack(start_ind=i, rest=next_rest)
            self.comb.pop()


sln = Solution()
print(sln.combinationSum(candidates=[2,3,6,7], target=7))  # Output: [ [2,2,3] , [7] ]
"""
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""

sln = Solution()
print(sln.combinationSum(candidates=[2,3,5], target=8))  # Output: [ [2,2,2,2] , [2,3,3] , [3,5] ]

sln = Solution()
print(sln.combinationSum(candidates=[2], target=1))  # Output: []