# Split LInked List in Parts
# Time: O(n)
# Space: O(k) counting output. O(1) not counting output.
# Topics: Linked List
# Difficulty: Medium
# Notes: If there are N nodes in the list, and k parts, 
# then every part has N // k elements, except the first 
# N % k parts have an extra one.

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # first find how many total nodes
        num_nodes = 0
        ptr = head

        while ptr is not None:
            num_nodes += 1
            ptr = ptr.next

        output = []
        nodes_per_section = num_nodes // k
        num_one_extra = num_nodes % k
        curr_ptr = head

        while curr_ptr is not None:
            output.append(curr_ptr)

            for _ in range(nodes_per_section if len(output) <= num_one_extra else nodes_per_section - 1):
                curr_ptr = curr_ptr.next

            next_ptr = curr_ptr.next
            curr_ptr.next = None
            curr_ptr = next_ptr

        while len(output) < k:
            output.append(None)

        return output
