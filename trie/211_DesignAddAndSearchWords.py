# Design Add and Search Words Data Structure
# Time: O(n) to addWord. O((26^3)n) to search. n is length of word
# Space: O(26^25) -> O(1) still constant
# Topics: String, Depth-First Search, Design, Trie
# Difficulty: Medium
# Notes: There are at most 3 dots in a search query string. The input word
# length is at most 25 characters. Since these are defined constants, the
# search and space complexity is techincally still O(n) and O(1) respectively.

class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}  # hashmap
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = self.TrieNode()
            curr_node = curr_node.children[char]
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        curr_node = self.root
                
        def search_helper(start_word_idx, curr_node):  # dfs
            for i in range(start_word_idx, len(word)):
                char = word[i]

                if char == '.':
                    for next_char in curr_node.children:                    
                        if search_helper(i + 1, curr_node.children[next_char]) is True:
                            return True
                    return False
                else:  # is an alphabet character
                    if char not in curr_node.children:
                        return False
                    curr_node = curr_node.children[char]

            return curr_node.is_end
        
        return search_helper(0, curr_node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
