from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        date_points = []
        for itv in intervals:
            date_points.append((itv[0], 1))
            date_points.append((itv[1], -1))
        date_points.sort()  # в массиве date_points на заданную дату: выезд до въезда
        min_rooms = 0
        s = 0
        for dp in date_points:
            s += dp[1]
            min_rooms = max(min_rooms, s)
        return min_rooms

sln = Solution()  # Example 1
print(sln.minMeetingRooms(intervals=[[0,30],[5,10],[15,20]]))  # Output: 2

sln = Solution()  # Example 2
print(sln.minMeetingRooms(intervals=[[7,10],[2,4]]))  # Output: 1