# Hard 1335. Minimum Difficulty of a Job Schedule
# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).
# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days.
# The difficulty of a day is the maximum difficulty of a job done on that day.
# You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].
# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

class Solution:
    def minDifficulty(self, jobDifficulty, d):
        pass

sln = Solution()
print(sln.minDifficulty(jobDifficulty=[6,5,4,3,2,1], d=2))

sln = Solution()
print(sln.minDifficulty(jobDifficulty=[9,9,9], d=4))

sln = Solution()
print(sln.minDifficulty(jobDifficulty=[1,1,1], d=3))