# Lowest Common Ancestor of a Binary Search Tree
# Time: O(h) where h is the height of the BST. O(n) worst case if unbalanced. O(logn) best case if balanced.
# Space: O(h) where h is the height of the BST (stack space). O(n) worst case. O(logn) best case.
# Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Difficulty: Easy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # there will be at least 2 nodes in the tree. p != q guaranteed. p and q will exist
        # all values are unique in BST
        
        if root.val == p.val:
            return p
        
        if root.val == q.val:
            return q
        
        # current root is less than both p and q. LCA must be somewhere in right path
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # current root is greater than both p and q. LCA must be somewhere in left path
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # current root is between p and q
        return root
