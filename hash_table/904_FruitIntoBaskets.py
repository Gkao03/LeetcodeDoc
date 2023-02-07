# Fruit Into Baskets
# Time: O(n)
# Space: O(1)
# Topics: Array, Hash Table, Sliding Window
# Difficulty: Medium

from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 1
        counts = defaultdict(lambda: 0)

        counts[fruits[0]] += 1
        left = 0  # idx of left side of window
        right = 1  # idx of right side just outside of window

        while right < len(fruits):
            # extend window
            while right < len(fruits) and len(counts) <= 2:
                counts[fruits[right]] += 1

                if len(counts) <= 2:
                    max_fruits = max(max_fruits, sum(counts.values()))

                right += 1

            # shrink window
            while left < right and len(counts) > 2:
                counts[fruits[left]] -= 1

                if counts[fruits[left]] == 0:
                    counts.pop(fruits[left])

                left += 1

        return max_fruits
