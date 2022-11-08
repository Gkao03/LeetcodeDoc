# Pseudo-Palindromic Paths in a Binary Tree
# Time: O(n) where n is number of nodes in the tree.
# Space: O(h) stack space where h is height of tree. O(n) worst case. O(logn) best case.
# Topics: Bit Manipulation, Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Difficulty: Medium

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, curr_set):
        if node.val in curr_set:
            curr_set.remove(node.val)
        else:
            curr_set.add(node.val)
            
        if node.left is None and node.right is None:  # at a leaf node
            if len(curr_set) <= 1:
                self.answer += 1
                
        if node.left is not None:
            self.dfs(node.left, curr_set)
            
        if node.right is not None:
            self.dfs(node.right, curr_set)
            
        # either re-add or re-delete
        if node.val in curr_set:
            curr_set.remove(node.val)
        else:
            curr_set.add(node.val)
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # at least 1 node exists in tree
        self.answer = 0
        odd_set = set()  # contains digits which have odd count along path
        
        self.dfs(root, odd_set)
        return self.answer
