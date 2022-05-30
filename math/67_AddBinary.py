# Add Binary
# Time: O(n + m). n is length of a. m is length of b
# Space: O(1)
# Topics: Math, String, Bit Manipulation, Simulation
# Difficulty: Easy

class Solution:
    def decimal2binary_str(self, dec: int, string: str):  # O(logn) to convert decimal to binary
        if dec <= 1:
            return '1' if dec == 1 else '0'
        
        string = self.decimal2binary_str(dec // 2, string)
        string = string + '0' if dec % 2 == 0 else string + '1'
        return string
    
    def addBinary(self, a: str, b: str) -> str:
        a_int = 0
        b_int = 0
        
        for power in range(len(a)):
            idx = len(a) - power - 1
            bit = 1 if a[idx] == '1' else 0
            a_int += 2 ** power * bit
            
        for power in range(len(b)):
            idx = len(b) - power - 1
            bit = 1 if b[idx] == '1' else 0
            b_int += 2 ** power * bit
            
        num = a_int + b_int
        
        solution = self.decimal2binary_str(num, "")
        return solution
