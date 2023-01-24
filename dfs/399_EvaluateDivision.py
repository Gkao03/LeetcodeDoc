# Evaluate Division
# Time: O(qn) where n is number of equations and q is number of queries.
# Space: O(n) to store hash table. O(n) for dfs.
# Topics: Array, Depth-First Search, Breadth-First Search, Union Find, Graph, Shortest Path
# Difficulty: Medium

from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, src, target, hash_table, visited):
        visited.add(src)

        if src == target:
            return 1

        if src not in hash_table:
            return float("inf")

        for next_target, curr_val in hash_table[src]:
            if next_target not in visited:
                curr_answer = curr_val * self.dfs(next_target, target, hash_table, visited)

                if curr_answer != float("inf") and curr_answer != float("-inf"):
                    return curr_answer

        return float("inf")

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hash_table = defaultdict(lambda: [])  # this is the graph representation ->  a: (b, val)
        all_variables = set()  # set of all variables

        # construct the graph
        for (a, b), val in zip(equations, values):
            hash_table[a].append((b, val))
            hash_table[b].append((a, 1 / val))
            all_variables.add(a)
            all_variables.add(b)

        output = []

        for c, d in queries:
            if c not in all_variables or d not in all_variables:
                output.append(-1.0)
                continue

            answer = self.dfs(c, d, hash_table, set())
            output.append(answer if answer != float("inf") and answer != float("-inf") else -1.0)

        return output
