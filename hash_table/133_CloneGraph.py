# Clone Graph
# Time: O(N+M). N is number of nodes, M is number of edges. O(N^2) worst case if fully connected => n(n-1)/2 edges
# Space: O(N+M). N is number of nodes, M is number of edges. O(N^2) worst case if fully connected => n(n-1)/2 edges
# Topics: Hash Table, Depth-First Search, Breadth-First Search, Graph
# Difficulty: Medium
# Notes: add node to visited hash map before actually visiting to avoid overwriting previously copied nodes


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None
        
        stack = [node]  # stack for DFS. can also use queue for BFS
        copy_node = Node(node.val, [])  # will be appending to empty list in traversal
        copy_stack = [copy_node]
        visited = {copy_node.val: copy_node}  # map to existing nodes in copied graph
        
        while len(stack) != 0:
            curr_node = stack.pop()
            curr_copy_node = copy_stack.pop()
            
            for adj_node in curr_node.neighbors:
                if adj_node.val not in visited:
                    stack.append(adj_node)
                    temp_node = Node(adj_node.val, [])
                    copy_stack.append(temp_node)
                    visited[temp_node.val] = temp_node
                else:
                    temp_node = visited[adj_node.val]
                    
                curr_copy_node.neighbors.append(temp_node)
        
        return copy_node
