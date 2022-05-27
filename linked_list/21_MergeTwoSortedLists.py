# Merge Two Sorted (Linked) Lists
# Time: O(n)
# Space: O(1)
# Topics: Linked List, Recursion (not really)
# Difficulty: Easy

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_list(self, node):  # for debugging
        vals = []
        
        while node is not None:
            vals.append(node.val)
            node = node.next
            
        print(vals)
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        # list1 and list2 will not be NULL here
        curr_node1 = list1
        curr_node2 = list2
        
        head = None
        if curr_node1.val <= curr_node2.val:
            head = curr_node1
            curr_node1 = curr_node1.next
        else:
            head = curr_node2
            curr_node2 = curr_node2.next
            
        node_ptr = head
        
        while curr_node1 is not None and curr_node2 is not None:
            if curr_node1.val <= curr_node2.val:
                node_ptr.next = curr_node1
                curr_node1 = curr_node1.next
            else:
                node_ptr.next = curr_node2
                curr_node2 = curr_node2.next
            
            node_ptr = node_ptr.next
                
        if curr_node1 is None:
            node_ptr.next = curr_node2
        elif curr_node2 is None:
            node_ptr.next = curr_node1
            
        return head