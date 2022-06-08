# Min Stack
# Time: O(1) per operation. O(n) for n operations
# Space: O(n) for n push operations
# Topics: Stack, Design
# Difficulty: Easy
# Notes: we use the formula 2x-curr_min to encode the stack values (where x is the current value) when x < min. 
# since x < curr_min, this guarantees that 2x-curr_min<x which means the pushed value will always be less than the current minimum.
# when popping, if we encounter a popped value less than the current min, since we have the formula 2x-curr_min=y, we can do the
# inverse to get back the min which is curr_min=2x-y where x is now the current min (as x < min in the push operation) and y is the
# current element looked at on the pop operation. 
# See https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/ for more details

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_element = val
            self.stack.append(val)
        else:
            if val < self.min_element:  # push y = 2val-curr_min. val is now the new curr_min
                self.stack.append(2 * val - self.min_element)
                self.min_element = val
            else:  # just push normally
                self.stack.append(val)
        

    def pop(self) -> None:  # given pop operations are always valid
        val_popped = self.stack.pop()
        
        if val_popped < self.min_element:
            prev_min = 2 * self.min_element - val_popped
            self.min_element = prev_min
            return (val_popped + prev_min) / 2
        else:  # just pop normally
            if len(self.stack) == 0:
                self.min_element = None
            return val_popped
        

    def top(self) -> int:  # given top operations are always valid
        val_top = self.stack[-1]
        
        if val_top < self.min_element:
            prev_min = 2 * self.min_element - val_top
            return int((val_top + prev_min) / 2)  # this should be a whole number anyways
        else:  # just top normally
            return val_top
        

    def getMin(self) -> int:
        return self.min_element
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()