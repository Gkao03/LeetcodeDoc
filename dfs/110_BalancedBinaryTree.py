# Balanced Binary Tree
# Time: O(n)
# Space: O(h) stack space where h is height of tree. O(n) if not balanced. O(logn) if balanced.
# Topics: Tree, Depth-First Search, Binary Tree
# Difficulty: Easy
# Notes: to get from O(n^2) to O(n) time, calculate height and balance in same dfs to avoid repeated computation (see helper)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node):  # return tuple (T/F, height)
        if node is None:
            return True, 0
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        left_is_balanced, left_height = left[0], left[1]
        right_is_balanced, right_height = right[0], right[1]
        
        is_balanced = left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1
        
        return is_balanced, max(left_height, right_height) + 1
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, _ = self.helper(root)
        
        return is_balanced
