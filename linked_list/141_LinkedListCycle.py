# Linked List Cycle
# Time: O(n)
# Space: O(1)
# Topics: Hash Table, Linked List, Two Pointers
# Difficulty: Easy
# Notes: a hash table can also be used to check visited nodes but will use O(n) space

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        counter = 0
        fast_pointer = head.next
        slow_pointer = head
        
        while fast_pointer is not None and slow_pointer is not None:
            if fast_pointer is None or slow_pointer is None:
                break
            
            # both fast and slow are not None here
            if fast_pointer == slow_pointer:  # same memory address
                return True
            
            # print(fast_pointer)
            
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next if counter % 2 == 0 else slow_pointer
            
            counter += 1
        
        # Linked List reached the end for one or both pointers
        return False
