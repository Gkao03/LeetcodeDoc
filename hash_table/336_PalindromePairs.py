# Palindrome Pairs
# Time: O(ns^2). n is length of 'words'. s is length of longest string in words.
# Space: O(n) to store hash table. O(n^2) if counting output space.
# Topics: Array, Hash Table, String, Trie
# Difficulty: Hard

from typing import List
from collections import defaultdict

class Solution:
    def is_palindrome(self, word):
        return word == word[::-1]
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # all strings in words are unique
        hash_table = defaultdict(lambda: [])
        
        for i, word in enumerate(words):
            hash_table[word].append(i)
        
        output = []
        for i, word in enumerate(words):
            if word == "":  # edge case if empty string
                for s_idx, string in enumerate(words):
                    if s_idx != i and self.is_palindrome(string):
                        output.append([i, s_idx])
                continue
                
            for w_idx in range(len(word)):
                str1 = word[:w_idx]
                str2 = word[w_idx:]
                
                if self.is_palindrome(str1):
                    for pair_i in hash_table[str2[::-1]]:
                        if pair_i != i:
                            output.append([pair_i, i])
                
                if self.is_palindrome(str2):
                    for pair_i in hash_table[str1[::-1]]:
                        if pair_i != i:
                            output.append([i, pair_i])
                    
        return output
