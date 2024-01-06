"""
1235. (Hard) Maximum Profit in Job Scheduling
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
You're given the startTime, endTime and profit arrays,
return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
If you choose a job that ends at time X you will be able to start another job that starts at time X.
Constraints:
  1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
  1 <= startTime[i] < endTime[i] <= 10^9
  1 <= profit[i] <= 10^4
"""

import bisect
class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda tpl: tpl[1])  # = list[tuple]
        # print(jobs)
        profit = []  # [[end_time, max_profit]] max_profit для всех заданий, у которых время завершения <= endTime
        for tpl in jobs:
            if len(profit) == 0 or profit[-1][0] < tpl[1]: profit.append([tpl[1], 0])
        for tpl in jobs:
            i = bisect.bisect_left(profit, tpl[0], key=lambda t: t[0])
            if profit[i][0] == tpl[0]: p = profit[i][1] + tpl[2]
            elif i == 0: p = tpl[2]
            else: p = profit[i-1][1] + tpl[2]
            k = bisect.bisect_left(profit, tpl[1], key=lambda t: t[0])
            if k > 0: p = max(p, profit[k-1][1])
            profit[k][1] = max(profit[k][1], p)
        return profit[-1][1]

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda tpl: tpl[1])  # = list[tuple]
        # print(jobs)
        end_times = [tpl[1] for tpl in jobs]  # asc sorted
        profit = len(end_times) * [0]  # profit[i] <= profit[i+1]
        profit[0] = jobs[0][2]
        for i in range(1, len(jobs)):
            s, e, p = jobs[i]
            profit[i] = profit[i-1]
            j = bisect.bisect_right(end_times, s)
            profit[i] = max(profit[i], p if j == 0 else p + profit[j-1])
        return profit[-1]


sln = Solution()
print(sln.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))

sln = Solution()
print(sln.jobScheduling(startTime=[1,2,3,4,6], endTime=[3,5,10,6,9], profit=[20,20,100,70,60]))

sln = Solution()
print(sln.jobScheduling(startTime=[1,1,1], endTime=[2,3,4], profit=[5,6,4]))

# dp = [10,10,20,20,30,30]
# print(bisect.bisect_left(dp, 19))
# print(bisect.bisect_right(dp, 20))