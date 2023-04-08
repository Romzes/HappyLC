# Easy 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math

class Solution:
    def middleNode(self, head):
        if not head: return None
        curr, cnt = head, self.count(head)
        for i in range(math.floor(cnt/2)): curr = curr.next
        return curr

    def count(self, head):
        curr, cnt = head, 0
        while curr: curr, cnt = curr.next, cnt+1
        return cnt

sln = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(sln.middleNode(head).val)