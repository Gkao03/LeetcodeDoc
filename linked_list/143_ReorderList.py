# Reorder List
# Time: O(n)
# Space: O(1)
# Topics: Linked List, Two Pointers, Stack, Recursion
# Difficulty: Medium

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        
        slow_prev = None
        slow = head
        fast = head
        while fast is not None:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next if fast.next is not None else None
        
        slow_prev.next = None
        # slow now points to head of right half of linked list
        # reverse second half of linked list
        prev = None
        curr = slow
        nxt = curr.next
        while curr is not None:
            curr.next = prev
            prev, curr = curr, nxt
            nxt = nxt.next if nxt is not None else None
        
        # relink
        ptr1 = head
        ptr2 = prev
        while ptr1 is not None and ptr2 is not None:
            ptr1_next = ptr1.next
            ptr2_next = ptr2.next if ptr2 is not None else None
            
            ptr1.next = ptr2
            ptr1 = ptr1_next
            ptr2.next = ptr1
            ptr2 = ptr2_next
            
        return head
