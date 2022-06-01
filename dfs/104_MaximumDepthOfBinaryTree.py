# Maximum Depth of Binary Tree
# Time: O(n)
# Space: O(1). O(h) if you count stack space where h is maximum height of tree.
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
    max_depth = 0
    
    def helper(self, node, curr_depth):
        if curr_depth > self.max_depth:
            self.max_depth = curr_depth
            
        if node is None:
            return
        
        self.helper(node.left, curr_depth + 1)
        self.helper(node.right, curr_depth + 1)
        
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0)
        return self.max_depth
