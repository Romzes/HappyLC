# Easy 1491. Average Salary Excluding the Minimum and Maximum Salary
# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def average(self, salary):
        return (sum(salary) - min(salary) - max(salary)) / (len(salary)-2)

class Solution:
    def average(self, salary):
        sum = 0; mn = 1e9; mx = -1e9
        for sal in salary: sum += sal; mn = min(mn, sal); mx = max(mx, sal)
        return (sum - mn - mx)/(len(salary) - 2)

sln = Solution()
print(sln.average(salary=[4000,3000,1000,2000]))

sln = Solution()
print(sln.average(salary=[1000,2000,3000]))