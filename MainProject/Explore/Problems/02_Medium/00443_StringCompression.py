# 443. (Medium) String Compression
# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#     If the group's length is 1, append the character to s.
#     Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.
# Constraints:
#  1 <= chars.length <= 2000
#  chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

from typing import List
########## LeetCode ####################################################################################################
class Solution:
    def compress(self, chars: List[str]) -> int:
        j, c0, cnt = 0, chars[0], 1
        for i in range(1, len(chars)):
            c = chars[i]
            if c == c0: cnt += 1
            else:
                j = self.set_char(chars, j, c0, cnt)
                c0, cnt = c, 1
        j = self.set_char(chars, j, c0, cnt)
        return j

    def set_char(self, chars, j, c0, cnt):
        chars[j], j = c0, j+1
        if cnt == 1: return j
        if 2 <= cnt <= 9:
            chars[j] = str(cnt)
            return j+1
        l = list(str(cnt))
        j2 = j+len(l)
        chars[j:j2] = l
        return j2

class Solution:
    def compress(self, chars: List[str]) -> int:
        # leetcode 443
        j = 0
        pi = pc = None
        for i, c in enumerate(chars):
            if i == 0 or c != (chars[i-1] if i-1 != pi else pc): m = 1
            else: m += 1
            if i == len(chars)-1 or c != chars[i+1]:
                pi = j+m-1; pc = chars[pi]  # save prev chars
                chars[j] = c; j += 1
                if m > 1:
                    for d in str(m): chars[j] = d; j += 1

        return j

def test_solution():
    sln = Solution()
    chars = ['a', 'a', '2']  # ['a', '2', '2'] !!! МОЖНО ОШИБИТЬСЯ !!!
    j = sln.compress(chars)
    print(j)
    print(chars[0:j])

    sln = Solution()
    chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    j = sln.compress(chars)
    print(j)
    print(chars[0:j])

    sln = Solution()
    chars = ['a']
    j = sln.compress(chars)
    print(j)
    print(chars[0:j])

    sln = Solution()
    chars = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    j = sln.compress(chars)
    print(j)
    print(chars[0:j])

    sln = Solution()
    chars = ['a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
             'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
    j = sln.compress(chars)
    print(j)
    print(chars[0:j])

test_solution()

########## Yandex ######################################################################################################
def compress(chars: str) -> str:
    # Yandex
    res = []
    for i, c in enumerate(chars):
        m = 1 if i == 0 or c != chars[i-1] else m+1
        if i == len(chars)-1 or c != chars[i+1]:
            res.append(c)
            if m > 1: res.append(str(m))
    return ''.join(res)

def test_compress():
    print(compress(chars='abc'))
    print(compress(chars='aa2'))
    print(compress(chars='222333'))
    print(compress(chars='aaa3aaa3bb2'))

# test_compress()
