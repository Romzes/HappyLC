class Node:
    def __init__(self, x, next=None, random=None):
        self.val, self.next, self.random = int(x), next, random

class Solution(object):
    def copyRandomList(self, head):
        if not head: return None
        node_map = {}
        src_curr = head; dst_head = None; dst_prev = None
        while src_curr:
            dst_curr = Node(x=src_curr.val, random=src_curr)
            node_map[src_curr] = dst_curr
            if not dst_head: dst_head = dst_curr
            if dst_prev: dst_prev.next = dst_curr
            dst_prev = dst_curr
            src_curr = src_curr.next

        dst_curr = dst_head
        while dst_curr:
            src_rand = dst_curr.random.random
            dst_curr.random = node_map[src_rand] if src_rand else None
            dst_curr = dst_curr.next

        return dst_head
