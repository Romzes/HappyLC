from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.res_list, self.arr = [], []
        self.backtrack(open_cnt=0, close_cnt=0)
        return self.res_list

    def backtrack(self, open_cnt, close_cnt):
        # дано: 0 <= close_cnt <= open_cnt <= n
        if len(self.arr) == 2 * self.n:
            self.res_list.append(''.join(self.arr))
            return
        if open_cnt < self.n:
            self.arr.append('(')
            self.backtrack(open_cnt=open_cnt+1, close_cnt=close_cnt)
            self.arr.pop()
        if close_cnt < open_cnt:
            self.arr.append(')')
            self.backtrack(open_cnt=open_cnt, close_cnt=close_cnt+1)
            self.arr.pop()

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.res_list, self.arr, self.open_cnt = [], [], 0
        self.backtrack()
        return self.res_list

    def backtrack(self):
        # инвариант: 0 <= close_cnt <= open_cnt <= n
        if len(self.arr) == 2 * self.n:
            self.res_list.append(''.join(self.arr))
            return
        if self.open_cnt < self.n:
            self.arr.append('(')
            self.open_cnt += 1
            self.backtrack()
            self.arr.pop()
            self.open_cnt -= 1
        if len(self.arr) - self.open_cnt < self.open_cnt:
            # close_cnt < open_cnt
            self.arr.append(')')
            self.backtrack()
            self.arr.pop()

sln = Solution()  # Example 1
print(sln.generateParenthesis(n=3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]

sln = Solution()  # Example 2
print(sln.generateParenthesis(n=1))  # Output: ["()"]


