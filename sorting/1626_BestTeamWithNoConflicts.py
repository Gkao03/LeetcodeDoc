# Best Team With No Conflicts
# Time: O(n^2)
# Space: O(n)
# Topics: Array, Dynamic Programming, Sorting
# Difficulty: Medium

from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        sort_zipped = sorted(zip(ages, scores))
        ages = [x[0] for x in sort_zipped]
        scores = [x[1] for x in sort_zipped]

        dp = [0] * len(ages)

        for i in range(len(ages)):
            max_score = 0

            for j in range(i + 1):
                if ages[i] > ages[j] and scores[i] >= scores[j] or ages[i] == ages[j]:
                    max_score = max(max_score, dp[j])

            dp[i] = max_score + scores[i]

        return max(dp)
