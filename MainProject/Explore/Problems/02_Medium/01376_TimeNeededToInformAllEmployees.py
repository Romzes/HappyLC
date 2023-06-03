# Medium 1376. Time Needed to Inform All Employees
# A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.
# Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1.
# Also, it is guaranteed that the subordination relationships have a tree structure.
# The head of the company wants to inform all the company employees of an urgent piece of news.
# He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.
# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).
# Return the number of minutes needed to inform all the employees about the urgent news.

class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        if n <= 1: return 0
        tree = n * [None]
        for i, m in enumerate(manager):
            if m == -1: continue
            if tree[m] is None: tree[m] = []
            tree[m].append(i)

        def calc_minutes(i):
            if tree[i] is None: return 0
            mx = 0
            for j in tree[i]: mx = max(mx, calc_minutes(j))
            return mx + informTime[i]

        return calc_minutes(headID)


sln = Solution()
print(sln.numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]))

sln = Solution()
print(sln.numOfMinutes(n=6, headID=2, manager=[2,2,-1,2,2,2], informTime=[0,0,1,0,0,0]))

sln = Solution()
print(sln.numOfMinutes(n=5, headID=0, manager=[-1,0,0,1,2], informTime=[5,10,20,0,0]))