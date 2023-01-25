# Find Closest Node to Given Two Nodes
# Time: O(n) where n is number of nodes (length of "edges")
# Space: O(n)
# Topics: Depth-First Search, Graph
# Difficulty: Medium

from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        ptr1, hash1 = node1, {}  # {node: depth}
        ptr2, hash2 = node2, {}  # {node: depth}
        depth = 0
        min_distance = float("inf")
        min_node_idx = float("inf")

        while ptr1 != -1 and ptr2 != -1:
            hash1[ptr1] = depth
            hash2[ptr2] = depth

            if ptr1 in hash2:
                if max(hash1[ptr1], hash2[ptr1]) <= min_distance:
                    min_distance = max(hash1[ptr1], hash2[ptr1])
                    min_node_idx = min(min_node_idx, ptr1)

            if ptr2 in hash1:
                if max(hash1[ptr2], hash2[ptr2]) <= min_distance:
                    min_distance = max(hash1[ptr2], hash2[ptr2])
                    min_node_idx = min(min_node_idx, ptr2)

            ptr1 = edges[ptr1] if edges[ptr1] not in hash1 else -1
            ptr2 = edges[ptr2] if edges[ptr2] not in hash2 else -1
            depth += 1

        # finish rest of ptr1 if needed
        while ptr1 != -1:
            hash1[ptr1] = depth

            if ptr1 in hash2:
                if max(hash1[ptr1], hash2[ptr1]) <= min_distance:
                    min_distance = max(hash1[ptr1], hash2[ptr1])
                    min_node_idx = min(min_node_idx, ptr1)

            ptr1 = edges[ptr1] if edges[ptr1] not in hash1 else -1
            depth += 1

        # finish rest of ptr2 if needed
        while ptr2 != -1:
            hash2[ptr2] = depth

            if ptr2 in hash1:
                if max(hash1[ptr2], hash2[ptr2]) <= min_distance:
                    min_distance = max(hash1[ptr2], hash2[ptr2])
                    min_node_idx = min(min_node_idx, ptr2)

            ptr2 = edges[ptr2] if edges[ptr2] not in hash2 else -1
            depth += 1

        return min_node_idx if min_node_idx != float("inf") else -1
