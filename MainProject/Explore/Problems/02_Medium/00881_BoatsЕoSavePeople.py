# Medium 881. Boats to Save People
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.

class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        boats, j1, j2 = 0, 0, len(people)-1
        while j1 <= j2:
            if people[j1] + people[j2] <= limit: j1, j2 = j1+1, j2-1
            else: j2 -= 1
            boats += 1
        return boats

sln = Solution()
print(sln.numRescueBoats(people=[1,1,2,3,4,5], limit=5))

