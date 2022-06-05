# Best Time to Buy and Sell Stock
# Time: O(n)
# Space: O(n)
# Topics: Array, Dynamic Programming
# Difficulty: Easy

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        # at least 2 prices exist
        max_profit = [0] * len(prices)
        min_price_so_far = [999999] * len(prices)  # arbitrary large value greater than input constraint
        
        min_price_so_far[0] = prices[0]
        
        for i in range(1, len(prices)):
            curr_price = prices[i]
            curr_min_price = min_price_so_far[i - 1]
            curr_profit = curr_price - curr_min_price
            
            max_profit[i] = max(curr_profit, max_profit[i - 1])
            min_price_so_far[i] = min(curr_min_price, curr_price)
            
        return max_profit[-1]
