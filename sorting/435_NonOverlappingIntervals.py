# Non-overlapping intervals
# Time: O(nlogn). upperbound by initial sorting
# Space: O(1)
# Topics: Array, Dynamic Programming, Greedy, Sorting
# Difficulty: Medium
# Notes: sort by the end interval and greedily check consecutive
# intervals, if there is overlap increase remove counter and continue.

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # sort by end of interval
        
        num_remove = 0
        curr_idx = 0
        next_idx = 1
        while curr_idx < len(intervals) and next_idx < len(intervals):  # check consecutive intervals
            curr_start, curr_end = intervals[curr_idx]
            next_start, next_end = intervals[next_idx]
            
            if next_start < curr_end:  # remove the next interval
                num_remove += 1
                next_idx += 1
            else:  # no need to remove
                curr_idx = next_idx
                next_idx += 1
                
        return num_remove
