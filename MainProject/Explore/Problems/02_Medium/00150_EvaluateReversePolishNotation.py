"""
150 (Medium) Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
  The valid operators are '+', '-', '*', and '/'.
  Each operand may be an integer or another expression.
  The division between two integers always truncates toward zero.
  There will not be any division by zero.
  The input represents a valid arithmetic expression in a reverse polish notation.
  The answer and all the intermediate calculations can be represented in a 32-bit integer.
Constraints:
  1 <= tokens.length <= 10^4
  tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opers = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: int(x / y)}
        stack = []
        for t in tokens:
            f = opers.get(t)
            if f:
                y, x = stack.pop(), stack.pop()
                stack.append(f(x, y))
            else:
                stack.append(int(t))
        return stack[-1]

sln = Solution()
print(sln.evalRPN(tokens=["2","1","+","3","*"]))

sln = Solution()
print(sln.evalRPN(tokens=["4","13","5","/","+"]))

sln = Solution()
print(sln.evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

