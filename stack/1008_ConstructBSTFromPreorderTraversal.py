# Construct Binary Search Tree from Preorder Traversal
# Time: O(n). n is number of nodes in tree
# Space: O(h). h is height of tree. O(n) if unbalanced. O(logn) if balanced
# Topics: Array, Stack, Tree, Binary Search Tree, Monotonic Stack, Binary Tree
# Difficulty: Medium

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        stack = [root]
        prev_node = root
        
        for i in range(1, len(preorder)):
            curr_val = preorder[i]
            new_node = TreeNode(curr_val)

            if len(stack) == 0 or curr_val < stack[-1].val:
                prev_node.left = new_node
                stack.append(new_node)
                prev_node = new_node
                continue

            while len(stack) > 0 and curr_val > stack[-1].val:
                popped_node = stack.pop()

            popped_node.right = new_node
            stack.append(new_node)
            prev_node = new_node

        return root
