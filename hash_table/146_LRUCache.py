# LRU Cache
# Time: O(n) for n operations. O(1) per operation. get and put are O(1)
# Space: O(n) where n is the capacity
# Topics: Hash Table, Linked List, Design, Doubly-Linked List
# Difficulty: Medium

class LRUCache:
    class ListNode:  # Node for doubly linked list
        def __init__(self, key, val, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = next
            

    def __init__(self, capacity: int):
        self.cache = {}  # stores key: key_node
        self.capacity = capacity
        self.head = None
        self.tail = None
        

    def get(self, key: int) -> int:
        if key in self.cache:
            key_node = self.cache[key]
            val = key_node.val
            
            # update LRU
            if self.head is not self.tail and self.tail is not key_node:  # more than 1 object in cache and not most recent
                prev_node = key_node.prev
                next_node = key_node.next
                
                if self.head is key_node:  # key node is at the head
                    next_node.prev = None
                    self.head = next_node
                else:  # somewhere in middle and not at end
                    next_node.prev = prev_node
                    prev_node.next = next_node
                    
                self.tail.next = key_node
                key_node.prev = self.tail
                key_node.next = None
                self.tail = key_node
            
            return val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # exists so just update val and LRU
            key_node = self.cache[key]
            key_node.val = value
            
            # update LRU
            if self.head is not self.tail and self.tail is not key_node:  # more than 1 object in cache and not most recent
                prev_node = key_node.prev
                next_node = key_node.next
                
                if self.head is key_node:  # key node is at the head
                    next_node.prev = None
                    self.head = next_node
                else:  # somewhere in middle and not at tail
                    next_node.prev = prev_node
                    prev_node.next = next_node
                    
                self.tail.next = key_node
                key_node.prev = self.tail
                key_node.next = None
                self.tail = key_node
        else:  # does not exist
            if len(self.cache) < self.capacity:  # room to fit in cache
                new_key_node = self.ListNode(key, value)
                self.cache[key] = new_key_node
                
                if self.head is None and self.tail is None:  # empty cache
                    self.head = new_key_node
                    self.tail = new_key_node
                else:  # cache contains at least 1 item
                    self.tail.next = new_key_node
                    new_key_node.prev = self.tail
                    self.tail = new_key_node
            else:  # no room in cache, evict from LRU. head holds LRU
                new_key_node = self.ListNode(key, value)
                self.cache[key] = new_key_node
                
                evict_key = self.head.key
                self.cache.pop(evict_key)
                
                # add new key node to end of LRU
                self.tail.next = new_key_node
                new_key_node.prev = self.tail
                self.tail = new_key_node
                
                # evict the head and update head
                self.head = self.head.next
                self.head.prev = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
