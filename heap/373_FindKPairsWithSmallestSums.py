# Find K Pairs with Smallest Sums
# Time: O(klogk)
# Space: O(k)
# Topics: Array, Heap
# Difficulty: Medium

from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # nums1 and nums2 sorted in non decreasing order
        answer = []
        min_heap = []

        for i in range(min(k, len(nums1))):  # O(k)
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # tuple: (sum, idx1, idx2)

        for _ in range(k):  # O(k)
            curr_sum, idx1, idx2 = heapq.heappop(min_heap)  # O(logk)
            answer.append([nums1[idx1], nums2[idx2]])

            if idx2 + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))

        return answer
