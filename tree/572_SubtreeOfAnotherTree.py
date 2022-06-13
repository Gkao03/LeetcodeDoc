# Subtree of Another Tree
# Time: O(mn) where m is the number of nodes in subRoot tree and n is number of nodes in root tree.
# Space: O(h) stack space where h is height of root tree. O(n) if unbalanced. O(logn) if balanced
# Topics: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function
# Difficulty: Easy
# Notes: this recursive implementation in O(mn) time borrows from the "sameTree" problem done in another
# question. sameTree can be done in linear time and this function is called for each node in the root tree
# which leads to O(mn) time.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_same_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 is None and root2 is not None:
            return False
        
        if root1 is not None and root2 is None:
            return False
        
        if root1.val == root2.val:
            return self.is_same_tree(root1.left, root2.left) and self.is_same_tree(root1.right, root2.right)
        
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        same_tree_found = self.is_same_tree(root, subRoot)
        
        if not same_tree_found and root is not None:
            same_tree_found = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
        return same_tree_found


# Subtree of Another Tree
# Time: O(m+n) where m is the number of nodes in subRoot and n is the number of nodes in root tree.
# Space: O(m+n). Stores traversal order
# Topics: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function
# Difficulty: Easy
# Notes: we use the idea that a tree can be uniquely identified given it's inorder and either it's preorder/postorder
# traversal order. It is important to include "None" type as unique node identifier. Given this, we can borrow from our
# previous implementation of "strStr" problem which we know can be done in linear time. We compare the inorder traversals
# of both trees using strStr and preorder/postorder traversal of both trees using strStr. If there is a match found in both
# traversals, subRoot is a subtree of root. This can reduce the time complexity down to linear.

class Solution2:
    def inorder(self, root, nodes):
        if root is None:
            nodes.append(None)
            return nodes
        
        nodes = self.inorder(root.left, nodes)
        nodes.append(root.val)
        nodes = self.inorder(root.right, nodes)
        
        return nodes
    
    def preorder(self, root, nodes):
        if root is None:
            nodes.append(None)
            return nodes
        
        nodes.append(root.val)
        nodes = self.preorder(root.left, nodes)
        nodes = self.preorder(root.right, nodes)
        
        return nodes
    
    def calc_lps(self, pattern):  # O(pattern) to construct
        if len(pattern) == 1:
            return [0]
        
        lps = [0] * len(pattern)  # longest proper prefix that is also a suffix
        i = 0
        j = 1
        
        while j < len(pattern):
            if pattern[j] == pattern[i]:
                lps[j] = i + 1
                i += 1
                j += 1
            elif pattern[j] != pattern[i] and i != 0:
                i = lps[i-1]
            else:
                lps[j] = 0
                j += 1
                
        return lps
    
    def find_subtree(self, haystack, needle, lps):  # very similar to strStr implementation
        h_idx = 0
        n_idx = 0
        
        while h_idx < len(haystack):
            if haystack[h_idx] == needle[n_idx]:
                n_idx += 1
                h_idx += 1
            elif haystack[h_idx] != needle[n_idx] and n_idx != 0:
                n_idx = lps[n_idx - 1]
            elif haystack[h_idx] != needle[n_idx] and n_idx == 0:
                h_idx += 1
                
            # found condition
            if n_idx >= len(needle):
                return True
            
        return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # guaranteed to have at least one node in both trees
        root_inorder = self.inorder(root, [])
        root_preorder = self.preorder(root, [])
        subroot_inorder = self.inorder(subRoot, [])
        subroot_preorder = self.preorder(subRoot, [])
        
        if len(subroot_inorder) > len(root_inorder):
            return False
        
        lps_inorder = self.calc_lps(subroot_inorder)
        lps_preorder = self.calc_lps(subroot_preorder)
        
        found_inorder = self.find_subtree(root_inorder, subroot_inorder, lps_inorder)
        found_preorder = self.find_subtree(root_preorder, subroot_preorder, lps_preorder)
        
        return found_inorder and found_preorder
