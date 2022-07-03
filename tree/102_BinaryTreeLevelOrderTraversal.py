# Binary Tree Level Order Traversal
# Time: O(n) where n is number of nodes in tree
# Space: O(n) where n is number of nodes in tree
# Topics: Tree, Breadth-First Search, Binary Tree
# Difficulty: Medium
# Notes: Level Order = BFS. Use a queue for BFS

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque()
        num_elements = 0
        nodes_by_level = []
        
        prev_level = 0
        queue.append((root, 0))  # tuple (node, level)
        num_elements += 1
        curr_level_nodes = []
        
        while num_elements != 0:
            curr_node, curr_level = queue.popleft()
            num_elements -= 1
            
            if curr_level != prev_level:
                prev_level = curr_level
                nodes_by_level.append(curr_level_nodes)
                curr_level_nodes = []
            curr_level_nodes.append(curr_node.val)
            
            # add children
            if curr_node.left is not None:
                queue.append((curr_node.left, curr_level + 1))
                num_elements += 1
            if curr_node.right is not None:
                queue.append((curr_node.right, curr_level + 1))
                num_elements += 1
        
        # add final level (should always have at least one node remaining)
        nodes_by_level.append(curr_level_nodes)
        
        return nodes_by_level
