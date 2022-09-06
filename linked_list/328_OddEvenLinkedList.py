# Odd Even Linked List
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:  # no nodes
            return None
        
        if head.next is None or head.next.next is None:  # 1 or 2 nodes
            return head
        
        # at least 3 nodes exist
        even_head = head.next
        ptr1 = head
        ptr2 = ptr1.next
        ptr3 = ptr2.next
        
        while ptr3 is not None:
            odd_tail = ptr3
            ptr1.next = ptr3
            ptr2.next = ptr3.next
            
            # move pointers
            ptr1 = ptr3
            ptr2 = ptr3.next
            ptr3 = ptr2.next if ptr2 is not None else None
            
        odd_tail.next = even_head
        return head
