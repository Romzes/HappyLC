# 1167 (Medium) Minimum Cost to Connect Sticks
"""
You have some number of sticks with positive integer lengths.
These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.
You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y.
You must connect all the sticks until there is only one stick remaining.
Return the minimum cost of connecting all the given sticks into one stick in this way.

Constraints:
  1 <= sticks.length <= 10^4
  1 <= sticks[i] <= 10^4
"""

from typing import List
import heapq

# Runtime=75 ms  Beats=96.87%    Memory=18.88 MB  Beats=46.11%
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1: return 0
        if len(sticks) == 2: return sticks[0] + sticks[1]
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 2:
            s1 = heapq.heappop(sticks)
            s = s1 + sticks[0]
            cost += s
            heapq.heappushpop(sticks, s)
        return cost + sticks[0] + sticks[1]

# Runtime = 71 ms   Beats=99.53%     Memory=18.94 MB  Beats=26.66%
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1: return 0
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s = s1 + sticks[0]
            cost += s
            heapq.heappushpop(sticks, s)
        return cost


""" Доказательство
Шаг 1
A = a[1], a[2], ... a[n] - 1ое множество палок
B = b[1], b[2], ... b[n] - 2ое множество палок
a[i] <= b[i]
тогда min_cost(A) <= min_cost(B)
Док-во: возьмём оптимальный вариант соединения B и сделаем аналогичное по индексам соединение из A, тогда min_cost(B) <= index_cost(A) <= min_cost(A)
Шаг 2
для данных sticks
A = соединение 2ух самых коротких палок из sticks + все остальные sticks
B = соединение 2ух произвольных палок из sticks + все остальные sticks
переход к шагу 1
"""
# индукция по n = len(sticks): как оптимально соединить 2,3,4, ... палок
sln = Solution()
sticks = [2,4,3]
print(sln.connectSticks(sticks=sticks))  # output: 14

sln = Solution()
sticks = [1,8,3,5]
print(sln.connectSticks(sticks=sticks))  # output: 30

sln = Solution()
sticks = [5]
print(sln.connectSticks(sticks=sticks))  # output: 0