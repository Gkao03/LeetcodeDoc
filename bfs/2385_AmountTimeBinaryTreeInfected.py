# Amount of Time for Binary Tree to Be Infected
# Time: O(n)
# Space: O(n)
# Topics: Hash Table, Tree, Depth-first Search, Breadth-first Search, Binary Tree
# Difficulty: Medium

from typing import Optional
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # dfs to convert tree to undirected graph
    def convert_to_undirected_graph(self, curr_node, parent_node, adj_map, start_int):
        start_node = None
        if curr_node.val == start_int:
            start_node = curr_node

        if parent_node is not None:  # case if root node
            adj_map[curr_node.val].append(parent_node)

        if curr_node.left is not None:
            adj_map[curr_node.val].append(curr_node.left)
            ret_left = self.convert_to_undirected_graph(curr_node.left, curr_node, adj_map, start_int)

            if start_node is None:
                start_node = ret_left

        if curr_node.right is not None:
            adj_map[curr_node.val].append(curr_node.right)
            ret_right = self.convert_to_undirected_graph(curr_node.right, curr_node, adj_map, start_int)

            if start_node is None:
                start_node = ret_right

        return start_node

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj_map = defaultdict(list)  # node: [adjacent nodes]

        # convert to undirected graph and also find start infection node
        start_node = self.convert_to_undirected_graph(root, None, adj_map, start)

        # do BFS
        queue = deque([(start_node, 0)])
        visited = set()
        answer = 0

        while len(queue) > 0:
            curr_node, curr_depth = queue.popleft()
            visited.add(curr_node.val)

            for adj_node in adj_map[curr_node.val]:
                if adj_node.val not in visited:
                    queue.append((adj_node, curr_depth + 1))

            answer = curr_depth

        return answer