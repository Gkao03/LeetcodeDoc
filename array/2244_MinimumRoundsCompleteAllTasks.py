# Minimum Rounds to Complete All Tasks
# Time: O(n)
# Space: O(n)
# Difficulty: Medium

from typing import List
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks)  # O(n) time and space

        min_rounds = 0
        for count in counts.values():
            if count == 1:
                return -1

            min_rounds += count // 3 if count % 3 == 0 else count // 3 + 1

        return min_rounds
