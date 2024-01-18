"""
986. (Medium) Interval List Intersections
You are given two lists of closed intervals, firstList and secondList,
where firstList[i] = [start_i, end_i] and secondList[j] = [start_j, end_j].
Each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3].
Constraints:
  0 <= firstList.length, secondList.length <= 1000
  firstList.length + secondList.length >= 1
  0 <= start_i < end_i <= 10^9 , end_i < start_i+1
  0 <= start_j < end_j <= 10^9 , end_j < start_j+1
"""
from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        n1 = len(firstList); n2 = len(secondList); i = j = 0
        while i < n1 and j < n2:
            seg1 = firstList[i]; seg2 = secondList[j]
            a = max(seg1[0], seg2[0]); b = min(seg1[1], seg2[1])
            if a <= b: res.append([a, b])
            if seg1[1] <= seg2[1]: i += 1
            else: j += 1
        return res

sln = Solution()
print(sln.intervalIntersection(firstList=[[0,2],[5,10],[13,23],[24,25]], secondList=[[1,5],[8,12],[15,24],[25,26]]))

sln = Solution()
print(sln.intervalIntersection(firstList=[[1,3],[5,9]], secondList=[]))