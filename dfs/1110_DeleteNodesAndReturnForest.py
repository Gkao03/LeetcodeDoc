# Delete Nodes and Return Forest
# Time: O(n). n is number of nodes
# Space: O(n + h). n is number of nodes and h is height of tree (stack space)
# Topics: Tree, Depth-First Search, Binary Tree
# Difficulty: Medium

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs_delete(self, curr_node):
        if curr_node.val in self.delete_set:
            if curr_node.left is not None and curr_node.left.val not in self.delete_set:
                self.answer.append(curr_node.left)

            if curr_node.right is not None and curr_node.right.val not in self.delete_set:
                self.answer.append(curr_node.right)

        # continue dfs and check if node should be unlinked (effectively deleted)
        if curr_node.left is not None:
            if self.dfs_delete(curr_node.left):
                curr_node.left = None

        if curr_node.right is not None:
            if self.dfs_delete(curr_node.right):
                curr_node.right = None

        return True if curr_node.val in self.delete_set else False

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []

        self.delete_set = set(to_delete)
        self.answer = []

        # do dfs
        self.dfs_delete(root)

        # final check with root
        if root.val not in self.delete_set:
            self.answer.append(root)

        return self.answer
