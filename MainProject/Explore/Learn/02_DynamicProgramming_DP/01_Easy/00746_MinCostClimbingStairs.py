# Easy 746. Min Cost Climbing Stairs
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
# Constraints:
#   2 <= cost.length <= 1000

class Solution:
    def minCostClimbingStairs(self, cost):
        a, b = cost[-2], cost[-1]
        for i in range(len(cost)-3, -1, -1): a, b = cost[i] + min(a, b), a
        return min(a, b)

sln = Solution()
print(sln.minCostClimbingStairs(cost=[2,1]))

sln = Solution()
print(sln.minCostClimbingStairs(cost=[10,15,20]))

sln = Solution()
print(sln.minCostClimbingStairs(cost=[1,100,1,1,1,100,1,1,100,1]))