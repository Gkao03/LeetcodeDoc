# Diameter of Binary Tree
# Time: O(n)
# Space: O(h) where h is height of tree. O(n) if unbalanced. O(logn) if balanced.
# Topics: Tree, Depth-First Search, Binary Tree
# Difficulty: Easy

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node):  # return tuple (max(left path, right path) including root, longest path including root so far)
        if node is None:
            return -1, 0
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        left_height = left[0] + 1
        right_height = right[0] + 1
        
        max_path_with_node = max(left[1], right[1], left_height + right_height)
        
        return max(left_height, right_height), max_path_with_node
    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # at least one node in tree
        max_direct_path, max_path_with_subnode = self.helper(root)
        return max(max_direct_path, max_path_with_subnode)
