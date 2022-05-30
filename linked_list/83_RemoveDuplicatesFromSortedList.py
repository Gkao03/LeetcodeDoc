# Remove Duplicates from Sorted List
# Time: O(n)
# Space: O(1)
# Topics: Linked List
# Difficulty: Easy

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr_node = head
        
        while curr_node.next is not None:
            next_val = curr_node.next.val
            
            if next_val == curr_node.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
                
        return head
