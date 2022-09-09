# Find K Closest Elements
# Time: O(logn + k)
# Space: O(k)
# Topics: Array, Two Pointers, Binary Search, Sorting, Heap
# Difficulty: Medium

from typing import List
from bisect import bisect_left
import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)  # O(logn)
        if idx >= len(arr) or (idx - 1 >= 0 and abs(arr[idx - 1] - x) <= abs(arr[idx] - x)):
            idx -= 1
                
        left_idx = idx - 1
        right_idx = idx + 1
        
        for _ in range(k - 1):
            if left_idx < 0:
                right_idx += 1
                continue
            if right_idx >= len(arr):
                left_idx -= 1
                continue
            
            dist_left = abs(arr[left_idx] - x)
            dist_right = abs(arr[right_idx] - x)
            
            if dist_left < dist_right:
                left_idx -= 1
            elif dist_right < dist_left:
                right_idx += 1
            else:  # dist_left == dist_right
                left_idx -= 1
        
        left_idx += 1
        right_idx -= 1
        output = []
        while left_idx <= right_idx:
            output.append(arr[left_idx])
            left_idx += 1
            
        return output


# Find K Closest Elements
# Time: O(logn + klogk)
# Space: O(k)
# Topics: Array, Two Pointers, Binary Search, Sorting, Heap
# Difficulty: Medium

class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)  # O(logn)
        heap = []
        
        # add k elements to the right to heap
        for i in range(k):
            if idx + i >= len(arr):
                break
            heapq.heappush(heap, (abs(x - arr[idx + i]), arr[idx + i]))  # O(logk)
            
        # add k elements to the left to heap
        for i in range(1, k + 1):
            if idx - i < 0:
                break
            heapq.heappush(heap, (abs(x - arr[idx - i]), arr[idx - i]))  # O(logk)
            
        output = []
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])
            
        output.sort()  # O(klogk)
        return output
