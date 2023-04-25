# Easy 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s):
        i = 0; j = len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1; j -= 1

sln = Solution()
s = ['h','e','l','l','o']
sln.reverseString(s)
print(s)

sln = Solution()
s = ['H','a','n','n','a','h']
sln.reverseString(s)
print(s)
