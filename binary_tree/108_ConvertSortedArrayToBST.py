# Convert Sorted Array to Binary Search Tree (BST)
# Time: O(n)
# Space: O(logn). The deepest we go in stack space is logn since the tree is balanced.
# Topics: Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
# Difficulty: Easy

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, left, right, arr) -> Optional[TreeNode]:
        if right < left:
            return None
        
        mid = (left + right) // 2
        
        val = arr[mid]
        new_node = TreeNode(val=val)
        
        new_node.left = self.helper(left, mid - 1, arr)
        new_node.right = self.helper(mid + 1, right, arr)
        
        return new_node
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        
        val = nums[m]
        root = TreeNode(val=val)
        
        root.left = self.helper(l, m - 1, nums)
        root.right = self.helper(m + 1, r, nums)
        
        return root
