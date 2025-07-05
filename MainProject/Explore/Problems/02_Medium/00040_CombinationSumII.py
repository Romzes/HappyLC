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

# Runtime = 3ms  Beats 91.46%  ;  Memory = 17.92 MB  Beats 34.99%
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res_list = []
        indexes = [0]  # индексы монотонно возрастают
        s = candidates[0]
        while True:
            if s < target and indexes[-1] < len(candidates)-1:
                indexes.append(indexes[-1] + 1)
                s += candidates[indexes[-1]]
                continue
            if s == target:
                comb = [candidates[i] for i in indexes]
                res_list.append(comb)

            s -= candidates[indexes.pop()]
            while indexes and candidates[indexes[-1]] == candidates[-1]:
                # индексы на этих позициях нельзя увеличивать => удаляем их
                s -= candidates[indexes.pop()]

            if not indexes: break
            j = indexes[-1]
            while candidates[j] == candidates[indexes[-1]]: indexes[-1] += 1
            s = s - candidates[j] + candidates[indexes[-1]]

        return res_list

sln = Solution()
print(sln.combinationSum2(candidates=[10,1,2,7,6,1,5], target=8))
"""
Output: [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
]
"""

sln = Solution()
print(sln.combinationSum2(candidates=[2,5,2,1,2], target=5))
"""
Output: [
    [1,2,2],
    [5]
]
"""

sln = Solution()
candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(sln.combinationSum2(candidates, target=30))
