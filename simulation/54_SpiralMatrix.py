# Spiral Matrix
# Time: O(mn)
# Space: O(mn). need to store all elements of matrix to output
# Topics: Array, Matrix, Simulation
# Difficulty: Medium

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3
        curr_direction = RIGHT
        i_min = 0
        i_max = len(matrix) - 1
        j_min = 0
        j_max = len(matrix[0]) - 1
        curr_i = 0
        curr_j = 0
        output = []
        
        while i_min <= i_max and j_min <= j_max:
            output.append(matrix[curr_i][curr_j])
            
            if curr_direction == RIGHT:
                if curr_j == j_max:  # turn DOWN
                    i_min += 1
                    curr_i += 1
                    curr_direction = DOWN
                else:  # continue RIGHT
                    curr_j += 1
            elif curr_direction == DOWN:
                if curr_i == i_max:  # turn LEFT
                    j_max -= 1
                    curr_j -= 1
                    curr_direction = LEFT
                else:  # continue DOWN
                    curr_i += 1
            elif curr_direction == LEFT:
                if curr_j == j_min:  # turn UP
                    i_max -= 1
                    curr_i -= 1
                    curr_direction = UP
                else:  # continue LEFT
                    curr_j -= 1
            elif curr_direction == UP:
                if curr_i == i_min:  # turn RIGHT
                    j_min += 1
                    curr_j += 1
                    curr_direction = RIGHT
                else:  # continue UP
                    curr_i -= 1
        
        return output
