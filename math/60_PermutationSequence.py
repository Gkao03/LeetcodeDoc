# Permutation Sequence
# Time: O(n^2). O(n) recursive calls with O(n) loop for each call
# Space: O(n) stack space + bookkeeping space
# Topics: Math, Recursion
# Difficulty: Hard

from math import factorial

class Solution:
    def recurse(self, n, k, used_digits, curr_k, n_remain, curr_digit_list):
        jump_size = factorial(n_remain - 1)
        prev_digit = None
        prev_count = curr_k
        order = 0

        for digit in range(1, n + 1):  # O(n)
            if not used_digits[digit - 1]:
                count_k = curr_k + order * jump_size

                if n_remain == 1 and count_k == k:  # end condition
                    curr_digit_list.append(str(digit))
                    return ''.join(curr_digit_list)

                if count_k == k:
                    used_digits[digit - 1] = True
                    curr_digit_list.append(str(digit))
                    return self.recurse(n, k, used_digits, count_k, n_remain - 1, curr_digit_list)

                if count_k > k:
                    break

                prev_digit = digit
                prev_count = count_k
                order += 1

        used_digits[prev_digit - 1] = True
        curr_digit_list.append(str(prev_digit))
        return self.recurse(n, k, used_digits, prev_count, n_remain - 1, curr_digit_list)

    def getPermutation(self, n: int, k: int) -> str:
        used_digits = [False] * n  # idx i - 1 represents int i
        return self.recurse(n, k, used_digits, 1, n, [])
