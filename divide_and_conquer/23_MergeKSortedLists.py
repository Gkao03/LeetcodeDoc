# Merge k Sorted Lists
# Time: O(nklogk). n is average length of each lists[i]. k is number of lists == len(lists).
# Space: O(1)
# Topics: Linked List, Divide and Conquer, Heap, Merge Sort
# Difficulty: Hard
# Notes: can also use heap or recursive method with same runtime,
# but will use extra space.

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:            
    def merge_sorted_lists(self, head1, head2):
        if head1 is None:
            return head2
        
        if head2 is None:
            return head1
        
        ptr1, ptr2 = head1, head2
        if ptr1.val <= ptr2.val:
            curr_node = ptr1
            ptr1 = ptr1.next
        else:
            curr_node = ptr2
            ptr2 = ptr2.next
            
        new_head = curr_node
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                curr_node.next = ptr1
                ptr1 = ptr1.next
            else:
                curr_node.next = ptr2
                ptr2 = ptr2.next
            curr_node = curr_node.next
                
        curr_node.next = ptr1 if ptr2 is None else ptr2
        return new_head
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        end_idx = len(lists) - 1
        while end_idx > 0:
            curr_idx = 0
            
            while curr_idx <= end_idx:
                store_idx = curr_idx // 2
                
                if curr_idx + 1 <= end_idx:
                    merge_head = self.merge_sorted_lists(lists[curr_idx], lists[curr_idx + 1])
                else:
                    merge_head = lists[curr_idx]
                    
                lists[store_idx] = merge_head
                curr_idx += 2
            
            end_idx = end_idx // 2
            
        return lists[0]
