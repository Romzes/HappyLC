# Medium 253. Meeting Rooms II
# Given an array of meeting time intervals intervals where intervals[i] = [ start[i], end[i] )
# return the minimum number of conference rooms required.

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals: List[List[int]]
        moments = 2*len(intervals)*[None]; j = 0
        for itv in intervals:
            moments[j], moments[j+1] = (itv[0], 1), (itv[1], -1)
            j += 2
        moments.sort(key=lambda mnt: mnt[0] + 0.1 * mnt[1])
        sum = 0; rooms = -1
        for mnt in moments:
            sum += mnt[1]
            if sum > rooms: rooms = sum
        return rooms

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals); beg = n*[None]; end = n*[None]
        for i, itv in enumerate(intervals): beg[i] = itv[0]; end[i] = itv[1]
        beg.sort(); end.sort()
        i = j = 0; sum = 0; rooms = -1
        while i < n:
            if beg[i] < end[j]: sum +=1; i += 1
            elif end[j] < beg[i]: sum -= 1; j += 1
            else: i += 1; j += 1
            rooms = max(rooms, sum)
        return rooms

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        arr = 2 * len(intervals) * [None]; i = 0
        for j, itv in enumerate(intervals):
            arr[i], arr[i+1] = (itv[0], 1), (itv[1], -1)
            i += 2
        arr.sort()
        s = rooms = 0
        for a in arr:
            s += a[1]
            rooms = max(rooms, s)
        return rooms

sln = Solution()
print(sln.minMeetingRooms(intervals=[[0,30],[5,10],[15,20]]))

sln = Solution()
print(sln.minMeetingRooms(intervals=[[7,10],[2,4]]))

sln = Solution()
print(sln.minMeetingRooms(intervals=[[0,20],[5,20],[15,20]]))