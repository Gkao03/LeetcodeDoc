# Video Stitching
# Time: O(nlogn)
# Space: O(1)
# Topics: Array, Dynamic Programming, Greedy
# Difficulty: Medium

from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # sort by start time
        clips.sort(key=lambda x: x[0])  # O(nlogn) time

        max_end = 0
        answer = 0
        idx = 0

        while idx < len(clips):
            prev_end = max_end
            curr_start, curr_end = clips[idx]

            if curr_start > max_end:
                return -1

            while curr_start <= prev_end:
                max_end = max(max_end, curr_end)

                if max_end >= time:
                    return answer + 1

                idx += 1
                if idx >= len(clips):
                    break

                curr_start, curr_end = clips[idx]

            answer += 1

        return -1
