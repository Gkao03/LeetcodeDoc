# Longest Repeating Character Replacement
# Time: O(n)
# Space: O(1)
# Topics: Hash Table, String, Sliding Window
# Difficulty: Medium
# Notes: s consists of only uppercase English letters so
# hash table contains at most 26 characters.

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(lambda: 0)
        left_idx = 0
        right_idx = 0
        max_count_window = 0
        max_len = k
        
        while right_idx < len(s):
            char = s[right_idx]
            counter[char] += 1
            max_count_window = max(max_count_window, counter[char])
            
            while right_idx - left_idx + 1 - max_count_window > k:
                counter[s[left_idx]] -= 1
                left_idx += 1
                max_count_window = max(counter.values())  # O(26) time
                
            right_idx += 1
            max_len = max(max_len, right_idx - left_idx)
            
        return max_len
