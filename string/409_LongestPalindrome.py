# Longest Palindrome
# Time: O(n)
# Space: O(n)
# Topics: Hash Table, String, Greedy
# Difficulty: Easy

from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_even_dict = defaultdict(lambda: 0)
        
        for char in s:
            char_even_dict[char] += 1
        
        
        longest_len = 0
        odd_count = 0
        for char, char_count in char_even_dict.items():
            if char_count % 2 == 0:  # even
                longest_len += char_count
            else:  # odd
                if char_count >= 3:
                    longest_len += char_count - 1
                odd_count += 1
                
        longest_len = longest_len + 1 if odd_count > 0 else longest_len
        
        return longest_len
