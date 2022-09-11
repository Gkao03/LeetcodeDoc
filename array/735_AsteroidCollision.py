# Asteroid Collision
# Time: O(n)
# Space: O(n)
# Topics: Array, Stack
# Difficulty: Medium

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # input asteroids will not have 0 int
        output = []
        pos_asteroid_stack = []
        
        asteroid_idx = 0
        while asteroid_idx < len(asteroids):
            asteroid = asteroids[asteroid_idx]
            
            if asteroid < 0 and len(pos_asteroid_stack) == 0:
                output.append(asteroid)
                asteroid_idx += 1
            elif asteroid > 0:
                pos_asteroid_stack.append(asteroid)
                asteroid_idx += 1
            else:  # asteroid is negative and positive stack is not empty
                if abs(asteroid) > pos_asteroid_stack[-1]:
                    pos_asteroid_stack.pop()
                elif pos_asteroid_stack[-1] > abs(asteroid):
                    asteroid_idx += 1
                else:  # asteroids have same size
                    pos_asteroid_stack.pop()
                    asteroid_idx += 1
                    
        output.extend(pos_asteroid_stack)
        return output
