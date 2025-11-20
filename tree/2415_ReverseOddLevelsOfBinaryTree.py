# Reverse Odd Levels of Binary Tree
# Time: O(n)
# Space: O(logn) since perfect binary tree
# Difficulty: Medium
# Notes: if done by BFS, will use O(n) space to store each level nodes

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node1, node2, curr_depth):
        if curr_depth % 2 == 1:  # swap left and right val if odd
            node1.val, node2.val = node2.val, node1.val

        if node1.left is not None:
            self.dfs(node1.left, node2.right, curr_depth + 1)
            self.dfs(node1.right, node2.left, curr_depth + 1)

    def bfs(self, root):
        queue = deque([root])
        curr_depth = 0
        
        while len(queue) > 0:
            if curr_depth % 2 == 1:  # swap if odd depth
                q_list = list(queue)
                i, j = 0, len(q_list) - 1
                while i < j:
                    node1 = q_list[i]
                    node2 = q_list[j]
                    node1.val, node2.val = node2.val, node1.val

                    i += 1
                    j -= 1
            
            for _ in range(len(queue)): # get next depth nodes
                curr_node = queue.popleft()

                if curr_node.left is not None:
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)

            curr_depth += 1

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left is not None:
            self.dfs(root.left, root.right, 1)

        # if root.left is not None:
        #     self.bfs(root)

        return root
        