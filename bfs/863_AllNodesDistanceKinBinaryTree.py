# All Nodes Distance K in Binary Tree
# Time: O(n)
# Space: O(h). h is the height of tree (stack space). O(n) worst case. O(logn) if balanced
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Difficulty: Medium
# Notes: use DFS until you find the target node. After popping from stack,
# calculate the remaining distance needed and check the opposite branch
# path distance k from target. Do a final dfs from the target for the nodes
# k distance away.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_nodes(self, node, remain_dist):
        if node is None:
            return
        
        if remain_dist == 0:
            self.output.append(node.val)
            return
        
        if node.left is not None:
            self.get_nodes(node.left, remain_dist - 1)
        if node.right is not None:
            self.get_nodes(node.right, remain_dist - 1)
    
    def dfs(self, node, target, curr_depth, k):
        if node.val == target.val:
            self.target_depth = curr_depth
        
        # only continue if not found target
        if self.target_depth is None and node.left is not None:
            self.dfs(node.left, target, curr_depth + 1, k)
        
        # search right after popping from left
        checked = False
        if self.target_depth is not None and node.val != target.val:
            checked = True
            remaining_distance = k - (self.target_depth - curr_depth)
            if remaining_distance == 0:
                self.output.append(node.val)
            elif remaining_distance > 0:
                self.get_nodes(node.right, remaining_distance - 1)
        
        # only continue if not found target
        if self.target_depth is None and node.right is not None:
            self.dfs(node.right, target, curr_depth + 1, k)
        
        # search left after popping from right
        if self.target_depth is not None and node.val != target.val and not checked:
            checked = True
            remaining_distance = k - (self.target_depth - curr_depth)
            if remaining_distance == 0:
                self.output.append(node.val)
            elif remaining_distance > 0:
                self.get_nodes(node.left, remaining_distance - 1)
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.target_depth = None
        self.output = []
        
        self.dfs(root, target, 0, k)
        if k == 0:
            self.output.append(target.val)
        else:
            self.get_nodes(target.left, k - 1)
            self.get_nodes(target.right, k - 1)
        return self.output
