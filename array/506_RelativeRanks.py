# Relative Ranks
# Time: O(nlogn)
# Space: O(n)
# Topics: Array, Sorting, Heap
# Difficulty: Easy

from typing import List
import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        place = 1
        answer = [""] * len(score)

        scores_and_idx = [(-s, i) for i, s in enumerate(score)]  # O(n)
        heapq.heapify(scores_and_idx)  # O(n)

        while len(scores_and_idx) > 0:  # O(n)
            _, idx = heapq.heappop(scores_and_idx)  # O(logn)
            if place == 1:
                answer[idx] = "Gold Medal"
            elif place == 2:
                answer[idx] = "Silver Medal"
            elif place == 3:
                answer[idx] = "Bronze Medal"
            else:
                answer[idx] = str(place)
            place += 1

        return answer
