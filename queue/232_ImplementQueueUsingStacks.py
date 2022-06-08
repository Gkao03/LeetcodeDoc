# Implement Queue using Stacks
# Time: amortized O(1) per operation. O(n) for n operations
# Space: O(n). n push operations
# Topics: Stack, Design, Queue
# Difficulty: Easy


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                stack1_popped = self.stack1.pop()
                self.stack2.append(stack1_popped)
        
        stack2_popped = self.stack2.pop()
        return stack2_popped

    def peek(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                stack1_popped = self.stack1.pop()
                self.stack2.append(stack1_popped)
                
        stack2_peeked = self.stack2[-1]
        return stack2_peeked 

    def empty(self) -> bool:
        return len(self.stack1) == len(self.stack2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()