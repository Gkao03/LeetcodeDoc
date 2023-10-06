# Sum Root to Leaf Numbers
# Time: O(n). n is number of nodes in tree
# Space: O(n) stack space worst case. O(logn) stack space best case if balanced tree
# Topics: Tree, Depth-First Search, Binary Tree
# Difficulty: Medium

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, curr_sum):
        if root.left is None and root.right is None:  # at leaf node
            return 10 * curr_sum + root.val

        left_num = self.dfs(root.left, 10 * curr_sum + root.val) if root.left is not None else 0
        right_num = self.dfs(root.right, 10 * curr_sum + root.val) if root.right is not None else 0

        return left_num + right_num

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
