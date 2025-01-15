# Count Nodes Equal to Average of Subtree
# Time: O(n)
# Space: O(h) stack space. h is height of binary tree. O(n) if unbalanced. O(logn) if balanced.
# Topics: Tree, Depth-First Search, Binary Tree
# Difficulty: Medium

import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root):
        if root.left is None and root.right is None:
            self.answer += 1
            return root.val, 1
        
        sum_left, num_nodes_left = self.dfs(root.left) if root.left is not None else (0, 0)
        sum_right, num_nodes_right = self.dfs(root.right) if root.right is not None else (0, 0)

        average = math.floor((sum_left + sum_right + root.val) / (num_nodes_left + num_nodes_right + 1))
        if average == root.val:
            self.answer += 1

        return sum_left + sum_right + root.val, num_nodes_left + num_nodes_right + 1

    def averageOfSubtree(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 1
        
        self.answer = 0

        sum_left, num_nodes_left = self.dfs(root.left) if root.left is not None else (0, 0)
        sum_right, num_nodes_right = self.dfs(root.right) if root.right is not None else (0, 0)

        average = math.floor((sum_left + sum_right + root.val) / (num_nodes_left + num_nodes_right + 1))
        if average == root.val:
            self.answer += 1

        return self.answer
