# Palindrome Linked List
# Time: O(n)
# Space: O(1)
# Topics: Linked List, Two Pointers, Stack, Recursion
# Difficulty: Easy
# Notes: to get O(n) time and O(1) space follow this strategy. Find the middle of the linked list.
# reverse the second half of the linked list. Compare using two pointers if the two linked lists are the same or not.
# This can also be done with O(n) time and O(n) space using stack or recursion

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # at least one node exists in constraint
        # count number of nodes to find the middle node index
        curr_node = head
        num_nodes = 0
        while curr_node is not None:
            num_nodes += 1
            curr_node = curr_node.next
            
        if num_nodes == 1:
            return True
            
        # find mid node index. We don't need to consider the middle node if odd number of nodes
        mid_node_idx = (num_nodes + 1) // 2
        
        curr_node = head
        node_idx = 0
        while node_idx != mid_node_idx:
            node_idx += 1
            curr_node = curr_node.next
        
        # prev_node is start of middle of linked list to begin reversal
        prev_node = curr_node
        curr_node = prev_node.next
        next_node = curr_node.next if curr_node is not None else None
        
        prev_node.next = None
        
        # do reversal
        while curr_node is not None:
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next if next_node is not None else None
            
        # head of reversed list is prev_node
        node1 = prev_node
        node2 = head
        
        while node1 is not None and node2 is not None:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
            
        return True
