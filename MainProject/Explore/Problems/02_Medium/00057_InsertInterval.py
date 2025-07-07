# 57 (Medium) Insert Interval
"""
You are given an array of non-overlapping intervals intervals
where intervals[i] = [start[i], end[i]] represent the start and the end of the i-th interval and intervals is sorted in ascending order by start[i].
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start[i]
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.

Constraints:
  0 <= intervals.length <= 10^4
  intervals[i].length == 2
  0 <= start[i] <= end[i] <= 10^5
  intervals is sorted by start[i] in ascending order.
  newInterval.length == 2
  0 <= start <= end <= 10^5
"""

from typing import List

# бинарный поиск интервала - сложный код !!!
# Runtime = 0ms  Beats 100.00%  ;  Memory = 19.61MB  Beats 60.39%
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        res1 = Solution.find_interval(newInterval, k=0, intervals=intervals)
        if res1['intersects']:
            res2 = Solution.find_interval(newInterval, k=1, intervals=intervals, l=res1['ind'])
            arr = intervals[0:res1['ind']]
            ins_itv = [
                min(newInterval[0], intervals[res1['ind']][0]),
                max(newInterval[1], intervals[res2['ind']][1])
            ]
            arr.append(ins_itv)
            arr.extend(intervals[res2['ind']+1:])
            return arr

        arr = intervals[0:res1['ind']]
        arr.append(newInterval)
        arr.extend(intervals[res1['ind']:])
        return arr


    @staticmethod
    def find_interval(itv, k, intervals, l=0, r=None):
        if r is None: r = len(intervals)-1
        j = None
        while l <= r:
            m = (l + r) // 2
            mid_itv = intervals[m]
            if mid_itv[0] <= itv[k] <= mid_itv[1]: return dict(intersects=True, ind=m)
            if Solution.is_intersects(mid_itv, itv): j = m
            if itv[k] < mid_itv[0]: r = m-1
            else: l = m+1  # mid_itv[1] < itv[k]
        # r = l-1
        if j is not None: return dict(intersects=True, ind=j)
        return dict(intersects=False, ind=l)

    @staticmethod
    def is_intersects(itv1, itv2):
        return not(itv2[1] < itv1[0] or itv1[1] < itv2[0])

# красивое решение :)
# Runtime = 0ms  Beats 100.00%  ;  Memory = 19.61MB  Beats 60.39%
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        res_list = []
        for i, itv in enumerate(intervals):
            cmp = Solution.compare(newInterval, itv)
            if cmp == 1:
                res_list.append(itv)  # itv < newInterval
                continue
            if cmp == 0:
                newInterval[0], newInterval[1] = min(newInterval[0], itv[0]), max(newInterval[1], itv[1])
                continue
            if cmp == -1:
                # newInterval < itv
                res_list.append(newInterval)
                res_list.extend(intervals[i:])
                return res_list
        res_list.append(newInterval)
        return res_list


    @staticmethod
    def compare(itv1, itv2):
        if itv1[1] < itv2[0]: return -1  # itv1 < itv2
        if itv2[1] < itv1[0]: return 1  # itv2 < itv1
        return 0  # itv1 intersects with itv2


sln = Solution()
print(sln.insert(intervals=[[1,3],[6,9]], newInterval=[2,5]))  # Output: [[1,5],[6,9]]

sln = Solution()
print(sln.insert(intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval=[4,8]))  # Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
