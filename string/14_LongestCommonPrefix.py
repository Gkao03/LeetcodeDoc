# Longest Common Prefix
# Time: O(n + m) where n is the length of the strs array. m is the length of the longest str
# Space: O(1)
# Topics: String
# Difficulty: Easy

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        max_str_idx = 0
        
        first_str = strs[0]
        second_str = strs[1]
        
        for i, tup in enumerate(zip(first_str, second_str)):
            if tup[0] == tup[1]:
                max_str_idx += 1
            else:
                break
        
        max_str_idx -= 1
                
        strs_idx = 1
        while strs_idx < len(strs) - 1:
            if max_str_idx < 0:
                break
            
            str1 = strs[strs_idx]
            str2 = strs[strs_idx + 1]
            
            max_str_idx = min(max_str_idx, len(str1) - 1, len(str2) - 1)
            
            while max_str_idx >= 0:
                if str1[max_str_idx] != str2[max_str_idx]:
                    max_str_idx -= 1
                else:
                    break
            
            strs_idx += 1
                    
        if max_str_idx < 0:
            return ""
            
        # last check with last 2 strings
        first_str = strs[-2]
        second_str = strs[-1]
        
        res_str_idx = 0
        
        while res_str_idx <= max_str_idx:
            if first_str[res_str_idx] == second_str[res_str_idx]:
                res_str_idx += 1
        
        prefix = first_str[:res_str_idx]
        
        return prefix
