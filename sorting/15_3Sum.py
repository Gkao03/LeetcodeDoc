# 3Sum
# Time: O(n^2)
# Space: O(n) - hashmap is used
# Topics: Array, Two Pointers, Sorting
# Difficulty: Medium
# Notes: We use sorting and then fix one value at a time through the array and use 
# two pointers to find the other two values. This results in nested loops for O(n^2) runtime

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()  # O(nlogn)
        
        first_val_visited = set()
        triplets = []
        
        for i, val in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            
            if val not in first_val_visited:  # only iterate if not used first val before
                first_val_visited.add(val)
                second_val_visited = set()

                while left < right:
                    if val + nums[left] + nums[right] < 0:  # increase left pointer to increase sum
                        left += 1
                    elif val + nums[left] + nums[right] > 0:  # decrease right pointer to decrease sum
                        right -= 1
                    else:  # sum is 0
                        if nums[left] not in second_val_visited:
                            second_val_visited.add(nums[left])
                            triplets.append([val, nums[left], nums[right]])
                        left += 1
                            
        return triplets
