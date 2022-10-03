# Maximum Frequency Stack
# Time: O(1) per operation
# Space: O(n) for n operations
# Topics: Hash Table, Stack, Design, Ordered Set
# Difficulty: Hard
# Notes: the idea is to use a list of stacks

from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.hash_table = defaultdict(lambda: 0)
        self.stacks = []

    def push(self, val: int) -> None:
        curr_idx = self.hash_table[val]
        self.hash_table[val] += 1
        
        if curr_idx >= len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[curr_idx].append(val)

    def pop(self) -> int:
        # at least one element will exist
        popped = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
            
        self.hash_table[popped] -= 1
        return popped


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
