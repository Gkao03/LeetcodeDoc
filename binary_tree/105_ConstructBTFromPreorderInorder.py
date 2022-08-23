# Construct Binary Tree from Preorder and Inorder Traversal
# Time: O(n). n is number of nodes in tree
# Space: O(n). O(n) space to store hash map and O(n) space for stack recursion
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
    curr_pidx = 1
    
    def helper(self, left_idx, right_idx, preorder):
        if self.curr_pidx >= len(preorder):
            return None
        
        if left_idx > right_idx:
            return None
        
        mid_inorder_idx, mid_node = self.node_map[preorder[self.curr_pidx]]
        self.curr_pidx += 1
        
        mid_node.left = self.helper(left_idx, mid_inorder_idx - 1, preorder)
        mid_node.right = self.helper(mid_inorder_idx + 1, right_idx, preorder)
        
        return mid_node
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.node_map = {}
        
        for i, val in enumerate(inorder):
            self.node_map[val] = (i, TreeNode(val))
            
        pre_val = preorder[0]
        start_idx, root = self.node_map[pre_val]
        
        root.left = self.helper(0, start_idx - 1, preorder)
        root.right = self.helper(start_idx + 1, len(inorder) - 1, preorder)
        return root
