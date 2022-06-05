# Valid Anagram
# Time: O(n)
# Space: O(n)
# Topics: Hash Table, String, Sorting
# Difficulty: Easy

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = defaultdict(lambda: 0)
        for char in s:
            char_count[char] += 1
            
        for char in t:
            char_count[char] -= 1
            
            if char_count[char] < 0:
                return False
            
        leftover_count = sum(char_count.values())  # O(n) to calculate
        
        if leftover_count != 0:
            return False
        
        return True
