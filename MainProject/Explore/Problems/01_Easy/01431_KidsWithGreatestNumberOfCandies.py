# 1431. Kids With the Greatest Number of Candies
# There are n kids with candies. You are given an integer array candies,
# where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
# they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        mx = max(candies)
        return [c + extraCandies >= mx for c in candies]

sln = Solution()
print(sln.kidsWithCandies(candies=[2,3,5,1,3], extraCandies=3))

sln = Solution()
print(sln.kidsWithCandies(candies=[4,2,1,1,2], extraCandies=1))

sln = Solution()
print(sln.kidsWithCandies(candies=[12,1,12], extraCandies=10))
