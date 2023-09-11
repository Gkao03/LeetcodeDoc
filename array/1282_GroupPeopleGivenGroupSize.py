# Group the People Given the Group Size They Belong To
# Time: O(n)
# Space: O(n) to keep hash table
# Topics: Array, Hash Table
# Difficulty: Medium

from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output = []
        groupsize_to_group = defaultdict(lambda: [])

        for i, group_size in enumerate(groupSizes):
            groupsize_to_group[group_size].append(i)

            if len(groupsize_to_group[group_size]) == group_size:
                output.append(groupsize_to_group[group_size])
                groupsize_to_group.pop(group_size)
        
        output.extend(groupsize_to_group.values())

        return output
