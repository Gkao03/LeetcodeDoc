# Sort List
# Time: O(nlogn). n is number of total nodes.
# Space: O(1) not considering stack space. O(logn) considering stack space.
# Topics: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
# Difficulty: Medium

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_sorted_linked_lists(self, head1, head2):
        node1, node2 = head1, head2
        if node1.val <= node2.val:
            new_head = node1
            node1 = node1.next
        else:
            new_head = node2
            node2 = node2.next
            
        curr_node = new_head
        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                curr_node.next = node1
                node1 = node1.next
            else:
                curr_node.next = node2
                node2 = node2.next
            curr_node = curr_node.next
            
        curr_node.next = node1 if node2 is None else node2
        while curr_node.next is not None:
            curr_node = curr_node.next
            
        return new_head, curr_node
    
    def merge_sort(self, left_head, num_nodes):
        if num_nodes == 1:
            return left_head, left_head
        
        right_head = left_head
        for _ in range(num_nodes // 2):
            right_head = right_head.next
            
        left_head, left_tail = self.merge_sort(left_head, num_nodes // 2)
        right_head, right_tail = self.merge_sort(right_head, (num_nodes + 1) // 2)
        left_tail.next, right_tail.next = None, None
        left_head, right_tail = self.merge_sorted_linked_lists(left_head, right_head)
        
        return left_head, right_tail
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        num_nodes = 0
        curr_node = head
        while curr_node is not None:  # O(n) time
            num_nodes += 1
            curr_node = curr_node.next
            
        head, tail = self.merge_sort(head, num_nodes)
        return head
