# Kth Smallest Element in a BST
# Time: O(h + k). h is the height of the BST.
# Space: O(h). Need the space for stack space during recursion.
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
    counter = 0
    
    def inorder_traversal(self, root, k):
        if root is None:
            return None
        
        solution = self.inorder_traversal(root.left, k)
        if solution is not None:
            return solution
        
        self.counter += 1
        if self.counter == k:
            return root.val
        
        solution = self.inorder_traversal(root.right, k)
        
        return solution
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        solution = self.inorder_traversal(root, k)
        return solution
