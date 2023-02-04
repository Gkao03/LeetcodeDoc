# Permutation in String
# Time: O(m - n). n is len(s1). m is len(s2). m > n in general case.
# Space: O(1)
# Topics: Hash Table, Two Pointers, String, Sliding Window
# Difficulty: Medium
# Notes: since input is only lower case english alphabet, O(26) == O(1).

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # O(n) space/time for hash table
        s1_count = defaultdict(lambda: 0)
        for char in s1:
            s1_count[char] += 1

        left = 0  # remove this char
        right = len(s1)  # add this char

        # O(n) space/time for hash table
        s2_window = defaultdict(lambda: 0)
        for char in s2[left:right]:
            s2_window[char] += 1

        # O(n) time check
        if s1_count == s2_window:
            return True

        # O(m - n) time check
        while right < len(s2):
            left_char = s2[left]  # delete this
            right_char = s2[right]  # add this

            s2_window[left_char] -= 1
            s2_window[right_char] += 1

            # O(26)
            equal_count = True
            for i in range(26):
                curr_char = chr(ord('a') + i)

                if s2_window[curr_char] != s1_count[curr_char]:
                    equal_count = False
                    break
            
            if equal_count:
                return True

            left += 1
            right += 1

        return False
