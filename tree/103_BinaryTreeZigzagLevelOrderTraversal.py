# Binary Tree ZigZag Level Order Traversal
# Time: O(n). n is number of nodes in tree
# Space: O(n)
# Topics: Tree, Breadth-First Search, Binary Tree
# Difficulty: Medium

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        output = []
        curr_output = []
        queue = deque()
        queue.append((root, 0))  # stores tuple: (node, current level)
        curr_level = 0  # even is right to left. odd is left to right
        
        while len(queue) > 0:
            next_node, next_level = queue.popleft()
                
            if next_level > curr_level:
                output.append(curr_output[::-1] if next_level % 2 == 0 else curr_output)
                curr_output = []
                
            curr_level = next_level
            curr_output.append(next_node.val)
            
            if next_node.left is not None:
                queue.append((next_node.left, curr_level + 1))
            if next_node.right is not None:
                queue.append((next_node.right, curr_level + 1))
                    
        output.append(curr_output[::-1] if curr_level % 2 == 1 else curr_output)
        return output
