# Final Prices With a Special Discount in a Shop
# Time: O(n)
# Space: O(n)
# Topics: Array, Stack, Monotonic Stack
# Difficulty: Easy

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = [0] * len(prices)
        answer[-1] = prices[-1]
        stack = [prices[-1]]

        for i in range(len(prices) - 2, -1, -1):
            curr_price = prices[i]

            while len(stack) > 0 and stack[-1] > curr_price:  # find first available discount
                stack.pop()

            if len(stack) == 0:  # no discount
                stack.append(curr_price)
                answer[i] = curr_price
                continue

            # discount found (stack[-1])
            answer[i] = curr_price - stack[-1]
            stack.append(curr_price)

        return answer
        