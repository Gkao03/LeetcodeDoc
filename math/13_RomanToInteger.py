# Roman to Integer
# Time: O(n)
# Space: O(1)
# Topics: Hash Table, Math, String
# Difficulty: Easy

class Solution:
    mapping = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
    
    def romanToInt(self, s: str) -> int:
        ptr = 0
        total = 0
        
        while ptr < len(s):
            left = s[ptr]
            right = s[ptr + 1] if ptr + 1 < len(s) else None
            
            val_left = self.mapping[left]
            val_right = self.mapping[right] if right is not None else 0
            
            if val_left < val_right:
                total += val_right - val_left
                ptr += 2
            else:
                total += val_left
                ptr += 1
                
        return total
