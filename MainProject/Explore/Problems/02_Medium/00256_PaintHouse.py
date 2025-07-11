# 256 (Medium) Paint House
"""
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.

Constraints:
  costs.length == n
  costs[i].length == 3
  1 <= n <= 100
  1 <= costs[i][j] <= 20
"""

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 18.00 MB  Beats 31.44%
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        opt = costs[0]
        for i in range(1, len(costs)):
            # opt[0,1,2] = минимальная цена покраски первых i домов cost[0..i-1], при условии что дом costs[i-1] покрашен в цвет j=0,1,2
            opt = [
                costs[i][0] + min(opt[1], opt[2]),
                costs[i][1] + min(opt[0], opt[2]),
                costs[i][2] + min(opt[0], opt[1])
            ]
        return min(opt)


sln = Solution()
print(sln.minCost(costs=[[17,2,17],[16,16,5],[14,3,19]]))  # Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.

sln = Solution()
print(sln.minCost(costs=[[7,6,2]]))  # Output: 2

sln = Solution()
print(sln.minCost(costs=[[3,5,3],[6,17,6],[7,13,18],[9,10,18]]))  # Output: 26
