# Number of Longest Increasing Subsequence
# Time: O(n^2)
# Space: O(n)
# Topics: Array, Dynamic Programming, Binary Indexed Tree, Segment Tree
# Difficulty: Medium
# Notes: the minimum value for each dp_lis[i] and count_list[i] will be 1 
# since a sequence can be the value itself in the smallest case.

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp_lis = [1]  # dp_lis[i] represents LIS up to and must include (but not past) element at ith index
        count_lis = [1]  # count_lis[i] represents number of increasing subsequences of length dp_lis[i] up to and must include (but not past) element at ith index
        max_lis = 1

        for i in range(1, len(nums)):  # O(n)
            curr_lis = 0
            curr_num = nums[i]

            for j in range(i):  # O(n)
                if curr_num > nums[j]:
                    curr_lis = max(curr_lis, dp_lis[j])

            curr_sum = 0

            for j in range(i):  # O(n)
                if dp_lis[j] == curr_lis and curr_num > nums[j]:
                    curr_sum += count_lis[j]

            dp_lis.append(curr_lis + 1)
            count_lis.append(curr_sum if curr_lis > 0 else 1)

            # update max lis
            max_lis = max(max_lis, curr_lis + 1)

        # get the values that have lis equal to max lis and sum it up for the answer
        num_lis = sum([val for val, lis in zip(count_lis, dp_lis) if lis == max_lis])

        return num_lis
