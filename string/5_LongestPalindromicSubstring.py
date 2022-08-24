# Longest Palindromic Substring
# Time: O(n^2)
# Space: O(n). Need the space to store the output solution
# Topics: String, Dynamic Programming
# Difficulty: Medium

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        
        longest = (1, s[0])
        
        # check odd lengths
        for i in range(len(s)):
            curr_string = s[i]
            left = i - 1
            right = i + 1
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_string = s[left] + curr_string + s[right]
                longest = max(longest, (len(curr_string), curr_string))
                left -= 1
                right += 1
                
        # check even lengths
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                curr_string = s[i:i+2]
                left = i - 1
                right = i + 2
                longest = max(longest, (len(curr_string), curr_string))

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    curr_string = s[left] + curr_string + s[right]
                    longest = max(longest, (len(curr_string), curr_string))
                    left -= 1
                    right += 1
                
        return longest[1]
