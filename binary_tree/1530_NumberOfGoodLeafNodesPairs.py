# Number of Good Leaf Nodes Pairs
# Time: O(nd^2). n is number of nodes in tree. d is distance.
# Space: O(nd). n is number of nodes in tree. d is distance.
# Topics: Tree, Depth-First Search, Binary Tree
# Difficulty: Medium
# Notes: while d is an input parameter, since the constraint d << n,
# we can make an assumption that d is a constant. Then the runtime
# and space can be simplified to O(n).

import copy, itertools
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, curr_node, hashmap):
        if curr_node.left is None and curr_node.right is None:
            new_hashmap = [0] * (self.distance + 1)
            new_hashmap[1] = 1
            return new_hashmap

        left_hashmap = [0] * (self.distance + 1)
        if curr_node.left is not None:
            new_hashmap = copy.deepcopy(hashmap)

            # shift
            new_hashmap[1:] = new_hashmap[:-1]
            new_hashmap[0] = 0

            # call left
            left_hashmap = self.dfs(curr_node.left, new_hashmap)

        right_hashmap = [0] * (self.distance + 1)
        if curr_node.right is not None:
            new_hashmap = copy.deepcopy(hashmap)

            # shift
            new_hashmap[1:] = new_hashmap[:-1]
            new_hashmap[0] = 0

            # call right
            right_hashmap = self.dfs(curr_node.right, new_hashmap)

        # update answer
        for dist in range(1, self.distance):
            right_sum = sum(right_hashmap[:self.distance - dist + 1])
            self.answer += left_hashmap[dist] * right_sum

        merged_hashmap = [0] * (self.distance + 1)
        for dist in range(self.distance, 0, -1):
            merged_hashmap[dist] = left_hashmap[dist - 1] + right_hashmap[dist - 1]

        return merged_hashmap

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.distance = distance
        self.answer = 0
        self.dfs(root, [0] * (distance + 1))

        return self.answer
