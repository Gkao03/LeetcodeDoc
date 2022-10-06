# Median of Two Sorted Arrays
# Time: O(min(log m, log n))
# Space: O(1)
# Topics: Array, Binary Search, Divide and Conquer
# Difficulty: Hard
# Notes: https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # array A (nums1) is smaller array. Array B (nums2) is larger array.
        n, m = len(nums1), len(nums2)
        
        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = len(nums1), len(nums2)
            
        start = 0
        end = n
        real_mid_merged = (n + m + 1) // 2
        
        while start <= end:
            mid = (start + end) // 2
            leftAsize = mid
            leftBsize = real_mid_merged - mid
            
            leftA = nums1[leftAsize - 1] if leftAsize > 0 else float('-inf')
            leftB = nums2[leftBsize - 1] if leftBsize > 0 else float('-inf')
            rightA = nums1[leftAsize] if leftAsize < n else float('inf')
            rightB = nums2[leftBsize] if leftBsize < m else float('inf')
            
            if leftA <= rightB and leftB <= rightA:
                if (m + n) % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                return max(leftA, leftB)
            elif leftA > rightB:
                end = mid - 1
            else:
                start = mid + 1
        
        # should not reach this return statement anyways
        return 0
