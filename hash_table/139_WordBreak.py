# Word Break
# Time: O(mn). m is number of words in wordDict. n is length of string.
# Space: O(n)
# Topics: Hash Table, String, Dynamic Programming, Trie, Memoization
# Difficulty: Medium

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        
        for s_idx in range(len(s) - 1, -1, -1):
            for word in wordDict:
                word_len = len(word)
                if s_idx + word_len <= len(s) and s[s_idx:s_idx + word_len] == word:  # found a match
                    dp[s_idx] = dp[s_idx + word_len]
                
                if dp[s_idx] is True:  # found a match AND RHS of string can also be segmented
                    break
            
        return dp[0]
