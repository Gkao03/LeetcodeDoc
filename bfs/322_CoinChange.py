# Coin Change
# Time: Pseudo O(CA). C is number of denominations. A is amount.
# Space: Pseudo O(A). A is amount.
# Topics: Array, Dynamic Programming, Breadth-First Search
# Difficulty: Medium
# Notes: can use BFS for naive solution, but will get exponential runtime without DP.
# The DP table is built bottom up.

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # value and index represents min amount of coins needed to get that amount
        dp_table = [10 ** 5] * (amount + 1)  # filled with arbitrary large value greater than constraint
        dp_table[0] = 0  # 0 coins needed for 0 amount
        print(dp_table)
        
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    if dp_table[amt - coin] != 2 * amount:
                        dp_table[amt] = min(dp_table[amt], dp_table[amt - coin] + 1)
                        
        if dp_table[-1] == 10 ** 5:
            return -1
        
        return dp_table[-1]
