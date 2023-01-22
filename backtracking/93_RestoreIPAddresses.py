# Restore IP Addresses
# Time: O(n choose 4) where n is length of string
# Space: O(1) stack space not counting output space. O(# of answers) counting output.
# Topics: String, Backtracking
# Difficulty: Medium

from typing import List

class Solution:
    def helper(self, s, start_idx, curr_output):
        if len(curr_output) == 4 and start_idx == len(s):
            self.output.append('.'.join(curr_output))
            curr_output.pop()
            return

        if len(curr_output) == 4 and start_idx < len(s):
            curr_output.pop()
            return

        for i in range(start_idx + 1, len(s) + 1):
            curr_s = s[start_idx:i]
            curr_int = int(curr_s)

            # check valid ints
            if curr_int == 0 and curr_s == '0' or 1 <= curr_int <= 255 and curr_s[0] != '0':
                curr_output.append(curr_s)
                self.helper(s, i, curr_output)
            else:
                break

        if len(curr_output) > 0:
            curr_output.pop()

        return

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.output = []
        self.helper(s, 0, [])
        return self.output
