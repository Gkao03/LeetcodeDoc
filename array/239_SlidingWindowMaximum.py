# Sliding Window Maximum
# Time: O(n). we push and pop each element at most 2 times (2n total time)
# Space: O(k)
# Topics: Array, Queue, Sliding Window, Heap, Monotonic Queue
# Difficulty: Hard

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0  # leftmost idx of window
        right = k  # rightmost idx just outside of window
        
        output = []
        queue = deque()  # monotonic decreasing queue (holds indices - elements at indices are decreasing)
        
        # init first window
        for i in range(k):
            while len(queue) > 0 and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            
        output.append(nums[queue[0]])
                
        while right < len(nums):
            # remove left, add right
            if left == queue[0]:
                queue.popleft()
                
            while len(queue) > 0 and nums[right] >= nums[queue[-1]]:
                queue.pop()
            queue.append(right)
            
            output.append(nums[queue[0]])
            left += 1
            right += 1
        
        return output
