# Validate Binary Search Tree
# Time: O(n). n is number of nodes in tree
# Space: O(h) stack space. h is height of binary tree. O(n) if unbalanced. O(logn) if balanced.
# Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Difficulty: Medium

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST_helper(self, node, left_limit, right_limit):
        if node is None:
            return True
        
        if not (left_limit <= node.val <= right_limit):  # node value not within valid range
            return False
        
        return self.isValidBST_helper(node.left, left_limit, node.val - 1) and self.isValidBST_helper(node.right, node.val + 1, right_limit)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # node values are integers
        max_limit = float("inf")
        min_limit = float("-inf")
        
        return self.isValidBST_helper(root, min_limit, max_limit)
