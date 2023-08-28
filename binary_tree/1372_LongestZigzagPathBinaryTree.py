# Longest ZigZag Path in a Binary Tree
# Time: O(n)
# Space: O(h) stack space. h is height of tree. O(n) worst case. O(logn) best case
# Topics: Dynamic Programming, Tree, Depth-First Search, Binary Tree
# Difficulty: Medium

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recurse(self, root):
        if root is None:
            return -1, -1, -1

        left = self.recurse(root.left)
        right = self.recurse(root.right)

        return left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root)[2]
