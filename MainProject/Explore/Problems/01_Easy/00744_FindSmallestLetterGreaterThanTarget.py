# Easy 744. Find Smallest Letter Greater Than Target
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
# There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters, target):
        ans = ''; l = 0; r = len(letters)-1
        while l <= r:
            m = (l + r)//2; v = letters[m]
            if v <= target: l = m+1
            else: ans = v; r = m-1
        return ans if ans != '' else letters[0]

sln = Solution()
print(sln.nextGreatestLetter(letters=['c','f','j'], target='a'))

sln = Solution()
print(sln.nextGreatestLetter(letters=['c','f','j'], target='c'))

sln = Solution()
print(sln.nextGreatestLetter(letters=['x','x','y','y'], target='z'))