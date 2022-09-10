# Subarray Sum Equals K
# Time: O(n)
# Space: O(n)
# Topics: Array, Hash Table, Prefix Sum
# Difficulty: Medium

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = defaultdict(lambda: 0)
        
        answer = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            target = prefix_sum - k
            if target in hash_table:
                answer += hash_table[target]
            if prefix_sum == k:
                answer += 1
                
            hash_table[prefix_sum] += 1
        
        return answer
