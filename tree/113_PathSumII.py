# Path Sum II
# Time: O(n). n is number of nodes in tree
# Space: O(nlogn) with O(h) stack space
# Topics: Backtracking, Tree, Depth-First Search, Binary Tree
# Difficulty: Medium
# Notes: for a balanced tree, there will be O(2^logn)=O(n) leaf nodes.
# If all leaf nodes end at a valid path, each path length will be O(logn).
# Therefore it can take O(nlogn) space to store the output solution. The
# stack space used is the height of the tree in the general case O(h).

from typing import Optional, List
import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node, target, curr_sum, curr_output, output):
        curr_sum += node.val
        curr_output.append(node.val)
        
        # at a leaf node
        if node.left is None and node.right is None:
            if curr_sum == target:
                output.append(copy.deepcopy(curr_output))
                
        # go left
        if node.left is not None:
            self.dfs(node.left, target, curr_sum, curr_output, output)
        
        # go right
        if node.right is not None:
            self.dfs(node.right, target, curr_sum, curr_output, output)
        
        curr_output.pop()
        
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        output = []
        self.dfs(root, targetSum, 0, [], output)
        return output
