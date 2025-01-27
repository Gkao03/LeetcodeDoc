# Network Delay Time
# Time: O(ElogV). E is num edges and V is num nodes.
# Space: O(V)
# Topics: Depth-First Search, Breadth-First Search, Heap, Shortest Path
# Difficulty: Medium

import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # all node designations subtract 1. node n is node n-1
        # init graph
        adj_map = defaultdict(lambda: [])  # source: (weight, target)
        for u, v, w in times:
            adj_map[u - 1].append((w, v - 1))

        min_times = [float("inf")] * n  # init distances
        pq = []  # priority queue
        visited = [False] * n

        # add initial node
        min_times[k - 1] = 0
        heap_item = [0, k - 1]  # [weight, node]
        heapq.heappush(pq, heap_item)

        # dijkstra
        while len(pq) > 0:
            curr_weight, curr_node = heapq.heappop(pq)
            if visited[curr_node]:
                continue

            visited[curr_node] = True

            for adj_weight, adj_node in adj_map[curr_node]:
                if not visited[adj_node] and curr_weight + adj_weight < min_times[adj_node]:
                    min_times[adj_node] = curr_weight + adj_weight
                    heapq.heappush(pq, (curr_weight + adj_weight, adj_node))

        min_time = max(min_times)
        return min_time if min_time != float("inf") else -1
