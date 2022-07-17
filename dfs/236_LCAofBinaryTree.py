# Lowest Common Ancestor of a Binary Tree
# Time: O(n)
# Space: O(n)
# Topics: Tree, Depth-First Search, Binary Tree
# Difficulty: Medium
# Notes: Store path to p and q in separate arrays and compare the arrays.
# Return first matching node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_path_to_node(self, curr_node, target_node, path):
        if curr_node.val == target_node.val:
            path.append(curr_node)
            return True
        
        in_left = self.get_path_to_node(curr_node.left, target_node, path) if curr_node.left is not None else False
        if in_left:
            path.append(curr_node)
            return True
        
        in_right = self.get_path_to_node(curr_node.right, target_node, path) if curr_node.right is not None else False
        if in_right:
            path.append(curr_node)
            return True
        
        return False
        
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # all values in binary tree are guaranteed to be unique. p and q guaranteed to exist
        p_path = []
        self.get_path_to_node(root, p, p_path)
        
        q_path = []
        self.get_path_to_node(root, q, q_path)
        
        min_path_len = min(len(p_path), len(q_path))
        
        p_path = p_path[len(p_path)-min_path_len:]
        q_path = q_path[len(q_path)-min_path_len:]
        
        for p_node, q_node in zip(p_path, q_path):
            if p_node.val == q_node.val:
                return p_node
