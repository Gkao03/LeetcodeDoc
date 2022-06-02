# Add Two Numbers
# Time: O(n + m). n is length of l1. m is length of l2
# Space: O(max(n, m))
# Topics: Linked List, Math, Recursion
# Difficulty: Medium

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node1 = l1
        curr_node2 = l2
        overflow = 0
        
        # assign the first node
        val_sum = curr_node1.val + curr_node2.val + overflow
        if val_sum >= 10:
            val_sum -= 10
            overflow = 1
            
        head = ListNode(val=val_sum)
        curr_node_sum = head
        
        curr_node1 = curr_node1.next if curr_node1 is not None else None
        curr_node2 = curr_node2.next if curr_node2 is not None else None
        
        # loop while not end at both lists
        while curr_node1 is not None or curr_node2 is not None:
            val1 = curr_node1.val if curr_node1 is not None else 0
            val2 = curr_node2.val if curr_node2 is not None else 0
            
            val_sum = val1 + val2 + overflow
            
            if val_sum >= 10:
                val_sum -= 10
                overflow = 1
            else:
                overflow = 0
                
            curr_node_sum.next = ListNode(val=val_sum)
            curr_node_sum = curr_node_sum.next
            
            curr_node1 = curr_node1.next if curr_node1 is not None else None
            curr_node2 = curr_node2.next if curr_node2 is not None else None
        
        # check for remaining overflow
        if overflow == 1:
            curr_node_sum.next = ListNode(val=1)
            
        return head
