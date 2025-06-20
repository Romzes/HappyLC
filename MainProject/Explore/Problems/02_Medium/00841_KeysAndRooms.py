# 841 (Medium) Keys and Rooms
"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it.
Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
return true if you can visit all the rooms, or false otherwise.

Constraints:
  n == rooms.length
  2 <= n <= 1000
  0 <= rooms[i].length <= 1000
  1 <= sum(rooms[i].length) <= 3000
  0 <= rooms[i][j] < n
  All the values of rooms[i] are unique.

"""

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 17.96 MB  Beats 99.29%
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        stack = rooms[0]  # список доступных ключей
        rooms[0] = None  # признак открытой комнаты
        open = 1  # кол-во открытых комнат
        while stack and open < n:
            k = stack.pop()
            if rooms[k] is None: continue  # комната-k уже была открыта раньше
            open += 1  # открыли комнату-K
            stack.extend(rooms[k])
            rooms[k] = None  # признак открытой комнаты
        return open == n


sln = Solution()
print(sln.canVisitAllRooms(rooms=[[1],[2],[3],[]]))  # Output: true

sln = Solution()
print(sln.canVisitAllRooms(rooms=[[1,3],[3,0,1],[2],[0]]))  # Output: false