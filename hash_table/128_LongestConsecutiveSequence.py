# Longest Consecutive Sequence
# Time: O(n)
# Space: O(n)
# Topics: Array, Hash Table, Union Find
# Difficulty: Medium

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}  # stores key int: (curr_longest_len, min_val, max_val)
        max_len = 0
        
        # only need to update integers that are consecutive
        for num in nums:
            if num not in hash_map:
                if num + 1 in hash_map and num - 1 in hash_map:
                    left_longest, left_min, left_max = hash_map[num - 1]
                    right_longest, right_min, right_max = hash_map[num + 1]
                    curr_longest = left_longest + right_longest + 1
                    
                    # update values for left and right ints in the current sequence
                    hash_map[left_min] = (curr_longest, left_min, right_max)
                    hash_map[right_max] = (curr_longest, left_min, right_max)
                    hash_map[num] = (curr_longest, left_min, right_max)
                elif num - 1 in hash_map:
                    left_longest, left_min, left_max = hash_map[num - 1]
                    curr_longest = left_longest + 1
                    
                    # update
                    hash_map[left_min] = (curr_longest, left_min, num)
                    hash_map[num] = (curr_longest, left_min, num)
                elif num + 1 in hash_map:
                    right_longest, right_min, right_max = hash_map[num + 1]
                    curr_longest = right_longest + 1
                    
                    # update
                    hash_map[right_max] = (curr_longest, num, right_max)
                    hash_map[num] = (curr_longest, num, right_max)
                else:  # not in hash map -> just insert
                    curr_longest = 1
                    hash_map[num] = (1, num, num)
                    
                max_len = max(max_len, curr_longest)
        
        return max_len
