# Find Median from Data Stream
# Time: O(logn) per 'addNum'. O(1) per 'findMedian'.
# Space: O(n) for n 'addNum'
# Topics: Two Pointers, Design, Sorting, Heap, Data Stream
# Difficulty: Hard

import heapq

class MedianFinder:
    def __init__(self):
        # always keep both heaps at most 1 length apart
        self.lt_heap = []  # max heap (less than) - simulated as min heap
        self.gt_heap = []  # min heap (greater or equal to)
        
    def addNum(self, num: int) -> None:
        # edge cases for first 2 numbers added to stream
        if len(self.lt_heap) == 0 and len(self.gt_heap) == 0:
            heapq.heappush(self.gt_heap, num)
            return
        
        if len(self.gt_heap) == 1 and len(self.lt_heap) == 0:
            min_val = self.gt_heap[0]
            if num >= min_val:  # move val from gt heap to lt heap
                heapq.heappush(self.lt_heap, -min_val)
                heapq.heappop(self.gt_heap)  # remove from gt heap
                heapq.heappush(self.gt_heap, num)  # push in new num
            else:
                heapq.heappush(self.lt_heap, -num)
            return
        
        # general case        
        if num >= -self.lt_heap[0]:
            if len(self.gt_heap) > len(self.lt_heap):
                if num < self.gt_heap[0]:
                    heapq.heappush(self.lt_heap, -num)
                else:
                    min_gt = heapq.heappop(self.gt_heap)
                    heapq.heappush(self.lt_heap, -min_gt)
                    heapq.heappush(self.gt_heap, num)
            else:
                heapq.heappush(self.gt_heap, num)
        else:
            if len(self.lt_heap) > len(self.gt_heap):
                max_lt = -heapq.heappop(self.lt_heap)
                heapq.heappush(self.gt_heap, max_lt)
            heapq.heappush(self.lt_heap, -num)
            
        return

    def findMedian(self) -> float:  # there will be at least one element when called
        num_elements = len(self.lt_heap) + len(self.gt_heap)
        
        if num_elements == 1:
            return self.gt_heap[0]
        
        if num_elements % 2 == 0:
            return (-self.lt_heap[0] + self.gt_heap[0]) / 2
        
        if len(self.gt_heap) > len(self.lt_heap):
            return self.gt_heap[0]
        
        return -self.lt_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
