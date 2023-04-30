# Medium 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Recursive-1
class Solution:
    def generateParenthesis(self, n):
        self.n = n; self.res = []; self.seq = []
        self.recurs(open=0, close=0)
        return self.res

    def recurs(self, open, close):
        if len(self.seq) == 2*self.n:
            self.res.append(''.join(self.seq))
            return
        if open < self.n:
            self.seq.append('(')
            self.recurs(open+1, close)
            self.seq.pop()
        if open > close:
            self.seq.append(')')
            self.recurs(open, close+1)
            self.seq.pop()

### Recursive-2
class Solution:
    def generateParenthesis(self, n):
        self.n = n; self.res = []; self.seq = 2*n*[None]
        self.recurs(i=0, open=0, close=0)
        return self.res

    def recurs(self, i, open, close):
        if i == 2*self.n:
            self.res.append(''.join(self.seq))
            return
        if open < self.n:
            self.seq[i] = '(';
            self.recurs(i+1, open+1, close)
        if open > close:
            self.seq[i] = ')';
            self.recurs(i+1, open, close+1)


sln = Solution()
print(sln.generateParenthesis(n=1))

sln = Solution()
print(sln.generateParenthesis(n=2))

sln = Solution()
print(sln.generateParenthesis(n=3))

sln = Solution()
print(sln.generateParenthesis(n=4))