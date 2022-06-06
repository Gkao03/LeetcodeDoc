# Flood Fill
# Time: O(mn)
# Space: O(mn)
# Topics: Array, Depth-First Search, Breadth-First Search, Matrix
# Difficulty: Easy
# Notes: can use queue for BFS. implementation uses stack for DFS

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        num_rows = len(image)
        num_cols = len(image[0])
        
        visited = [[False] * num_cols for _ in range(num_rows)]
        stack = []  # holds points to be visited
        
        start_color = image[sr][sc]
        stack.append((sr, sc))
        
        while len(stack) != 0:
            curr_row, curr_col = stack.pop()
            if visited[curr_row][curr_col]:
                continue
            
            # down
            if curr_row + 1 < num_rows and not visited[curr_row + 1][curr_col] and image[curr_row + 1][curr_col] == start_color:
                stack.append((curr_row + 1, curr_col))
                
            # left
            if curr_col - 1 >= 0 and not visited[curr_row][curr_col - 1] and image[curr_row][curr_col - 1] == start_color:
                stack.append((curr_row, curr_col - 1))
                
            # up
            if curr_row - 1 >= 0 and not visited[curr_row - 1][curr_col] and image[curr_row - 1][curr_col] == start_color:
                stack.append((curr_row - 1, curr_col))
                
            # right
            if curr_col + 1 < num_cols and not visited[curr_row][curr_col + 1] and image[curr_row][curr_col + 1] == start_color:
                stack.append((curr_row, curr_col + 1))
                
            visited[curr_row][curr_col] = True
            image[curr_row][curr_col] = newColor
            
        return image                
