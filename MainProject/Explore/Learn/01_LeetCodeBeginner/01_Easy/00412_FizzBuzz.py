# Easy 412. Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:
#   answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#   answer[i] == "Fizz" if i is divisible by 3.
#   answer[i] == "Buzz" if i is divisible by 5.
#   answer[i] == i (as a string) if none of the above conditions are true.

class Solution:
    def fizzBuzz(self, n):
        res = n*[None]
        for i in range(1, n+1):
            r3 = i % 3; r5 = i % 5
            if r3 == 0 and r5 == 0: res[i-1] = 'FizzBuzz'
            elif r3 == 0: res[i-1] = 'Fizz'
            elif r5 == 0: res[i-1] = 'Buzz'
            else: res[i-1] = str(i)
        return res

sln = Solution()
print(sln.fizzBuzz(n=3))

sln = Solution()
print(sln.fizzBuzz(n=5))

sln = Solution()
print(sln.fizzBuzz(n=15))