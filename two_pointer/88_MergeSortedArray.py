# Merge Sorted Array
# Time: O(m + n)
# Space: O(m)
# Topics: Array, Two Pointers, Sorting
# Difficulty: Easy

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = 0
        ptr2 = 0
        
        aux = []
        aux_ptr = 0
        
        while ptr1 < m and ptr2 < n:
            if aux_ptr < len(aux):
                if nums2[ptr2] < nums1[ptr1] or aux[aux_ptr] < nums1[ptr1]:
                    if nums2[ptr2] < aux[aux_ptr]:
                        aux.append(nums1[ptr1])
                        nums1[ptr1] = nums2[ptr2]
                        ptr1 += 1
                        ptr2 += 1
                    else:
                        aux.append(nums1[ptr1])
                        nums1[ptr1] = aux[aux_ptr]
                        aux_ptr += 1
                        ptr1 += 1
                else:
                    ptr1 += 1
            
            elif nums2[ptr2] < nums1[ptr1]:
                aux.append(nums1[ptr1])
                nums1[ptr1] = nums2[ptr2]
                ptr1 += 1
                ptr2 += 1
            else:
                ptr1 += 1
                
        # append remaining in nums1 to aux
        for i in range(ptr1, m):
            aux.append(nums1[i])
                
        while ptr1 < m + n and aux_ptr < len(aux) and ptr2 < n:
            if aux[aux_ptr] < nums2[ptr2]:
                nums1[ptr1] = aux[aux_ptr]
                ptr1 += 1
                aux_ptr += 1
            else:
                nums1[ptr1] = nums2[ptr2]
                ptr1 += 1
                ptr2 += 1
        
        # copy remaining elements
        while aux_ptr < len(aux):
            nums1[ptr1] = aux[aux_ptr]
            aux_ptr += 1
            ptr1 += 1
            
        while ptr2 < n:
            nums1[ptr1] = nums2[ptr2]
            ptr2 += 1
            ptr1 += 1
