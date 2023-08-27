# Minimum Swaps To Make Sequences Increasing
# Time: O(n)
# Space: O(1)
# Topics: Array, Dynamic Programming
# Difficulty: Hard

from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        prev_swap_count = 1
        prev_notswap_count = 0

        for i in range(1, len(nums1)):
            # first consider if we don't swap the current pair
            curr_notswap_prev_notswap_count = curr_notswap_prev_swap_count = float("inf")

            # 1. check case if previous values were not swapped
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                curr_notswap_prev_notswap_count = prev_notswap_count

            # 2. check case if previous values were swapped
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                curr_notswap_prev_swap_count = prev_swap_count

            curr_notswap_count = min(curr_notswap_prev_notswap_count, curr_notswap_prev_swap_count)

            # next consider if we do swap the current pair
            curr_swap_prev_notswap_count = curr_swap_prev_swap_count = float("inf")

            # 1. check case if previous values were not swapped
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                curr_swap_prev_notswap_count = prev_notswap_count + 1

            # 2. check case if previous values were swapped
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                curr_swap_prev_swap_count = prev_swap_count + 1

            curr_swap_count = min(curr_swap_prev_notswap_count, curr_swap_prev_swap_count)

            # update prev counts
            prev_swap_count = curr_swap_count
            prev_notswap_count = curr_notswap_count
        
        return min(prev_swap_count, prev_notswap_count)
