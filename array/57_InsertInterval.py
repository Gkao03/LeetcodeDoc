# Insert Interval
# Time: O(n)
# Space: O(n)
# Topics: Array
# Difficulty: Medium
# Notes: lots of check conditionals

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        new_start, new_end = newInterval
        insert_idx = 0
        
        for i, (start, end) in enumerate(intervals):  # find where to insert based off new start
            if i == 0 and new_start < start:  # insert at 0 idx
                break
                
            if i == len(intervals) - 1:
                insert_idx = len(intervals)
                break
                
            next_start, next_end = intervals[i + 1]
                
            if new_start >= start and new_start < next_start:
                insert_idx = i + 1
                break
                
        new_intervals = None
        
        if insert_idx == len(intervals):
            start, end = intervals[-1]
            if new_start <= end:  # overlap
                merge_interval = [start, max(new_end, end)]
                new_intervals = intervals[:-1] + [merge_interval]
            else:  # no overlap
                new_intervals = intervals + [newInterval]
        elif insert_idx == 0:
            merge_idx = insert_idx
            for i in range(merge_idx, len(intervals) - 1):
                check_start, check_end = intervals[i]
                check_next_start, check_next_end = intervals[i+1]

                if new_end < check_start:
                    break

                if new_end >= check_start and new_end < check_next_start:
                    merge_idx = i
                    break

                if i == len(intervals) - 2:
                    merge_idx = i + 1

            check_start, check_end = intervals[merge_idx]

            if new_end < check_start:  # no overlap with right side
                new_intervals = [newInterval] + intervals
            else:
                merge_end = max(check_end, new_end)
                new_intervals = [[new_start, merge_end]] + intervals[merge_idx+1:]
        else:  # insert somewhere in middle. at least 2 intervals exist
            merge_start = new_start
            merge_idx = insert_idx
            prev_start, prev_end = intervals[insert_idx-1]
            
            if prev_end >= new_start:  # check if left side needs to be merged
                merge_start = prev_start
                insert_idx = insert_idx - 1
                
            for i in range(merge_idx, len(intervals) - 1):
                check_start, check_end = intervals[i]
                check_next_start, check_next_end = intervals[i+1]

                if new_end < check_start:
                    break

                if new_end >= check_start and new_end < check_next_start:
                    merge_idx = i
                    break

                if i == len(intervals) - 2:
                    merge_idx = i + 1

            check_start, check_end = intervals[merge_idx]

            if new_end < check_start:  # no overlap with right side
                merge_end = max(prev_end, new_end)
                new_intervals = intervals[:insert_idx] + [[merge_start, merge_end]] + intervals[merge_idx:]
            else:
                merge_end = max(check_end, new_end)
                new_intervals = intervals[:insert_idx] + [[merge_start, merge_end]] + intervals[merge_idx+1:]
                    
        return new_intervals
