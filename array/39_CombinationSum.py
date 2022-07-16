# Combination Sum
# Time: Pseudo exponential due to "target" input
# Space: O(n * target/min(candidates)) stack space. n is length of candidates
# Topics: Array, Backtracking
# Difficulty: Medium
# Notes: Guaranteed that number of unique combinations that sum to target is less than 150 combinations

from typing import List

class Solution:
    def combo_helper(self, candidates, target, idx, solution, all_solutions): 
        for i in range(idx, len(candidates)):
            candidate = candidates[i]
            curr_solution = solution.copy()
            
            if target - candidate == 0:
                curr_solution.append(candidate)
                all_solutions.append(curr_solution)
            elif target - candidate > 0:
                curr_solution.append(candidate)
                self.combo_helper(candidates, target - candidate, i, curr_solution, all_solutions)
                
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # O(nlogn)
        all_solutions = []
        self.combo_helper(candidates, target, 0, [], all_solutions)
        return all_solutions
