# Longest Substring Without Repeating Characters
# Time: O(n)
# Space: O(n)
# Topics: Hash Table, String, Sliding Window
# Difficulty: Medium

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        count_idx_dict = defaultdict(lambda: [0, None])  # dictionary holds [count, most recent idx]
        start_idx = 0
        end_idx = 0
        max_len = 0
        
        while end_idx < len(s):
            if count_idx_dict[s[end_idx]][0] == 0:  # extend window
                count_idx_dict[s[end_idx]][0] += 1
                count_idx_dict[s[end_idx]][1] = end_idx
                end_idx += 1
                max_len += 1
            else:  # shift window
                check_idx = count_idx_dict[s[end_idx]][1] + 1  # next idx where existing character is not present in window
                while start_idx < check_idx and end_idx < len(s):
                    # update char at start idx
                    start_count, start_last_idx = count_idx_dict[s[start_idx]]
                    count_idx_dict[s[start_idx]] = [start_count - 1, start_last_idx]
                    start_idx += 1
                    
                    # update char at end idx
                    count_idx_dict[s[end_idx]][0] += 1
                    count_idx_dict[s[end_idx]][1] = end_idx
                    end_idx += 1
                    if end_idx >= len(s):
                        break
                        
                    # update check idx to latest idx needed to iterate to for no duplicates
                    check_idx = max(check_idx, count_idx_dict[s[end_idx]][1] + 1 if count_idx_dict[s[end_idx]][1] is not None else -1)
        
        return max_len
