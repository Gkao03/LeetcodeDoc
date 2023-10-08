# Max Dot Product of Two Subsequences
# Time: O(mn)
# Space: O(mn)
# Topics: Array, Dynamic Programming
# Difficulty: Hard

from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] represents max dot product up to and including i in nums1, j in nums2
        dp = [[0] * len(nums2) for _ in range(len(nums1))]
        dp[0][0] = nums1[0] * nums2[0]

        for i in range(1, len(nums1)):
            dp[i][0] = max(nums1[i] * nums2[0], dp[i - 1][0])

        for j in range(1, len(nums2)):
            dp[0][j] = max(nums1[0] * nums2[j], dp[0][j - 1])

        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                dp[i][j] = max(nums1[i] * nums2[j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + nums1[i] * nums2[j])

        return dp[-1][-1]
