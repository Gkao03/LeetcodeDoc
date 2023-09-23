# Longest String Chain
# Time: O(ns^2). n is length of words list. s is max length of a string.
# Space: O(ns). consider each character taking up space.
# Topics: Array, Hash Table, Two Pointers, String, Dynamic Programming
# Difficulty: Medium

from typing import List
from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        set_words = set(words)
        sorted_words = sorted(words, key=len, reverse=True)
        word_to_chainlen = defaultdict(lambda: 1)
        

        for word in sorted_words:  # O(n)
            i = 0

            while i < len(word):  # O(s)
                temp_word = word[:i] + word[i+1:]  # O(s)

                if temp_word in set_words:  # O(s) to hash
                    word_to_chainlen[temp_word] = max(word_to_chainlen[temp_word], word_to_chainlen[word] + 1)

                i += 1

        return max(word_to_chainlen.values()) if len(word_to_chainlen.values()) != 0 else 1
