# Populating Next Right Pointers in Each Node
# Time: O(n) where n is number of nodes in tree
# Space: O(1) if not counting stack space. O(logn) if counting stack space
# Topics: Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Difficulty: Medium

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def helper(self, curr_node, parent_node, from_left):
        if curr_node is None:
            return

        if from_left:  # came from left path
            curr_node.next = parent_node.right
        else:  # came from the right path
            curr_node.next = parent_node.next.left if parent_node.next is not None else None

        if curr_node.left is not None:  # go left
            self.helper(curr_node.left, curr_node, True)

        if curr_node.right is not None:  # go right
            self.helper(curr_node.right, curr_node, False)

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root

        self.helper(root.left, root, True)  # go left
        self.helper(root.right, root, False)  # go right

        return root
