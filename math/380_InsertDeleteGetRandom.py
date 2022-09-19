# Insert Delete GetRandom O(1)
# Time: O(1) per function call. O(n) for n calls.
# Space: O(n) for n inserts
# Topics: Array, Hash Table, Math, Design, Randomized
# Difficulty: Medium

import random

class RandomizedSet:

    def __init__(self):
        self.hash_map = {}  # stores val: idx of val in vals_arr
        self.vals_arr = []  # store all vals

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        
        self.vals_arr.append(val)
        self.hash_map[val] = len(self.vals_arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        
        # swap with end and update indices, then pop the removed val
        remove_idx = self.hash_map[val]
        end_val = self.vals_arr[-1]
        self.vals_arr[-1], self.vals_arr[remove_idx] = self.vals_arr[remove_idx], self.vals_arr[-1]
        
        self.hash_map[end_val] = remove_idx
        self.vals_arr.pop()
        self.hash_map.pop(val)  # remove value
        return True

    def getRandom(self) -> int:  # guaranteed that at least one element exists when called
        idx = random.randint(0, len(self.vals_arr) - 1)  # start to end inclusive
        return self.vals_arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()