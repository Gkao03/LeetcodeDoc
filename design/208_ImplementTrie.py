# Implement Trie (Prefix Tree)
# Time: O(k) insert, search, insert. k is length of the word
# Space: O(k) insert. O(1) search, startsWith. 
# For the entire tree => O(alphabet_size * avg_key_len * N) where N is number of words in trie
# Topics: Hash Table, String, Design, Trie
# Difficulty: Medium

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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
