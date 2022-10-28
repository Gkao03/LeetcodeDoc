# Split Array into Fibonacci Sequence
# Time: O(n^n)
# Space: O(n)
# Topics: String, Backtracking
# Difficulty: Medium

from typing import List

class Solution:
    def helper(self, curr_num):
        if len(curr_num) == 0:
            return True
        
        for i in range(1, len(curr_num) + 1):
            left_num = curr_num[:i]
            right_num = curr_num[i:]
            
            # make sure left num is a valid split (no leading 0 unless single digit)
            if len(left_num) > 1 and left_num[0] == '0' or int(left_num) > self.max_int:
                break
                
            if len(self.output) < 2 or int(left_num) == self.output[-1] + self.output[-2]:
                self.output.append(int(left_num))
                is_valid = self.helper(right_num)
            else:
                continue
            
            if not is_valid:
                self.output.pop()
            else:
                return True
            
        return False
        
    def splitIntoFibonacci(self, num: str) -> List[int]:
        self.output = []
        self.max_int = 2 ** 31 - 1
        
        for i in range(1, len(num) + 1):
            left_num = num[:i]
            right_num = num[i:]
            
            if len(left_num) > 1 and left_num[0] == '0' or int(left_num) > self.max_int:
                break
            self.output.append(int(left_num))
            
            is_valid = False
            for j in range(1, len(right_num) + 1):
                left_num2 = right_num[:j]
                right_num2 = right_num[j:]
                
                if len(left_num2) > 1 and left_num2[0] == '0' or int(left_num2) > self.max_int:
                    is_valid = False
                    break
                self.output.append(int(left_num2))
                
                # call recursively
                is_valid = self.helper(right_num2)
                
                if len(self.output) <= 2 or not is_valid:
                    self.output.pop()
                else:
                    return self.output
                
            self.output.pop()
        
        if len(self.output) < 3:
            return []
        
        return self.output
