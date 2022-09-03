# Remove Nth Node From End of List
# Time: O(n)
# Space: O(1)
# Topics: Linked List, Two Pointers
# Difficulty: Medium

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = head
        for _ in range(n):
            ptr1 = ptr1.next
            
        ptr2 = head
        prev = None
        nxt = ptr2.next
        while ptr1 is not None:
            ptr1 = ptr1.next
            prev = ptr2
            ptr2 = nxt
            nxt = nxt.next if nxt is not None else nxt
            
        # remove node at pointer 2
        if prev is None:  # ptr2 is at head
            head = nxt
        else:
            prev.next = nxt
            
        return head
