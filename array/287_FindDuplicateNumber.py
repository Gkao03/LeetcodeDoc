# Find the Duplicate Number
# Time: O(n)
# Space: O(1)
# Topics: Array, Two Pointers, Binary Search, Bit Manipulation
# Difficulty: Medium
# Notes: this utilizes floyd's tortoise and hare approach for
# cycle detection. Similar to problem 142 Linked List Cycle II
# to find node where cycle begins.
# See https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/
# for details on the math behind the algorithm.

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ptr1 = 0  # fast pointer
        ptr2 = 0  # slow pointer
        
        # do while
        ptr1 = nums[nums[ptr1]]
        ptr2 = nums[ptr2]
        while True:
            if ptr1 == ptr2:
                break
            
            ptr1 = nums[nums[ptr1]]
            ptr2 = nums[ptr2]
        
        ptr1 = 0
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
            
        return ptr1
