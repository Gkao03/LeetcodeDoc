# Swap Nodes in Pairs
# Time: O(n)
# Space: O(1)
# Topics: Linked List, Recursion
# Difficulty: Medium

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:  # no nodes
            return None
        
        if head.next is None:  # only 1 node exists
            return head
        
        # init
        prev = head
        curr = prev.next
        nxt = curr.next
        
        # do while (at least 2 nodes exist)
        prev.next = nxt
        curr.next = prev
        head = curr
        
        prev, curr = curr, prev  # swap
        nxt = nxt.next if nxt is not None else None
        curr = curr.next if curr is not None else None
        prev = prev.next
        
        while nxt is not None:
            curr.next = nxt.next
            prev.next = nxt
            nxt.next = curr
            
            nxt, curr = curr, nxt  # swap
            nxt = nxt.next.next if nxt is not None and nxt.next is not None else None
            curr = curr.next.next if curr is not None and curr.next is not None else None
            prev = prev.next.next
            
        return head
