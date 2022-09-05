# Path Sum
# Time: O(n). n is number of nodes in tree
# Space: O(h). h is height of tree (stack space)
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
    def dfs(self, node, target, curr_sum, found):
        curr_sum += node.val
        
        # at leaf node
        if node.left is None and node.right is None:
            if curr_sum == target:
                return True
            
        # go left
        if not found and node.left is not None:
            found = self.dfs(node.left, target, curr_sum, found)
            
        # go right
        if not found and node.right is not None:
            found = self.dfs(node.right, target, curr_sum, found)
            
        return found
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        return self.dfs(root, targetSum, 0, False)
