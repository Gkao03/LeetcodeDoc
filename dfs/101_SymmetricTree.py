# Symmetric Tree
# Time: O(n)
# Space: O(1). O(h) if you count stack space where h is maximum height of tree
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Notes: Can be done iteratively using a Queue. This is also an extension of "Same Tree" problem.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def same_tree(self, curr_p, curr_q, curr_same):
        if not curr_same:
            return False
        
        if curr_p is None and curr_q is None:
            return True
        
        if curr_p is not None and curr_q is None:
            return False
        
        if curr_p is None and curr_q is not None:
            return False
        
        # curr_p and curr_q are not None
        if curr_p.val != curr_q.val:
            return False
        
        curr_same = self.same_tree(curr_p.left, curr_q.right, curr_same) and curr_same
        curr_same = self.same_tree(curr_p.right, curr_q.left, curr_same) and curr_same
        
        return curr_same
        
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        is_sym = self.same_tree(root, root, True)
        return is_sym
