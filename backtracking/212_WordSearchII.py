# Word Search II
# Time: O(mn*3^s). m, n are dimensions of board. s is lenght of longest word in "words".
# Space: O(mn + sum(length of all words in "words")). need space to store Trie.
# Topics: Array, String, Backtracking, Trie, Matrix
# Difficulty: Hard

from typing import List

class Node:
    def __init__(self):
        self.children = {}  # hashtable
        self.is_end = False
            
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node()

            curr_node = curr_node.children[char]

        curr_node.is_end = True

    def search(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False

            curr_node = curr_node.children[char]

        return curr_node.is_end

class Solution:
    def dfs(self, i, j, curr_trie_node, curr_output, visited):
        visited[i][j] = True
        curr_output.append(self.board[i][j])
        
        found = False
        if curr_trie_node.is_end is True:
            self.output.add("".join(curr_output))
            found = True
            
        adj_dirs = [(i + di, j + dj) for di, dj in self.directions if 0 <= i + di < self.n and 0 <= j + dj < self.m]
        for adj_i, adj_j in adj_dirs:
            next_char = self.board[adj_i][adj_j]
            if not visited[adj_i][adj_j] and next_char in curr_trie_node.children:
                found = self.dfs(adj_i, adj_j, curr_trie_node.children[next_char], curr_output, visited)
                
                if found and len(curr_trie_node.children[next_char].children) == 0:  # pruning trie
                    curr_trie_node.children.pop(next_char)
                    
        visited[i][j] = False
        curr_output.pop()
        curr_trie_node.is_end = False
        
        return found
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.n, self.m = len(board), len(board[0])
        self.board = board
        self.output = set()
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        # init trie
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        root = trie.root
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_char = board[i][j]
                if curr_char in root.children:
                    found = self.dfs(i, j, root.children[curr_char], [], visited)
                    
                    if found and len(root.children[curr_char].children) == 0:  # pruning trie
                        root.children.pop(curr_char)
                        
        return self.output
