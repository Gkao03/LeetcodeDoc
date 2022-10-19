# Reverse Nodes in k-Group
# Time: O(n)
# Space: O(1)
# Topics: Linked List, Recursion
# Difficulty: Hard

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # at least 1 node exists
        if k == 1:
            return head
        
        end_ptr = head
        ptr1 = prev_tail = None
        ptr2 = curr_tail = head
        ptr3 = head.next
        
        while end_ptr is not None:
            # count k nodes
            counter = 0
            while end_ptr is not None and counter < k:
                counter += 1
                end_ptr = end_ptr.next
                
            if counter < k:  # left out nodes should not be reversed
                return head
            
            while ptr2 is not end_ptr:
                ptr2.next = ptr1
                
                # move pointers
                ptr1 = ptr2
                ptr2 = ptr3
                ptr3 = ptr3.next if ptr3 is not None else None
                
            # relink
            if prev_tail is None:  # check to make sure new head is correct
                head = ptr1
                
            if prev_tail is not None:
                prev_tail.next = ptr1
                
            curr_tail.next = ptr2
            
            # update tails
            prev_tail = curr_tail
            curr_tail = ptr2
        
        return head
