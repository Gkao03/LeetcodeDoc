# Cheapest Flights Within K Stops
# Time: O(E + VlogV). E is number of edges. V is number of vertices (cities)
# Space: O(E + V)
# Topics: Dynamic Programming, Depth-First Search, Breadth-First Search, Graph, Heap, Shortest Path
# Difficulty: Medium
# Notes: the worst case for time and space is O(V^2) if fully connected graph.

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(lambda: [])
        for frm, to, price, in flights:
            adj_list[frm].append((price, to))
            
        heap = [(0, 0, src)]  # (running cost, depth, curr city)
        visited = [float("inf")] * n
        
        while len(heap) > 0:
            running_cost, curr_depth, curr_city = heapq.heappop(heap)
            if visited[curr_city] <= curr_depth:  # the current path is longer than a previously found path (for depth)
                continue
                
            visited[curr_city] = curr_depth
            if curr_city == dst:
                return running_cost
                
            if curr_depth <= k:  # curr_depth + 1 <= k + 1
                for price, to in adj_list[curr_city]:
                    heapq.heappush(heap, (running_cost + price, curr_depth + 1, to))
                    
        return -1
