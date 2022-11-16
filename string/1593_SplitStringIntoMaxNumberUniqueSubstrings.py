# Split a String Into the Max Number of Unique Substrings
# Time: O(2^n)
# Space: O(n) stack space and to store set.
# Topics: Hash Table, String, Backtracking
# Difficulty: Medium

class Solution:
    def split(self, s, left_idx, right_idx, string_set):
        if left_idx >= len(s):
            self.answer = max(self.answer, len(string_set))
            return
        
        while right_idx <= len(s):
            curr_string = s[left_idx:right_idx]
            
            if curr_string not in string_set:
                string_set.add(curr_string)  # add valid string to existing set
                self.split(s, right_idx, right_idx + 1, string_set)  # recurse
                string_set.remove(curr_string)  # remove from set
                
            right_idx += 1
    
    def maxUniqueSplit(self, s: str) -> int:
        self.answer = 0
        string_set = set()
        
        self.split(s, 0, 1, string_set)
        return self.answer
