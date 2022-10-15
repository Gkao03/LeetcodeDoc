# Bus Routes
# Time: O(N^2). N is number of buses
# Space: O(N^2)
# Topics: Array, Hash Table, Breadth-First Search
# Difficulty: Hard

from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # create graph
        # {curr_bus_stop: [list[route ints]]}
        adj_list = defaultdict(lambda: [])
        for route_num, route in enumerate(routes):
            for bus_stop in route:
                adj_list[bus_stop].append(route_num)
        
        visited_routes = set()  # should not visit routes already checked
        queue = deque()
        queue.append(source)
        
        least_buses = 0
        while len(queue) > 0:
            curr_queue_size = len(queue)
            least_buses += 1
            
            for _ in range(curr_queue_size):
                curr_bus = queue.popleft()
                for next_route_num in adj_list[curr_bus]:
                    if next_route_num in visited_routes:
                        continue

                    visited_routes.add(next_route_num)

                    for next_bus_stop in routes[next_route_num]:
                        if next_bus_stop == target:
                            return least_buses
                        queue.append(next_bus_stop)
                
        return -1
