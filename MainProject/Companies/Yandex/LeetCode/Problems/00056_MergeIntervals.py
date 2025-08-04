from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda itv: itv[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            a, b = res[-1], intervals[i]
            if b[0] <= a[1]: a[1] = max(a[1], b[1])
            else: res.append(b)
        return res


sln = Solution()  # Example 1
print(sln.merge(intervals=[[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

sln = Solution()  # Example 2
print(sln.merge(intervals=[[1,4],[4,5]]))  # Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
