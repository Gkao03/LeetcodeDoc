# Merge Intervals
# Time: O(n)
# Space: O(n) to store solution
# Topics: Array, Sorting
# Difficulty: Medium

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start first
        intervals.sort(key = lambda x: x[0])
        merged_intervals = []
        
        interval_idx = 0
        while interval_idx < len(intervals):
            curr_start, curr_end = intervals[interval_idx]
            
            search_idx = interval_idx
            while search_idx < len(intervals):
                search_start, search_end = intervals[search_idx]
                if curr_end < search_start:
                    break
                
                curr_end = max(curr_end, search_end)
                search_idx += 1
                    
            interval_idx = search_idx
            merged_intervals.append([curr_start, curr_end])
        
        return merged_intervals
