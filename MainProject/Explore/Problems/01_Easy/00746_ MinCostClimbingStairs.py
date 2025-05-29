# Easy 746. Min Cost Climbing Stairs
"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Constraints:
  2 <= cost.length <= 1000
  0 <= cost[i] <= 999
"""

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m = len(cost)
        dp = m * [0]  # dp[i] - минимальная цена восхождения со ступеньки с индексом = i
        dp[-1], dp[-2] = cost[-1], cost[-2]
        for i in range(m-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])


sln = Solution()
print(sln.minCostClimbingStairs(cost=[10,15,20]))

sln = Solution()
print(sln.minCostClimbingStairs(cost=[1,100,1,1,1,100,1,1,100,1]))