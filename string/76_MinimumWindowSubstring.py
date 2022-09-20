# Minimum Window Substring
# Time: O(m + n). m is length of s. n is length of t.
# Space: O(m + n). space for hash table.
# Topics: Hash Table, String, Sliding Window
# Difficulty: Hard

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        # initial counts
        s_counter = defaultdict(lambda: 0)
        for i in range(len(t)):
            s_counter[s[i]] += 1
            
        t_counter = defaultdict(lambda: 0)
        for char in t:
            t_counter[char] += 1
        not_matched = set()  # set keeps track of chars in t not matched in window for s
        
        for char in t_counter.keys():
            if char not in s_counter or s_counter[char] < t_counter[char]:
                not_matched.add(char)
        
        left = 0  # left index of current window
        right = len(t)  # index of next char to be added
        min_window_size = float("inf") if len(not_matched) > 0 else len(t)
        min_substring = "" if min_window_size == float("inf") else s[:len(t)]
        
        while right < len(s):
            while len(not_matched) > 0 and right < len(s):  # increase window until all chars in t are covered
                right_char = s[right]
                s_counter[right_char] += 1
                
                if right_char in not_matched and s_counter[right_char] >= t_counter[right_char]:
                    not_matched.remove(right_char)
                    
                right += 1
                
            while len(not_matched) == 0 and left < right:  # shrink window
                if right - left < min_window_size:
                    min_window_size = right - left  # update min window size
                    min_substring = s[left:right]
                    
                left_char = s[left]
                s_counter[left_char] -= 1
                
                if s_counter[left_char] < t_counter[left_char]:
                    not_matched.add(left_char)
                    
                left += 1
                    
        return min_substring
