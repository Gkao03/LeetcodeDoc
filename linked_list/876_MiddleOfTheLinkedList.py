# Middle of the Linked List
# Time: O(n)
# Space: O(1)
# Topics: Linked List, Two Pointers
# Difficulty: Easy

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # at least one node exists
        curr_node = head
        num_nodes = 0
        
        while curr_node is not None:
            num_nodes += 1
            curr_node = curr_node.next
            
        target_idx = num_nodes // 2
        curr_idx = 0
        
        curr_node = head
        while curr_node is not None:
            if curr_idx == target_idx:
                return curr_node
            
            curr_node = curr_node.next
            curr_idx += 1
            
        # above while loop has to return
