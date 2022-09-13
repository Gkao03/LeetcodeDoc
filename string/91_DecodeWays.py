# Decode Ways
# Time: O(n)
# Space: O(1)
# Topics: String, Dynamic Programming
# Difficulty: Medium

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1
        
        prevprev_dp = 1
        prev_dp = 1
        answer = 1
        for i in range(1, len(s)):
            left_digit = s[i - 1]
            right_digit = s[i]
            
            # check both digits together
            two_digits_valid = False if left_digit == '0' or int(left_digit + right_digit) > 26 else True
            
            # check single digit on right
            one_digit_valid = False if right_digit == '0' else True
            
            if not two_digits_valid and not one_digit_valid:  # impossible to decode
                return 0
            elif two_digits_valid and one_digit_valid:  # both single and double digits are valid
                answer = prevprev_dp + prev_dp
            elif two_digits_valid:  # only double digits are valid
                answer = prevprev_dp
            else:  # only current digit is valid
                answer = prev_dp
                
            prevprev_dp, prev_dp = prev_dp, answer
        
        return answer
