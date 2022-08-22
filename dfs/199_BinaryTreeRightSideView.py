# Binary Tree Right Side View
# Time: O(n). n is number of nodes in tree
# Space: O(h) where h is height of tree. O(n) if not balanced. O(logn) if balanced
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Difficulty: Medium

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth = -1
    
    def helper(self, node, curr_depth, output):
        if node is None:
            return
        
        if curr_depth > self.max_depth:
            self.max_depth = curr_depth
            output.append(node.val)
            
        self.helper(node.right, curr_depth + 1, output)
        self.helper(node.left, curr_depth + 1, output)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.helper(root, 0, output)
        return output
