# Redundant Connection
# Time: O(V + E) = O(V) since tree + 1 edge (V = E)
# Space: O(V)
# Topics: Depth-First Search, Breadth-First Search, Union Find, Graph
# Difficulty: Medium

from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, curr_node, parent_node, graph, visited, cycle_edges_set):
        visited.add(curr_node)

        is_cycle = False
        for adj_node in graph[curr_node]:
            if adj_node != parent_node and adj_node in visited:  # condition for cycle detected
                cycle_edges_set.add((adj_node, curr_node))
                self.cycle_init_node = adj_node
                return True

            if adj_node != parent_node:
                is_cycle = self.dfs(adj_node, curr_node, graph, visited, cycle_edges_set)

            if is_cycle:
                cycle_edges_set.add((adj_node, curr_node))
                if curr_node == self.cycle_init_node:
                    return False
                return True

        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.cycle_init_node = None
        graph = defaultdict(lambda: [])
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        cycle_edges_set = set()
        self.dfs(1, None, graph, set(), cycle_edges_set)

        answer = None
        for i in range(len(edges) - 1, -1, -1):
            a, b = edges[i]
            if (a, b) in cycle_edges_set or (b, a) in cycle_edges_set:
                answer = [a, b]
                break

        return answer
