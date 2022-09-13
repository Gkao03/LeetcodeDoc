# Largest Number
# Time: O(nlogn)
# Space: O(n). must store output string
# Topics: String, Greedy, Sorting
# Difficulty: Medium

from typing import List
import math

class Solution:
    class IntWrapper:
        def __init__(self, num):
            self.num = num
            self.num_digits = int(math.log10(num)) + 1 if num > 0 else 1
            
        def __gt__(self, int_wrapper):
            num = int_wrapper.num
            num_digits = int_wrapper.num_digits
            if 10 ** num_digits * self.num + num > 10 ** self.num_digits * num + self.num:
                return True
            return False
            
    def largestNumber(self, nums: List[int]) -> str:
        int_list = [self.IntWrapper(num) for num in nums]
        int_list.sort(reverse=True)
        return str(int("".join([str(int_wrapper.num) for int_wrapper in int_list])))
