"""
You are given an integer n. There are n rooms numbered from 0 to n - 1.
You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi).
All the values of starti are unique.
Meetings are allocated to rooms in the following manner:
  Each meeting will take place in the unused room with the lowest number.
  If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
  When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.
A half-closed interval [a, b) is the interval between a and b including a and not including b.
Constraints:
  1 <= n <= 100
  1 <= meetings.length <= 10^5
  meetings[i].length == 2
  0 <= starti < endi <= 5 * 10^5
  All the values of starti are unique.
"""
from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        res = {}  # {room: cnt}
        max_room = max_cnt = -1
        free_rooms = list(range(n))  # list[room]
        work_rooms = []  # list[(end, room)]
        meetings.sort()
        for mt in meetings:
            while work_rooms and work_rooms[0][0] <= mt[0]:
                end, room = heapq.heappop(work_rooms)
                heapq.heappush(free_rooms, room)
            if free_rooms:
                room = heapq.heappop(free_rooms)
                end = mt[1]
            else:
                item = heapq.heappop(work_rooms)
                room = item[1]
                end = item[0] + mt[1] - mt[0]
            heapq.heappush(work_rooms, (end, room))
            cnt = res[room] = res.get(room, 0) + 1
            if cnt > max_cnt or cnt == max_cnt and room < max_room:
                max_room, max_cnt = room, cnt
        return max_room

sln = Solution()
print(sln.mostBooked(n=2, meetings=[[0,10],[1,5],[2,7],[3,4]]))

sln = Solution()
print(sln.mostBooked(n=3, meetings=[[1,20],[2,10],[3,5],[4,9],[6,8]]))

sln = Solution()
print(sln.mostBooked(n=4, meetings=[[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]))