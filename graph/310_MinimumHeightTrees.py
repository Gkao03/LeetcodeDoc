# Minimum Height Trees
# Time: O(n)
# Space: O(n)
# Topics: Depth-First Search, Breadth-First Search, Graph, Topological Sort
# Difficulty: Medium
# Notes: The given input is guaranteed to be a tree and there will be no repeated edges.
# Trees guaranteed to not have cycle so Topological sort can be done. Graphs can have
# at most 2 MHTs. Also make sure to consider edge cases!

from collections import defaultdict
from typing import List

class Solution:
    def find_MHT_root(self, start_node, target_height, adj_list, n):
        unvisited_set = set([i for i in range(n)])
        curr_height = 0
        stack = []
        stack.append((0, start_node))
        unvisited_set.remove(start_node)
        result_set = set()
        
        while len(stack) > 0:
            curr_height, curr_node = stack.pop()
            
            if curr_height == target_height and len(adj_list[curr_node]) != 1:  # make sure not a leaf node
                result_set.add(curr_node)
            
            for adj_node in adj_list[curr_node]:
                if adj_node in unvisited_set:
                    stack.append((curr_height + 1, adj_node))
                    unvisited_set.remove(adj_node)
                    
        return result_set
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        if n == 2:
            return [0, 1]
        
        # create graph
        adj_list = defaultdict(lambda: [])
        
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            
        # first find maximum height by doing 2 DFSs
        # first DFS to find a leaf node. Second DFS to find another leaf node
        unvisited_set = set([i for i in range(n)])
        leaf_node1 = unvisited_set.pop()
        deepest_height = 0
        while len(unvisited_set) > 0:  # 1st DFS
            stack = []
            stack.append((0, leaf_node1))  # remove random node from unvisited set
            
            while len(stack) > 0:
                curr_height, curr_node = stack.pop()
                
                if len(adj_list[curr_node]) == 1:  # is a leaf node
                    deepest_height, leaf_node1 = max((curr_height, curr_node), (deepest_height, leaf_node1))
                
                for adj_node in adj_list[curr_node]:
                    if adj_node in unvisited_set:
                        stack.append((curr_height + 1, adj_node))
                        unvisited_set.remove(adj_node)
        
        unvisited_set = set([i for i in range(n)])
        leaf_node2 = leaf_node1
        max_height = 0
        while len(unvisited_set) > 0:  # 2nd DFS
            stack = []
            stack.append((0, leaf_node1))  # start at leaf node
            unvisited_set.remove(leaf_node1)
            
            while len(stack) > 0:
                curr_height, curr_node = stack.pop()
                max_height, leaf_node2 = max((curr_height, curr_node), (max_height, leaf_node2))
                
                for adj_node in adj_list[curr_node]:
                    if adj_node in unvisited_set:
                        stack.append((curr_height + 1, adj_node))
                        unvisited_set.remove(adj_node)
        
        # find roots (union sets)
        result_set1 = self.find_MHT_root(leaf_node1, max_height // 2, adj_list, n)
        result_set1 = result_set1.union(self.find_MHT_root(leaf_node1, (max_height + 1) // 2, adj_list, n))
        result_set2 = self.find_MHT_root(leaf_node2, max_height // 2, adj_list, n)
        result_set2 = result_set2.union(self.find_MHT_root(leaf_node2, (max_height + 1) // 2, adj_list, n))
        
        output = list(result_set1 & result_set2)
            
        return output
