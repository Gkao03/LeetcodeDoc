# 01 Matrix
# Time: O(mn)
# Space: O(mn)
# Topics: Array, Dynamic Programming, Breadth-First Search, Matrix
# Difficulty: Medium

from collections import deque
from typing import List

class Solution:
    class Queue:
        def __init__(self):
            self.queue = deque()
            self.num_elements = 0
            
        def enqueue(self, x):
            self.queue.append(x)
            self.num_elements += 1
        
        def dequeue(self):
            try:
                dequeued = self.queue.popleft()
                self.num_elements -= 1
                return dequeued
            except IndexError:
                print("Cannot Dequeue from empty Queue!")
    
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        max_distance = m + n + 1
        nearest_mat = [[max_distance] * n for _ in range(m)]  # this fills with placeholder vals and also serves as "visited" matrix
        queue = self.Queue()
        
        # initialize for all 0's first
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val == 0:
                    nearest_mat[i][j] = 0
                    queue.enqueue((i, j))
                    
        while queue.num_elements != 0:
            curr_i, curr_j = queue.dequeue()
            
            # update shortest distance at current index
            adj_idxs = [(max(curr_i-1, 0), curr_j), (min(curr_i+1, m-1), curr_j), (curr_i, max(curr_j-1, 0)), (curr_i, min(curr_j+1, n-1))]
            distances = [nearest_mat[curr_i][curr_j]]
            for adj_idx in adj_idxs:
                adj_i, adj_j = adj_idx
                distances.append(nearest_mat[adj_i][adj_j] + 1)
                
            # get shortest distance
            nearest_mat[curr_i][curr_j] = min(distances)
            
            # add new adjacent indices to queue if not visited
            for adj_idx in adj_idxs:
                adj_i, adj_j = adj_idx
                if nearest_mat[adj_i][adj_j] == max_distance:  # not visited
                    queue.enqueue(adj_idx)
                    
        return nearest_mat
