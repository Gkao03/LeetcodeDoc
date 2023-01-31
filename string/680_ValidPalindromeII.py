# Valid Palindrome II
# Time: O(n)
# Space: O(1)
# Topics: Two Pointers, String, Greedy
# Difficulty: Easy

class Solution:
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            left = i
            right = len(s) - 1 - i

            if s[left] != s[right]:
                # remove left char
                if not self.is_palindrome(s, left + 1, right) and not self.is_palindrome(s, left, right - 1):
                    return False

                return True

        return True
