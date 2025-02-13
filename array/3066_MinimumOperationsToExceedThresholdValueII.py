# Minimum Operations to Exceed Threshold Value II
# Time: O(N + KlogN)
# Space: O(1). create heap in place
# Topics: Array, Heap, Simulation
# Difficulty: Medium

from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_ops = 0
        heapq.heapify(nums)  # O(n)

        while len(nums) >= 2 and nums[0] < k:
            x = heapq.heappop(nums)  # O(logn)
            y = heapq.heappop(nums)  # O(logn)

            heapq.heappush(nums, min(x, y) * 2 + max(x, y))  # O(logn)
            num_ops += 1

        return num_ops
