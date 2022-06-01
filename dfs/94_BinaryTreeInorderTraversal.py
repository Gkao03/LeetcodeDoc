# Binary Tree Inorder Traversal
# Time: O(n)
# Space: O(n)
# Topics: Stack, Tree, Depth-First Search, Binary Tree
# Difficulty: Easy
# Notes: Use a stack to do it iteratively instead of recursively

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ====== ITERATIVE SOLUTION ======
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr_node = root
        inorder_values = []
        
        while True:
            if curr_node is not None:
                stack.append(curr_node)
                curr_node = curr_node.left
            elif len(stack) != 0:
                curr_node = stack.pop()
                inorder_values.append(curr_node.val)
                curr_node = curr_node.right
            else:
                break
        
        return inorder_values


# ====== RECURSIVE SOLUTION ======
class Solution2:
    def helper(self, node, values) -> List[int]:
        if node is None:
            return values
        
        # go left
        values = self.helper(node.left, values)
        
        # append at current node
        values.append(node.val)
        
        # go right
        values = self.helper(node.right, values)
        
        return values
    
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_values = self.helper(root, [])
        return inorder_values
