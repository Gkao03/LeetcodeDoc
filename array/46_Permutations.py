# Permutations
# Time: O(n^2 * n!). There are n*n! function calls and each function takes O(n) time. List concat is also O(n).
# Space: O(n)
# Topics: Array, Backtracking
# Difficulty: Medium

from itertools import permutations
from typing import List

# Recursive Solution
class Solution:
    def permute_helper(self, nums, perm, all_perms):
        for i, num in enumerate(nums):
            curr_perm = perm.copy()
            curr_perm.append(num)
            
            if len(nums) == 1:
                all_perms.append(curr_perm)
            else:
                self.permute_helper(nums[:i] + nums[i+1:], curr_perm, all_perms)    
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        # all integers in nums guaranteed to be unique
        all_perms = []
        self.permute_helper(nums, [], all_perms)
        return all_perms


# Pythonic Solution
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = list(permutations(nums))
        perm = [list(p) for p in perm]
        return perm