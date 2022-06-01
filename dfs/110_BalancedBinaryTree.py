# Balanced Binary Tree
# Time: O(n)
# Space: O(n). stack space
# Topics: Tree, Depth-First Search, Binary Tree
# Difficulty: Easy

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Height:
    def __init__(self):
        self.height = 0

        
class Solution:
    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        lh = Height()
        rh = Height()

        lh.height = self.height(root.left)
        rh.height = self.height(root.right)

        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)

        if abs(lh.height - rh.height) <= 1:
            return l and r
        
        return False
