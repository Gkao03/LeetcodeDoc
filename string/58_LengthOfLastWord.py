# Length of Last Word
# Time: O(n)
# Space: O(1)
# Topics: String
# Difficulty: Easy

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        space_idx = len(s) - 1
        found_alpha = False
        end_space_chars_count = 0
        
        while space_idx >= 0:
            if s[space_idx] == ' ' and not found_alpha:
                end_space_chars_count += 1
                space_idx -= 1
            elif s[space_idx] != ' ':
                found_alpha = True
                space_idx -= 1
            else:
                break
                
        length = len(s) - space_idx - end_space_chars_count - 1
        return length
