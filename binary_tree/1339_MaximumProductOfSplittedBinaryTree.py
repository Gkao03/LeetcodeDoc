# Maximum Product of Splitted Binary Tree
# Time: O(n)
# Space: O(h) stack space where h is height of tree. O(n) worst case. O(logn) best case.
# Topics: Tree, Depth-First Search, Binary Tree
# Difficulty: Medium
# Notes: we return the answer modulo 10 ** 9 + 7 since the answer may be too large

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs_max_product(self, node):
        if node.left is None and node.right is None:  # leaf node
            return node.val
        
        sub_left_sum = 0
        if node.left is not None:
            sub_left_sum = self.dfs_max_product(node.left)
            self.max_product = max(self.max_product, (self.total_sum - sub_left_sum) * sub_left_sum)
        
        sub_right_sum = 0
        if node.right is not None:
            sub_right_sum = self.dfs_max_product(node.right)
            self.max_product = max(self.max_product, (self.total_sum - sub_right_sum) * sub_right_sum)
            
        return sub_left_sum + sub_right_sum + node.val
    
    def get_total_sum(self, node):
        self.total_sum += node.val
        
        if node.left is not None:
            self.get_total_sum(node.left)
            
        if node.right is not None:
            self.get_total_sum(node.right)
        
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # at least 2 nodes exist in tree
        self.total_sum = 0
        self.get_total_sum(root)
        
        self.max_product = float("-inf")
        self.dfs_max_product(root)
        
        return self.max_product % (10 ** 9 + 7)
