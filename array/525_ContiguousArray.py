# Contiguous Array
# Time: O(n)
# Space: O(n)
# Topics: Array, Hash Table, Prefix Sum
# Difficulty: Medium
# Notes: The idea here is to treat 0's as -1 and 1 as 1.
# then keep a running sum and hash table to see if the
# running sum has been previously met before. The hash
# table keeps track of the sum and the index at which the
# sum was found. If it is found later again, this means that
# the sum from previous to current index is 0 and that is the
# current length contiguous array.

from typing import List
from collections import Counter

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_table = {}  # curr_sum: idx at which sum occured
        hash_table[0] = -1
        max_len = 0
        curr_sum = 0
        
        for i, num in enumerate(nums):
            if num == 1:
                curr_sum += 1
            else:  # num == 0
                curr_sum -= 1
            
            if curr_sum not in hash_table:
                hash_table[curr_sum] = i
            else:  # sum is in hash table
                # this means current idx to previous idx has sum of 0
                max_len = max(max_len, i - hash_table[curr_sum])
        
        return max_len
