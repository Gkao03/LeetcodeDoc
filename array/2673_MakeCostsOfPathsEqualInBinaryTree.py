# Make Costs of Paths Equal in a Binary Tree
# Time: O(n)
# Space: O(1)
# Difficulty: Medium

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # equalize the cost from each sub path
        # calculate the cost of the current path from current node (inclusive) to leaf
        # edit cost values in place to save space

        answer = 0

        for i in range(n - 1, 0, -2):  # don't need to check index 0 (root)
            cl_idx = i - 1
            cr_idx = i
            parent_idx = cl_idx // 2

            answer += abs(cost[cl_idx] - cost[cr_idx])
            cost[parent_idx] = cost[parent_idx] + max(cost[cl_idx], cost[cr_idx])

        return answer
