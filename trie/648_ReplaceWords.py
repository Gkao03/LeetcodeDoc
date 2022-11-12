# Replace Words
# Time: O(m * max_len + N). m is number of words in sentence. max_len is longest word in dictionary. N is total characters in dictionary.
# Space: O(N)
# Topics: Array, Hash Table, String, Trie
# Difficulty: Medium

from typing import List

class Node:  # created class for a trie node
    def __init__(self):
        self.children = {}  # hashtable of children trie nodes
        self.is_end = False  # does the character mark the end of a word?


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr_node = self.root
        
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node()
            curr_node = curr_node.children[char]
        
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
            
        return curr_node.is_end  # True if end of word. False if not

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
            
        return True
    
    def contains_root(self, prefix, root_word):  # added this method for this specific question
        curr_node = self.root
        
        for char in prefix:
            if curr_node.is_end:
                return True
            
            if char not in curr_node.children:
                return False
            
            root_word.append(char)
            curr_node = curr_node.children[char]
            
        return curr_node.is_end


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")  # O(m) time to split
        
        trie = Trie()
        for d in dictionary:  # O(N) to insert all characters into dictionary
            trie.insert(d)
            
        output = []
        for word in words:
            root_word = []
            has_root = trie.contains_root(word, root_word)
            if has_root:
                output.append("".join(root_word))
            else:
                output.append(word)
                
        return " ".join(output)
