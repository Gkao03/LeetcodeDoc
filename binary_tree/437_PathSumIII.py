# Path Sum III
# Time: O(n)
# Space: O(n)
# Topics: Tree, Depth-First Search, Binary Search
# Difficulty: Medium
# Notes: the idea is to keep a frequency count of prefix sums of
# the dfs path.

from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, curr_sum, target_sum):
        curr_sum += node.val
        
        check_sum = curr_sum - target_sum
        if check_sum in self.hash_table:
            self.answer += self.hash_table[check_sum]
        self.hash_table[curr_sum] += 1
        
        if node.left is not None:
            self.dfs(node.left, curr_sum, target_sum)
            
        if node.right is not None:
            self.dfs(node.right, curr_sum, target_sum)
            
        self.hash_table[curr_sum] -= 1
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        
        self.answer = 0
        self.hash_table = defaultdict(lambda: 0)
        self.hash_table[0] += 1
        self.dfs(root, 0, targetSum)
        return self.answer
