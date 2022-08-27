# Task Scheduler
# Time: O(n)
# Space: O(1)
# Topics: Array, Hash Table, Greedy, Sorting, Heap, Counting
# Difficulty: Medium
# Notes: Since the tasks are constrained to upper-case English letters, this means there are
# at most 26 unique tasks. Because of this, many operations that would take greater than O(1)
# space or time would now take O(1) time. For example, heap push and pop would be a O(logn)
# operation to maintain the heap invariant, but since there are at most 26 elements in the heap,
# each push and pop is O(1). Similarly, counting the tasks takes O(n) time but takes O(1) space.

from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts_dict = Counter(tasks)  # O(n) time. O(1) space
        heap1 = [-count for count in counts_dict.values()]  # O(1) space
        heapq.heapify(heap1)  # O(1) time
        queue = deque()  # (count, idle_time)  O(1) space
        
        timer = 0
        while len(heap1) > 0 or len(queue) > 0:
            if len(heap1) > 0:  # schedule it in
                count = heapq.heappop(heap1)
                if count + 1 < 0:
                    queue.append((count + 1, timer + n))  # push (new_time, idle_time)
            
            if len(queue) > 0:  # this task can be scheduled in the future. push to heap1
                pop_count, pop_time = queue[0]
                if pop_time == timer:
                    queue.popleft()
                    heapq.heappush(heap1, pop_count)
                    
            timer += 1
            
        return timer
