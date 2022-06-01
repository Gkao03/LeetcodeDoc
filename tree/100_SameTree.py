# Same Tree
# Time: O(min(n, m)). n is # of nodes in p. m is # of nodes in q
# Space: O(1)
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
    def helper(self, curr_p, curr_q, curr_same):
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
        
        curr_same = self.helper(curr_p.left, curr_q.left, curr_same) and curr_same
        curr_same = self.helper(curr_p.right, curr_q.right, curr_same) and curr_same
        
        return curr_same
    
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same = self.helper(p, q, True)
        return is_same
