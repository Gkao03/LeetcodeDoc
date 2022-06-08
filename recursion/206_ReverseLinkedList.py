# Reverse Linked List
# Time: O(n)
# Space: O(1)
# Topics: Linked List, Recursion
# Difficulty: Easy
# Notes: can also be done recursively.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        # at least 1 node
        if head.next is None:
            return head
        
        # at least 2 nodes
        prev_node = None
        curr_node = head
        next_node = head.next
        
        while curr_node is not None:
            curr_node.next = prev_node
            
            # move node pointers
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next if next_node is not None else None
            
        # when finished, prev_node should point to head of new linked list
        return prev_node
