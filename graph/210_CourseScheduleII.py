# Course Schedule II
# Time: O(n+m) => n is number of courses (nodes). m is number of prereqs (edges)
# Space: O(n+m)
# Topics: Depth-First Search, Breadth-First Search, Graph, Topological Sort
# Difficulty: Medium

from typing import List
from collections import defaultdict

class Solution:
    def topological_sort(self, visited, curr_course, curr_output):
        visited[curr_course] = True
        
        for next_course in self.adj_list[curr_course]:
            if not self.global_visited[next_course]: 
                if visited[next_course] is True:
                    visited[curr_course] = False
                    self.global_visited[curr_course] = True
                    return True
                is_cycle = self.topological_sort(visited, next_course, curr_output)
                if is_cycle is True:
                    return True
            
        visited[curr_course] = False
        self.global_visited[curr_course] = True
        curr_output.append(curr_course)
        return False
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.adj_list = defaultdict(lambda: [])
        
        for prereq in prerequisites:
            course, pre_course = prereq
            self.adj_list[pre_course].append(course)
                
        # topological sort
        self.global_visited = [False] * numCourses
        output = []
        for i in range(len(self.global_visited)):
            if not self.global_visited[i]:
                curr_output = []
                is_cycle = self.topological_sort([False] * numCourses, i, curr_output)
                if is_cycle is True:
                    output = []
                    break
                output.extend(curr_output)
        output.reverse()
                    
        return output
