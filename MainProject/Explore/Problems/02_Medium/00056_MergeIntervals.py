"""
Medium 56. Merge Intervals
Given an array of intervals where intervals[i] = [start[i], end[i]], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
Constraints:
  1 <= intervals.length <= 10^4
  intervals[i].length == 2
  0 <= start[i] <= end[i] <= 10^4
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda itv: itv[0])
        res = []; curr = intervals[0]
        for itv in intervals:
            if itv[0] <= curr[1]: curr[1] = max(curr[1], itv[1])
            else:
                res.append(curr)
                curr = itv
        res.append(curr)
        return res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda itv: itv[0])
        res = [[intervals[0][0], intervals[0][1]]]
        for i in range(1, len(intervals)):
            itv = intervals[i]; last = res[-1]
            if last[0] <= itv[0] <= last[1]: last[1] = max(last[1], itv[1])
            else: res.append([itv[0], itv[1]])
        return res

sln = Solution()
print(sln.merge(intervals=[[1,3],[2,6],[8,10],[15,18]]))

sln = Solution()
print(sln.merge(intervals=[[1,4],[4,5]]))