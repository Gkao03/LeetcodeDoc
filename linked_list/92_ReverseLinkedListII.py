# Reverse Linked List II
# Time: O(n)
# Space: O(1)
# Topics: Linked List
# Difficulty: Medium

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        counter = 1
        prev = None
        curr = head
        nxt = head.next

        # find start point for curr
        while counter < left:
            prev = curr
            curr = nxt
            nxt = nxt.next if nxt is not None else None
            counter += 1

        left_tail = prev
        reversed_tail = curr
        prev = None

        while counter <= right:
            curr.next = prev

            # update pointers
            prev = curr
            curr = nxt
            nxt = nxt.next if nxt is not None else None
            
            counter += 1

        # prev at head of reversed list. curr at head of right list. now relink
        reversed_head = prev
        right_head = curr
        
        if left_tail is not None:
            left_tail.next = prev

        reversed_tail.next = right_head

        return reversed_head if left == 1 else head
