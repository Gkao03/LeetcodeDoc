# Implement strStr()
# Time: O(n + m). n = length of needle. m = length of haystack
# Space: O(n). n = length of needle (to construct the lps table)
# Topics: Two Pointers, String, String Matching
# Difficulty: Easy
# Notes: KMP Algorithm

class Solution:
    def calc_lps(self, pattern):  # O(pattern) to construct
        if len(pattern) == 1:
            return [0]
        
        lps = [0] * len(pattern)  # longest proper prefix that is also a suffix
        i = 0
        j = 1
        
        while j < len(pattern):
            if pattern[j] == pattern[i]:
                lps[j] = i + 1
                i += 1
                j += 1
            elif pattern[j] != pattern[i] and i != 0:
                i = lps[i-1]
            else:
                lps[j] = 0
                j += 1
                
        return lps
                 
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        lps = self.calc_lps(needle)
        
        h_idx = 0
        n_idx = 0
        
        while h_idx < len(haystack):
            if haystack[h_idx] == needle[n_idx]:
                n_idx += 1
                h_idx += 1
            elif haystack[h_idx] != needle[n_idx] and n_idx != 0:
                n_idx = lps[n_idx - 1]
            elif haystack[h_idx] != needle[n_idx] and n_idx == 0:
                h_idx += 1
                
            # found condition
            if n_idx >= len(needle):
                return h_idx - len(needle)
            
        return -1
