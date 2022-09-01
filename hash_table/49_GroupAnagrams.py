# Group Anagrams
# Time: O(ns). n is length of strs. s is length of longest string in strs
# Space: O(n)
# Notes: strs[i] contains only lowercase English letters and strs has at least 1 element.

from collections import defaultdict
from typing import List

class Solution:
    def get_counts(self, word):
        counts = [0] * 26  # 26 lowercase English letters
        for char in word:
            counts[ord(char) - ord('a')] += 1
            
        return counts
    
    def get_encoding(self, counts):
        encoding = ""
        for i, val in enumerate(counts):
            encoding += str(val) + chr(ord('a') + i)
            
        return encoding
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(lambda: [])
        
        for word in strs:
            counts = self.get_counts(word)  # O(s)
            encoding = self.get_encoding(counts)  # O(26)
            hash_map[encoding].append(word)
            
        return hash_map.values()
