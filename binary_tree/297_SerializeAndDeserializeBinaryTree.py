# Serialize and Deserialize Binary Tree
# Time: O(n). n is number of nodes in tree
# Space: O(n). need to store preorder list
# Topics: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
# Difficulty: Hard

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Codec:
    def preorder(self, node, preorder_list):
        if node is None:
            preorder_list.append('#')
            preorder_list.append(',')
            return
        
        preorder_list.append(str(node.val))
        preorder_list.append(',')
        self.preorder(node.left, preorder_list)
        self.preorder(node.right, preorder_list)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder_list = []
        self.preorder(root, preorder_list)
        preorder_list.pop()  # remove the last unnecessary delimiter
        return "".join(preorder_list)
    
    def decode_preorder(self, preorder_list):
        if self.preorder_idx >= len(preorder_list):
            return None
        
        curr_string = preorder_list[self.preorder_idx]
        self.preorder_idx += 1
        if curr_string == '#':
            return None
        
        node = TreeNode(int(curr_string))
        node.left = self.decode_preorder(preorder_list)
        node.right = self.decode_preorder(preorder_list)
        
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder_list = data.split(',')
        self.preorder_idx = 0
        root = self.decode_preorder(preorder_list)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))