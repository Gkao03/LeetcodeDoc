# Invert Binary Tree
# Time: O(n)
# Space: O(h) where h is height of tree (stack space) ==> O(n) worst case. O(logn) best case
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Difficulty: Easy

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:                
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:  # edge case with 0 nodes in tree
            return None
        
        if root.right is None and root.left is None:  # at a leaf node
            return root
        
        # else
        temp_left_node = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp_left_node
        
        return root
