# Minimum Time to Collect All Apples in a Tree
# Time: O(n)
# Space: O(n)
# Topics: Hash Table, Tree, Depth-First Search, Breadth-First Search
# Difficulty: Medium

from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, curr_node):
        self.visited[curr_node] = True
        child_has_apple = False

        for adj_node in self.hash_table[curr_node]:
            if not self.visited[adj_node]:
                found_apple = self.dfs(adj_node)
                if found_apple:
                    child_has_apple = True
                    self.answer += 2

        return self.has_apple[curr_node] or child_has_apple

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.has_apple = hasApple
        self.answer = 0
        self.visited = [False] * n
        self.hash_table = defaultdict(lambda: [])

        # create adjacency list in hash table
        for a, b in edges:
            self.hash_table[a].append(b)
            self.hash_table[b].append(a)

        # do dfs
        self.dfs(0)

        return self.answer
