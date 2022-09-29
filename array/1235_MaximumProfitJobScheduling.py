# Maximum Profit in Job Scheduling
# Time: O(nlogn). upper bounded by sort.
# Space: O(n). dp array is length n.
# Topics: Array, Binary Search, Dynamic Programming, Sorting
# Difficulty: Hard
# Notes: sort by start time and work backwards from suffix. 
# index of dp table represents maximum profit obtainable considering
# all jobs of index to the end. Use binary search on the sorted start times
# and the current end time as target to find the next valid interval.

from typing import List
from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        zipped = sorted(zip(startTime, endTime, profit))  # O(nlogn) sort
        startTime, endTime, profit = [x[0] for x in zipped], [x[1] for x in zipped], [x[2] for x in zipped]
        
        max_profit = 0
        dp = [0] * len(profit)
        dp[-1] = profit[-1]
        max_profit = profit[-1]
        
        for i in range(len(startTime) - 2, -1, -1):  # O(n) time
            curr_start, curr_end, curr_profit = startTime[i], endTime[i], profit[i]
            
            search_idx = bisect_left(startTime, curr_end)  # O(logn) binary search
            
            if search_idx >= len(dp):
                dp[i] = max(dp[i + 1], curr_profit)
            else:
                dp[i] = max(dp[i + 1], curr_profit + dp[search_idx])
                
        return dp[0]
