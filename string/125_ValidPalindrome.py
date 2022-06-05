# Valid Palindrome
# Time: O(n)
# Space: O(1)
# Topics: Two Pointers, String
# Difficulty: Easy


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        s = s.lower()
        
        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            else:
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1
                    
        return True


# A more pythonic way to solve it
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        return s == s[::-1]
