# Sort Colors
# Time: O(n)
# Space: O(1)
# Topics: Array, Two Pointers, Sorting
# Difficulty: Medium
# Notes: can also use 3 pointer for better efficiency and don't have to enumerate
# all possible cases

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_ptr = 0
        right_ptr = len(nums) - 1
        zero_ptr = 0
        two_ptr = len(nums) - 1
        
        while left_ptr < right_ptr:
            val_left = nums[left_ptr]
            val_right = nums[right_ptr]
            
            if val_left == 0 and val_right == 2:  # 0, 2
                left_ptr += 1
                right_ptr -= 1
            elif val_left == 0 and val_right == 1:  # 0, 1
                left_ptr += 1
            elif val_left == 1 and val_right == 2:  # 1, 2
                right_ptr -= 1
            elif val_left == 0 and val_right == 0:  # 0, 0
                nums[left_ptr + 1], nums[right_ptr] = nums[right_ptr], nums[left_ptr + 1]
                left_ptr += 2
            elif val_left == 2 and val_right == 2:  # 2, 2
                nums[right_ptr - 1], nums[left_ptr] = nums[left_ptr], nums[right_ptr - 1]
                right_ptr -= 2
            elif val_left == 2 and val_right == 0:  # 2, 0
                nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
                left_ptr += 1
                right_ptr -= 1
            elif val_left == 1 and val_right == 0:  # 1, 0
                nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
                left_ptr += 1
            elif val_left == 2 and val_right == 1:  # 2, 1
                nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
                right_ptr -= 1
            elif val_left == 1 and val_right == 1:  # 1, 1
                while zero_ptr < len(nums) and nums[zero_ptr] != 0:
                    zero_ptr += 1
                    
                # swap
                if zero_ptr < len(nums):
                    nums[zero_ptr], nums[left_ptr] = nums[left_ptr], nums[zero_ptr]
                
                left_ptr += 1
                
                while two_ptr >= 0 and nums[two_ptr] != 2:
                    two_ptr -= 1
                    
                # swap
                if two_ptr >= 0:
                    nums[two_ptr], nums[right_ptr] = nums[right_ptr], nums[two_ptr]
                    
                right_ptr -= 1  
            
            zero_ptr = max(zero_ptr, left_ptr)
            two_ptr = min(two_ptr, right_ptr)
            
            if zero_ptr >= len(nums) and two_ptr < 0:  # both out of bounds
                break
