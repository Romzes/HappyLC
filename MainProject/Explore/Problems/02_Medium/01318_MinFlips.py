# Medium 1318. Minimum Flips to Make a OR b Equal to c
# Given 3 positives numbers a, b and c.
# Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

class Solution:
    def minFlips(self, a, b, c):
        # a,b,c : int > 0
        d = a | b
        if c == d: return 0
        flp = 0; mask = 1; mx = max(a, b, c)
        while mask <= mx:
            cm = c & mask
            if cm != (d & mask):
                flp += 2 if cm == 0 and (a & mask) & (b & mask) else 1
            mask <<= 1
        return flp


sln = Solution()
print(sln.minFlips(a=2, b=6, c=5))

sln = Solution()
print(sln.minFlips(a=4, b=2, c=7))

sln = Solution()
print(sln.minFlips(a=1, b=2, c=3))

# a=2
# b=6
# c=5
# print(a | b)