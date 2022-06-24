# K Closest Points to the Origin
# Time: O(n + klogn)
# Space: O(n)
# Topics: Array, Math, Divide and Conquer, Geometry, Sorting, Heap, Quickselect
# Difficulty: Medium
# Notes: To build a heap given a list of values already is O(n) time.
# Runtime to insert is O(logn). 
# Runtime to delete min is O(logn) as getting the min is O(1) and reheapifying is O(logn). 
# Building a heap by adding elements one by one and heapifying each time is O(nlogn)

from typing import List
import math
import heapq

class Solution:
    def calc_distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return distance
        
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.calc_distance(point, (0, 0)), point) for point in points]
        heapq.heapify(distances)  # O(n) time to build heap from full list. O(nlogn) to build heap if adding one by one and heapify each time
        
        k_closest_origin = []
        for _ in range(k):
            popped = heapq.heappop(distances)  # O(1) to get min. O(logn) to reheapify. O(logn) overall to delete min
            point = popped[1]
            k_closest_origin.append(point)
            
        return k_closest_origin
