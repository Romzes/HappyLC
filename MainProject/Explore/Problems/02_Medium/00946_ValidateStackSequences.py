# Medium 946. Validate Stack Sequences
# Given two integer arrays pushed and popped each with distinct values,
# return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
# Constraints:
#   All the elements of pushed are unique.
#   popped.length == pushed.length
#   popped is a permutation of pushed.

# stack
class Solution:
    def validateStackSequences(self, pushed, popped):
        i, j, n, stack = 0, 0, len(pushed), []
        while True:
            if stack and j < n and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            elif i < n:
                stack.append(pushed[i])
                i += 1
            else:
                break
        return len(stack) == 0

# two pointers, memory=O(1)
class Solution:
    def validateStackSequences(self, pushed, popped):
        i, j, n, s = 0, 0, len(pushed), 0
        while True:
            if s > 0 and j < n and pushed[s-1] == popped[j]: s, j = s-1, j+1
            elif i < n: pushed[s], s, i = pushed[i], s+1, i+1
            else: break
        return s == 0

sln = Solution()
print(sln.validateStackSequences(pushed=[1,2,3,4,5], popped=[4,5,3,2,1]))

sln = Solution()
print(sln.validateStackSequences(pushed=[1,2,3,4,5], popped=[4,3,5,1,2]))

sln = Solution()
print(sln.validateStackSequences(pushed=[1,2,3,4,5,6,7,8,9], popped=[4,5,6,3,2,1,8,7,9]))