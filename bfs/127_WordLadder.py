# Word Ladder
# Time: O(n*m^2). n is length of wordList. m is length of each string.
# Space: O(n)
# Topics: Hash Table, String, Breadth-First Search
# Difficulty: Hard
# Notes: keep a checked set that we greedily pick and add to to prevent
# the time complexity from blowing up. If a word has been added previously
# to a chain, no need to check it again.

from typing import List
from collections import deque

class Solution:    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary = set(wordList)  # O(n) time and O(n) space
        if endWord not in dictionary:
            return 0
        
        # should guarantee to have a solution now
        checked = {beginWord}  # set of checked words in chain. O(n) space
        queue = deque()  # word, current length. O(n) space since we have a checked set
        queue.append((beginWord, 1))
        
        while len(queue) > 0:  # O(n) time
            curr_word, curr_len = queue.popleft()
            curr_word = [*curr_word]
            
            for i in range(len(curr_word)):  # O(m)
                curr_char_ord = ord(curr_word[i]) - ord('a')
                
                for j in range(26):  # O(26)
                    if j != curr_char_ord:
                        new_char = chr(ord('a') + j)
                        curr_word[i] = new_char
                        new_word = "".join(curr_word)  # O(m) to join
                        
                        if new_word == endWord:
                            return curr_len + 1
                        
                        if not new_word in checked and new_word in dictionary:
                            queue.append((new_word, curr_len + 1))
                            checked.add(new_word)
                            
                        # reset
                        curr_word[i] = chr(curr_char_ord + ord('a'))
        
        # should never reach this return statement anyways
        return 0
