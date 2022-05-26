# Palindrome Number
# Time: O(log(n)) where n is the integer
# Space: O(1)
# Topics: Math

import math

class Solution:
    def check_digits(self, num, factor):
        left_digit = num // factor
        right_digit = num % 10
        
        if left_digit == right_digit:
            return True
        return False
    
    def refactor(self, num, factor):
        temp = num % factor
        new_num = temp // 10
        return new_num
        
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        
        curr_x = x
        power = int(math.log10(curr_x))
        
        while curr_x != 0:
            factor = 10 ** power
            
            if not self.check_digits(curr_x, factor):
                return False
            
            curr_x = self.refactor(curr_x, factor)
            power -= 2
            
        return True
