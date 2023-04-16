# Medium 56. Merge Intervals
# Given an array of intervals where intervals[i] = [start[i], end[i]], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda itv: itv[0])
        res = []; curr = intervals[0]
        for itv in intervals:
            if itv[0] <= curr[1]: curr[1] = max(curr[1], itv[1])
            else:
                res.append(curr)
                curr = itv
        res.append(curr)
        return res

sln = Solution()
print(sln.merge(intervals=[[1,3],[2,6],[8,10],[15,18]]))

sln = Solution()
print(sln.merge(intervals=[[1,4],[4,5]]))