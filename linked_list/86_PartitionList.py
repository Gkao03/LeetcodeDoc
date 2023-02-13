# Partition List
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_less, curr_less = None, None
        head_geq, curr_geq = None, None
        curr_ptr = head

        while curr_ptr is not None:
            if curr_ptr.val < x:
                if head_less is None:
                    head_less = curr_ptr
                    curr_less = curr_ptr
                else:
                    curr_less.next = curr_ptr
                    curr_less = curr_less.next
            else:  # curr_ptr.val >= x
                if head_geq is None:
                    head_geq = curr_ptr
                    curr_geq = curr_ptr
                else:
                    curr_geq.next = curr_ptr
                    curr_geq = curr_geq.next
            
            curr_ptr = curr_ptr.next

        if curr_less is not None:
            curr_less.next = head_geq

        if curr_geq is not None:
            curr_geq.next = None

        return head_less if head_less is not None else head_geq
