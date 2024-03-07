"""
141 (Easy) Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val, self.next = x, None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        p1 = p2 = head
        while True:
            # p1 != None and p2 != None
            p1 = p1.next
            if not p1: return False
            p2 = p2.next.next if p2.next else None
            if not p2: return False
            if p1 == p2: return True
        return False