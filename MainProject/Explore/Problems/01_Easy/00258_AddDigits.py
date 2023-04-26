# Easy 258. Add Digits
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num):
        if num == 0: return 0
        r = num % 9
        return r if r > 0 else 9