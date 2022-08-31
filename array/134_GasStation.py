# Gas Station
# Time: O(n)
# Space: O(1)
# Topics: Array, Greedy
# Difficulty: Medium
# Notes: for this problem, if there exists a problem, it is guaranteed to be unique

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start_idx = -1
        
        for i in range(n):
            if gas[i] >= cost[i]:
                start_idx = i
                break
                
        if start_idx == -1:
            return -1
        
        # initialization
        curr_idx = start_idx
        answer_idx = start_idx
        prev_answer_idx = answer_idx
        past_start = False
        
        # do while
        curr_gas_in_car = gas[start_idx] - cost[start_idx]
        curr_idx = (curr_idx + 1) % n
        
        while answer_idx != curr_idx:
            if answer_idx == -1 and gas[curr_idx] >= cost[curr_idx]:
                if start_idx < prev_answer_idx:
                    if curr_idx > prev_answer_idx or curr_idx < start_idx:
                        answer_idx = curr_idx
                        prev_answer_idx = answer_idx
                        past_start = False
                    else:
                        return -1
                elif start_idx > prev_answer_idx:
                    if prev_answer_idx < curr_idx < start_idx:
                        answer_idx = curr_idx
                        prev_answer_idx = answer_idx
                        past_start = False
                    else:
                        return -1
                else:  # start_idx == prev_answer_idx
                    if curr_idx == start_idx:
                        return -1
                    answer_idx = curr_idx if prev_answer_idx != answer_idx else -1
                    if answer_idx == -1:
                        return -1
                    prev_answer_idx = answer_idx
                    past_start = False

            if curr_idx == answer_idx and past_start is True:
                return answer_idx
                
            curr_gas_in_car += gas[curr_idx]
            if curr_gas_in_car < cost[curr_idx]:  # can't make it to next station
                answer_idx = -1
                curr_gas_in_car = 0
            else:  # can make it to next station
                curr_gas_in_car = curr_gas_in_car - cost[curr_idx]
                
            curr_idx = (curr_idx + 1) % n
            past_start = True
        
        return answer_idx
