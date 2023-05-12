# Medium 2140. Solving Questions With Brainpower
# You are given a 0-indexed 2D integer array questions where questions[i] = [points[i], brainpower[i]].
# The array describes the questions of an exam, where you have to process the questions in order
# (i.e., starting from question 0) and make a decision whether to solve or skip each question.
# Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions.
# If you skip question i, you get to make the decision on the next question.
#   For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
#   If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
#   If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
# Return the maximum points you can earn for the exam.
# Constraints:
#   1 <= questions.length <= 105
#   questions[i].length == 2
#   1 <= points[i], brainpower[i] <= 105

class Solution:
    def mostPoints(self, questions):
        n = len(questions); dp = n*[0]
        for i in range(n-1,-1,-1):
            p1 = questions[i][0]
            j = i + questions[i][1] + 1
            if j < n: p1 += dp[j]
            p2 = dp[i+1] if i < n-1 else 0
            dp[i] = max(p1, p2)
        return dp[0]

sln = Solution()
questions = [[3,2],[4,3],[4,4],[2,5]]
print(sln.mostPoints(questions))

sln = Solution()
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
print(sln.mostPoints(questions))
