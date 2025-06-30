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

from typing import List

# Runtime = 3ms  Beats 97.53%  ;  Memory = 18.05 MB  Beats 19.30 %
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res_list = []
        indexes = [0]  # индексы монотонно не убывают
        s = candidates[0]
        while True:
            if s < target:
                indexes.append(indexes[-1])
                s += candidates[indexes[-1]]
                continue
            if s == target:
                # indexes монотонно не убывают => каждая новая комбинация comb будет уникальной в res_list
                comb = [candidates[i] for i in indexes]
                res_list.append(comb)
            # target <= s
            s -= candidates[indexes.pop()]
            while indexes and indexes[-1] == len(candidates)-1:
                # индексы на этих позициях нельзя увеличивать => удаляем их
                s -= candidates[indexes.pop()]
            if not indexes: break
            j = indexes[-1]
            indexes[-1] = j+1
            s = s - candidates[j] + candidates[j+1]
        return res_list


sln = Solution()
print(sln.combinationSum(candidates=[2,3,6,7], target=7))  # Output: [[2,2,3],[7]]
"""
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""

sln = Solution()
print(sln.combinationSum(candidates=[2,3,5], target=8))  # Output: [[2,2,2,2],[2,3,3],[3,5]]

sln = Solution()
print(sln.combinationSum(candidates=[2], target=1))  # Output: []