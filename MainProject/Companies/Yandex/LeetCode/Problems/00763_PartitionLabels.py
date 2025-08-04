from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_indexes = {c: i for i, c in enumerate(s)}
        res_list = []
        j1 = j2 = 0  # [j1; j2] текущая часть
        for i, c in enumerate(s):
            j2 = max(j2, max_indexes[c])
            if i == j2:
                res_list.append(j2-j1+1)
                j1 = j2 = i+1
        return res_list


sln = Solution()  # Example 1
print(sln.partitionLabels(s='ababcbacadefegdehijhklij'))  # Output: [9,7,8]
""" Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
"""

sln = Solution()  # Example 2
print(sln.partitionLabels(s='eccbbbbdec'))  # Output: [10]