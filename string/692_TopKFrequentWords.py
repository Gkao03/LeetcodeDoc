# Top K Frequent Words
# Time: O(nlogk). n is length of words list. k is k most frequent strings.
# Space: O(n)
# Topics: Hash Table, String, Trie, Sorting, Heap, Bucket Sort, Counting
# Difficulty: Medium

from typing import List
from collections import Counter
import heapq

class Solution:
    class Wrapper:
        def __init__(self, string, count):
            self.string = string
            self.count = count
            
        def __lt__(self, wrapper):
            if self.count == wrapper.count:
                return self.string > wrapper.string
            return self.count < wrapper.count
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)  # dictionary O(n) space -> string: count
        min_heap = []  # O(k) space
        
        # O(n) for loop. O(logk) heap push and pop.
        for string, count in counts.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, self.Wrapper(string, count))
            else:
                peeked = min_heap[0]
                if count > peeked.count or (count == peeked.count and string < peeked.string):
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, self.Wrapper(string, count))
                    
        output = []
        while len(min_heap) > 0:
            popped = heapq.heappop(min_heap)
            output.append(popped.string)
        output.reverse()
            
        return output
