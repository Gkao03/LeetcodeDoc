# First Bad Version
# Time: O(logn)
# Space: O(1)
# Topics: Binary Search, Interactive
# Difficulty: Easy


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        earlier_version = 1
        later_version = n
        
        # bad version is guaranteed to exist by constraint so must find in while loop
        while earlier_version <= later_version:
            mid_version = (earlier_version + later_version) // 2
            
            if mid_version == 1:
                if isBadVersion(1):
                    return 1
                earlier_version = mid_version + 1
            elif not isBadVersion(mid_version):  # first bad version on right side
                earlier_version = mid_version + 1
            elif isBadVersion(mid_version) and isBadVersion(mid_version - 1):  # first bad version on left side
                later_version = mid_version - 1
            else:  # isBadVersion(mid_version) and not isBadVersion(mid_version - 1). This is True meaning first bad version is mid
                return mid_version
