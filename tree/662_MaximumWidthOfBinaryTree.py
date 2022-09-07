# Maximum Width of Binary Tree
# Time: O(n)
# Space: O(n)
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Difficulty: Medium

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()  # stores tuple (curr_node, distance, curr_level)
        
        curr_level = 0
        left_dist = 0
        right_dist = 0
        max_width = 1
        
        if root.left is not None:
            queue.append((root.left, -1, curr_level + 1))
        if root.right is not None:
            queue.append((root.right, 1, curr_level + 1))
        
        while len(queue) > 0:
            curr_node, dist, next_level = queue.popleft()
            
            if next_level > curr_level:
                left_dist = dist
            
            curr_level = next_level
            right_dist = dist
            max_width = max(max_width, (right_dist - left_dist) // 2 + 1)
            
            if curr_node.left is not None:
                queue.append((curr_node.left, 2 * dist - 1, curr_level + 1))
            if curr_node.right is not None:
                queue.append((curr_node.right, 2 * dist + 1, curr_level + 1))
        
        return max_width
