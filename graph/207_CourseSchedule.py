# Course Schedule
# Time: O(n+m) => O(n^2) if fully connected. n is number of courses (nodes). m is number of prereqs (edges)
# Space: O(n+m)
# Topics: Depth-First Search, Breadth-First Search, Graph, Topological Sort
# Difficulty: Medium
# Notes: This problem is equivalent to finding if a cycle exists in a directed graph. 
# If a cycle exists, no topological ordering exists (only DAGs can be top sorted) and 
# therefore it will be impossible to take all courses.

from collections import defaultdict
from typing import List

class Solution:
    def detect_cycle(self, node_val, visited, is_cycle):  # dfs to detect cycle (can also use bfs)
        if node_val in self.global_visited:
            self.global_visited.remove(node_val)
        
        if visited[node_val] is True:  # there is a cycle
            return True
        
        adj_node_vals = self.adj_list[node_val]
        new_visited = visited.copy()
        new_visited[node_val] = True
        
        for adj_node_val in adj_node_vals:
            if is_cycle is True:
                break
                
            if adj_node_val not in self.global_visited:  # this if condition is important to eliminate repeated visits (will reduce runtime)
                is_cycle = is_cycle or self.detect_cycle(adj_node_val, new_visited, is_cycle)
            
        return is_cycle

    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj_list = defaultdict(lambda: [])  # O(n+m) space ==> O(n^2) worst case if fully connected
        
        # example: [0, 1] means you have to take course 1 before course 0
        for prereq in prerequisites:
            course, pre_course = prereq
            self.adj_list[pre_course].append(course)
        
        self.global_visited = {*[i for i in range(numCourses)]}
        visited = [False] * numCourses
        
        cannot_finish = False

        while len(self.global_visited) > 0:
            curr_course = self.global_visited.pop()  # remove random course from set
            cannot_finish = cannot_finish or self.detect_cycle(curr_course, visited, False)  # cannot finish if cycle exists
            
        return not cannot_finish
