# Easy 206. Reverse Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def reverseList(self, head):
        # if not head or not head.next: return head
        prev, curr = None, head
        while curr: curr.next, prev, curr = prev, curr, curr.next
        return prev

class Solution:
    def reverseList(self, head):
        # if not head or not head.next: return head
        prev = None  # head of reversed list before curr
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

sln = Solution()
head = None
print(sln.reverseList(head))

sln = Solution()
head = ListNode(1)
rvr = sln.reverseList(head)
print(rvr.val)

sln = Solution()
head = ListNode(1, ListNode(2))
rvr = sln.reverseList(head)
print(rvr.val)