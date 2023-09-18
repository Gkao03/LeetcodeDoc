# The K Weakest Rows in a Matrix
# Time: O(nlogk). n total rows and k weakest rows.
# Space: O(k) to store k row indices.
# Topics: Array, Binary Search, Sorting, Heap, Matrix
# Difficulty: Easy

from typing import List
import heapq

class Wrapper:
    def __init__(self, neg_num_soldiers, index):
        self.neg_num_soldiers = neg_num_soldiers
        self.index = index

    def __lt__(self, wrapper):
        if self.neg_num_soldiers < wrapper.neg_num_soldiers:
            return True
        elif self.neg_num_soldiers == wrapper.neg_num_soldiers:
            return self.index > wrapper.index
        return False


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_heap = []

        for i, row in enumerate(mat):  # O(n)
            num_soldiers = sum(row)

            if len(max_heap) < k:
                heapq.heappush(max_heap, Wrapper(-num_soldiers, i))  # O(logk)
            elif num_soldiers < -max_heap[0].neg_num_soldiers:  # get largest soldier count from heap
                heapq.heappop(max_heap)  # O(logk)
                heapq.heappush(max_heap, Wrapper(-num_soldiers, i))  # O(logk)

        k_weakest_rows = []
        while len(max_heap) > 0:  # O(k)
            k_weakest_rows.append(heapq.heappop(max_heap).index)  # O(logk)

        return reversed(k_weakest_rows)
