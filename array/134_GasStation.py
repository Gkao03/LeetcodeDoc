# Gas Station
# Time: O(n)
# Space: O(1)
# Topics: Array, Greedy
# Difficulty: Medium
# Notes: for this problem, if there exists a problem, it is guaranteed to be unique

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        rest_gas = 0
        start = 0
        
        for i, (g, c) in enumerate(zip(gas, cost)):
            new_gas = g - c
            
            total_gas += new_gas
            rest_gas += new_gas
            
            if rest_gas < 0:
                start = i + 1
                rest_gas = 0
                
        start = -1 if total_gas < 0 else start
        return start
