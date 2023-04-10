# Medium 1353. Maximum Number of Events That Can Be Attended
# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
# Return the maximum number of events you can attend.

class Solution:
    def maxEvents(self, events):
        days, i = 2*len(events)*[None], 0
        for ev in events:
            days[i], days[i+1] = (ev[0], 1), (ev[1]+1, -1)
            i += 2
        days.sort(key=lambda day: day[0] + 0.1*day[1])
        sum, mx = 0, -1e10
        for i, day in enumerate(days):
            sum += day[1]
            if sum > mx: mx = sum
        return mx

sln = Solution()
print(sln.maxEvents(events=[[1,2],[2,3],[3,4]]))

sln = Solution()
print(sln.maxEvents(events=[[1,2],[2,3],[3,4],[1,2]]))