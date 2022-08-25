# Find All Anagrams in a String
# Time: O(n + m). n is length of string s. m is length of string p.
# Space: O(n + m). Space includes output solution space
# Topics: Hash Table, String, Sliding Window
# Difficulty: Medium
# Notes: Space is O(m) not considering output solution. O(n) must be added since
# it is possible the output solution list contains every index in string s.

from collections import defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        p_counter = defaultdict(lambda: 0)
        for char in p:
            p_counter[char] += 1
            
        window_counter = defaultdict(lambda: 0)
        for char in s[0:len(p)]:
            window_counter[char] += 1
            
        is_same = p_counter == window_counter  # check if counts are same
        num_pchar_same = 0
        for key, w_val in window_counter.items():
            p_val = p_counter[key]
            num_pchar_same += min(p_val, w_val)
        
        output = []
        
        if is_same is True:
            output.append(0)
        
        for i in range(len(s) - len(p)):
            left = i  # delete this character from window
            right = i + len(p)  # add this character to window
            
            if is_same is True:
                if s[left] == s[right]:
                    output.append(left + 1)
                else:
                    window_counter[s[left]] -= 1
                    window_counter[s[right]] += 1
                    
                    if window_counter[s[left]] < p_counter[s[left]]:
                        num_pchar_same -= 1
                    if window_counter[s[right]] <= p_counter[s[right]]:
                        num_pchar_same += 1
                    
                    is_same = False
            else:  # is_same is False
                if s[left] != s[right]:
                    window_counter[s[left]] -= 1
                    window_counter[s[right]] += 1
                    
                    if window_counter[s[left]] < p_counter[s[left]]:
                        num_pchar_same -= 1
                    if window_counter[s[right]] <= p_counter[s[right]]:
                        num_pchar_same += 1
                        
                    if num_pchar_same == len(p):
                        is_same = True
                        output.append(left + 1)
            
        return output
