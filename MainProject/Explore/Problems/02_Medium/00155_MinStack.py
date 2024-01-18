"""
155. (Medium) Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
  MinStack() initializes the stack object.
  void push(int val) pushes the element val onto the stack.
  void pop() removes the element on the top of the stack.
  int top() gets the top element of the stack.
  int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Constraints:
  -2^31 <= val <= 2^31 - 1
  Methods pop, top and getMin operations will always be called on non-empty stacks.
  At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""

class MinStack:
    def __init__(self):
        self.stack, self.min_arr = [], [2**31-1]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_arr.append(min(self.min_arr[-1], val))

    def pop(self) -> None:
        self.min_arr.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # return -3
minStack.pop()
print(minStack.top())  # return 0
print(minStack.getMin())  # return -2