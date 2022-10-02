# Binary Tree Maximum Path Sum
# Time: O(n)
# Space: O(h) stack space. h is height of tree. O(n) worst case. O(logn) if balanced tree.
# Topics: Dynamic Programming, Tree, Depth-First Search, Binary Tree
# Difficulty: Hard

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_path_helper(self, node):
        if node.left is None and node.right is None:
            self.max_path_sum = max(self.max_path_sum, node.val)
            return node.val
        
        left_sum = 0 if node.left is None else self.max_path_helper(node.left)
        right_sum = 0 if node.right is None else self.max_path_helper(node.right)
        left_pos_sum = left_sum if left_sum > 0 else 0
        right_pos_sum = right_sum if right_sum > 0 else 0
        
        self.max_path_sum = max(self.max_path_sum, left_pos_sum + right_pos_sum + node.val)
        return max(left_sum + node.val, right_sum + node.val, node.val)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # at least 1 node in tree exists
        self.max_path_sum = float('-inf')
        self.max_path_helper(root)
        return self.max_path_sum
