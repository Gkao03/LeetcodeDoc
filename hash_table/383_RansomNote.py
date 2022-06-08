# Ransom Note
# Time: O(n + m). n is length of ransom note. m is length of magazine.
# Space: O(m)
# Topics: Hash Table, String, Counting
# Difficulty: Easy

from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        mag_count = defaultdict(lambda: 0)  # default 0 count
        
        for char in magazine:
            mag_count[char] += 1
            
        for char in ransomNote:
            mag_count[char] -= 1
            if mag_count[char] < 0:
                return False
            
        return True
