# Unique Binary Search Trees
# Time: O(n^2). O(n) recursive calls with O(n) loop per call
# Space: O(n) stack space and memo table
# Topics: Math, Dynamic Programming, Tree, Binary Search Tree, Binary Tree
# Difficulty: Medium

class Solution:
    def recurse(self, left_limit, right_limit):
        num_elements = right_limit - left_limit + 1

        if num_elements <= 0:
            return 1

        if num_elements in self.memo_table:
            return self.memo_table[num_elements]

        total = 0
        for root in range(left_limit, right_limit + 1):
            total += self.recurse(left_limit, root - 1) * self.recurse(root + 1, right_limit)

        self.memo_table[num_elements] = total
        return total

    def numTrees(self, n: int) -> int:
        self.memo_table = {1: 1,
                           2: 2,
                           3: 5}

        answer = 0
        for root in range(1, n + 1):
            answer += self.recurse(1, root - 1) * self.recurse(root + 1, n)

        return answer
