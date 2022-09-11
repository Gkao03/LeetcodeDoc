# Random Pick With Weights
# Time: O(n) to init. O(logn) for each pickIndex call. O(klogn) for k calls.
# Space: O(n)
# Topics: Math, Binary Search, Prefix Sum, Randomized
# Notes: it is important to do a binary search for this problem to reduce runtime.
# using prefix sum of weights (cumulative weights) can achieve this. Then choose an
# integer (uniform sample) from 0 to sum - 1. The interval that this lies in will
# indicate the index to return. The binary search capability can be achieved by
# specifying the "cum_weights" argument in the random module. Using the "weights"
# argument will not achieve binary search.

from typing import List
import random

class Solution:
    def __init__(self, w: List[int]):
        prefix_weights = []
        running_sum = 0
        for weight in w:
            running_sum += weight
            prefix_weights.append(running_sum)
        self.prefix_weights = prefix_weights
        self.samples = [i for i in range(len(w))]

    def pickIndex(self) -> int:
        return random.choices(self.samples, cum_weights=self.prefix_weights, k=1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
