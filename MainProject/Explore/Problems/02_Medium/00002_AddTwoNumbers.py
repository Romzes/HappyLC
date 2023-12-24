# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Constraints:
#   The number of nodes in each linked list is in the range [1, 100].
#   0 <= Node.val <= 9
#   It is guaranteed that the list represents a number that does not have leading zeros.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def addTwoNumbers(self, l1, l2):
        res = prev = None; car = 0
        while l1 or l2 or car > 0:
            v = car
            if l1: v += l1.val; l1 = l1.next
            if l2: v += l2.val; l2 = l2.next
            if v < 10: car = 0
            else: v, car = v-10, 1
            nd = ListNode(v)
            if prev: prev.next = nd
            else: res = nd
            prev = nd
        return res

    def print_list(self, l):
        arr = []
        while l:
            arr.append(l.val)
            l = l.next
        print(arr)

sln = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))  # 342
l2 = ListNode(5, ListNode(6, ListNode(4)))  # 465
sln.print_list(sln.addTwoNumbers(l1, l2))

sln = Solution()
l1 = ListNode(0)  # 0
l2 = ListNode(0)  # 0
sln.print_list(sln.addTwoNumbers(l1, l2))

sln = Solution()
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))  # 9999999
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))  # 9999
sln.print_list(sln.addTwoNumbers(l1, l2))