# Rotate List
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        num_nodes = 0
        curr_node = head
        tail = head
        while curr_node is not None:
            num_nodes += 1
            curr_node = curr_node.next
            tail = tail.next if tail.next is not None else tail
            
        rotate_k = k % num_nodes
        if rotate_k == 0:
            return head
        
        front_ptr = head
        for _ in range(rotate_k):
            front_ptr = front_ptr.next
            
        new_head = head
        prev_ptr = None
        while front_ptr is not None:
            front_ptr = front_ptr.next
            prev_ptr = new_head
            new_head = new_head.next
        
        tail.next = head
        prev_ptr.next = None
        return new_head
