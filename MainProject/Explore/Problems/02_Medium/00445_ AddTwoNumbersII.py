# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Constraints:
#   The number of nodes in each linked list is in the range [1, 100].
#   0 <= Node.val <= 9
#   It is guaranteed that the list represents a number that does not have leading zeros.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

### 1-Solution
class Solution:
    def addTwoNumbers(self, l1, l2):
        sz1 = self.list_size(l1); sz2 = self.list_size(l2);
        if sz1 < sz2: l1, l2 = l2, l1; sz1, sz2 = sz2, sz1
        arr = (sz1+1)*[None]
        for i in range(sz1, -1, -1):
            arr[i] = ListNode()
            if i < sz1: arr[i].next = arr[i+1]

        p1 = l1; p2 = l2; d = sz1-sz2
        for i in range(sz1):
            if i < d:
                arr[1+i].val = p1.val
            else:
                arr[1+i].val = p1.val + p2.val
                p2 = p2.next
            p1 = p1.next
        for i in range(sz1, 0, -1):
            if arr[i].val >= 10:
                arr[i].val -= 10
                arr[i-1].val += 1
        return arr[0] if arr[0].val > 0 else arr[1]

    def list_size(self, l):
        sz = 0
        while l: sz += 1; l = l.next
        return sz

    def print_list(self, l):
        arr = []
        while l:
            arr.append(l.val)
            l = l.next
        print(arr)

### 2-Solution (stack)
class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1 = self.list_to_stack(l1); stack2 = self.list_to_stack(l2);
        head = None; car = 0
        while stack1 or stack2 or car:
            v = car
            if stack1: v += stack1.pop()
            if stack2: v += stack2.pop()
            if v < 10: car = 0
            else: v, car = v-10, 1
            nd = ListNode(v)
            if head: nd.next = head; head = nd
            else: head = nd
        return head

    def list_to_stack(self, l):
        stack = []
        while l: stack.append(l.val); l = l.next
        return stack

    def print_list(self, l):
        arr = []
        while l:
            arr.append(l.val)
            l = l.next
        print(arr)


sln = Solution()
l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))  # 7243
l2 = ListNode(5, ListNode(6, ListNode(4)))               #  564
sln.print_list(sln.addTwoNumbers(l1, l2))

sln = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
sln.print_list(sln.addTwoNumbers(l1, l2))

sln = Solution()
l1 = ListNode(0)
l2 = ListNode(0)
sln.print_list(sln.addTwoNumbers(l1, l2))
