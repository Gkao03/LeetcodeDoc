# Construct Binary Tree from Preorder and Postorder Traversal
# Time: O(n). n is number of nodes in tree.
# Space: O(h) where h is height of tree. O(n) if not balanced. O(logn) if balanced
# Topics: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
# Difficulty: Medium

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, preorder, postorder):
        new_node = TreeNode(preorder[self.preorder_idx])
        self.preorder_idx += 1

        if new_node.val == postorder[self.postorder_idx]:
            self.postorder_idx += 1
            return new_node
            
        new_node.left = self.helper(preorder, postorder)

        if new_node.val != postorder[self.postorder_idx]:
            new_node.right = self.helper(preorder, postorder)

        if new_node.val == postorder[self.postorder_idx]:
            self.postorder_idx += 1

        return new_node

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # initialize some index trackers
        self.preorder_idx = 0
        self.postorder_idx = 0

        root = self.helper(preorder, postorder)
        return root
