# Medium 253. Meeting Rooms II
# Given an array of meeting time intervals intervals where intervals[i] = [ start[i], end[i] )
# return the minimum number of conference rooms required.

class Solution:
    def minMeetingRooms(self, intervals):
        moments, j = 2*len(intervals)*[None], 0
        for itv in intervals:
            moments[j], moments[j+1] = (itv[0], 1), (itv[1], -1)
            j += 2
        moments.sort(key=lambda mnt: mnt[0] + 0.1 * mnt[1])
        sum, rooms = 0, -1e10
        for mnt in moments:
            sum += mnt[1]
            if sum > rooms: rooms = sum
        return rooms

sln = Solution()
print(sln.minMeetingRooms(intervals=[[0,30],[5,10],[15,20]]))

sln = Solution()
print(sln.minMeetingRooms(intervals=[[7,10],[2,4]]))