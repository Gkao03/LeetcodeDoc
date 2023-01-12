# LFU Cache
# Time: O(1) per "get" and "put" operation
# Space: O(n) for n "put" operations
# Topics: Hash Table, Linked List, Design, Doubly-Linked List
# Difficulty: Hard

# general doubly linked list node
class ListNode:
    def __init__(self, key=None, val=None, use_counter=1):
        self.key = key
        self.val = val
        self.use_counter = use_counter
        self.next_lnode = None
        self.prev_lnode = None


# frequency node to store frequency of a key
class FreqNode(ListNode):
    def __init__(self, frequency):
        super().__init__(use_counter=frequency)
        self.next_fnode = None
        self.prev_fnode = None


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_nodes = {}  # frequency: [ListNode, ListNode] head/tail
        self.cache = {}  # key: ListNode
        self.head_freqnode = None
        self.tail_freqnode = None

    def evict_lfu(self):
        lfu_node = self.head_freqnode.next_lnode
        lfu_key = lfu_node.key
        self.cache.pop(lfu_key)

        prev_listnode = lfu_node.prev_lnode
        next_listnode = lfu_node.next_lnode
        prev_listnode.next_lnode = next_listnode
        if next_listnode is not None:
            next_listnode.prev_lnode = prev_listnode

        if self.head_freqnode.next_lnode is None:  # need to remove and update head/tail
            lfu_freq = self.head_freqnode.use_counter
            next_freqnode = self.head_freqnode.next_fnode

            if next_freqnode is not None:
                next_freqnode.prev_fnode = None

            self.head_freqnode = next_freqnode
            if self.head_freqnode is None:
                self.tail_freqnode = None

            self.freq_nodes.pop(lfu_freq)

    def update_lfucache(self, key):
        curr_listnode = self.cache[key]
        curr_freqnode = self.freq_nodes[curr_listnode.use_counter][0]
        next_freq = curr_listnode.use_counter + 1

        # remove list node from list node chain. update freq node hash map
        prev_listnode = curr_listnode.prev_lnode
        next_listnode = curr_listnode.next_lnode

        prev_listnode.next_lnode = next_listnode
        if next_listnode is not None:
            next_listnode.prev_lnode = prev_listnode

        if curr_listnode is self.freq_nodes[curr_listnode.use_counter][1]:
            self.freq_nodes[curr_listnode.use_counter][1] = prev_listnode
            
        # if freq node exists, add to chain
        if next_freq in self.freq_nodes:
            _, tail_listnode = self.freq_nodes[next_freq]
            tail_listnode.next_lnode = curr_listnode
            curr_listnode.prev_lnode = tail_listnode
            curr_listnode.next_lnode = None
            self.freq_nodes[next_freq][1] = curr_listnode  # update the tail node
        else:  # freq node does not exist
            # create a new freq node and add updated node
            new_freqnode = FreqNode(next_freq)
            new_freqnode.next_lnode = curr_listnode
            curr_listnode.prev_lnode = new_freqnode
            curr_listnode.next_lnode = None
            self.freq_nodes[next_freq] = [new_freqnode, curr_listnode]

            next_freqnode = curr_freqnode.next_fnode
            curr_freqnode.next_fnode = new_freqnode
            new_freqnode.prev_fnode = curr_freqnode
            new_freqnode.next_fnode = next_freqnode
            if next_freqnode is not None:
                next_freqnode.prev_fnode = new_freqnode
        
        # update tail freq nodes
        if self.tail_freqnode.next_fnode is not None:
            self.tail_freqnode = self.tail_freqnode.next_fnode

        # update head freqnode if needed
        if self.head_freqnode.next_lnode is None:  # move the head freq node
            self.head_freqnode = self.head_freqnode.next_fnode

        # remove the curr_freqnode if no list nodes attached to chain
        if curr_freqnode.next_lnode is None:
            prev_freqnode = curr_freqnode.prev_fnode
            next_freqnode = curr_freqnode.next_fnode
            next_freqnode.prev_fnode = prev_freqnode
            if prev_freqnode is not None:
                prev_freqnode.next_fnode = next_freqnode

            # remove key from freq node hash map
            self.freq_nodes.pop(curr_listnode.use_counter)

        # update use count
        curr_listnode.use_counter += 1

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_lfucache(key)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self.update_lfucache(key)
            self.cache[key].val = value
            return

        if len(self.cache) >= self.capacity:
            self.evict_lfu()

        # add a new listnode (and freqnode if needed)
        new_listnode = ListNode(key, value)
        self.cache[key] = new_listnode

        if 1 in self.freq_nodes:
            _, tail_listnode = self.freq_nodes[1]
            tail_listnode.next_lnode = new_listnode
            new_listnode.prev_lnode = tail_listnode
            self.freq_nodes[1][1] = new_listnode
        else:  # 1 not in freq node hash map
            new_freqnode = FreqNode(1)
            new_freqnode.next_lnode = new_listnode
            new_listnode.prev_lnode = new_freqnode
            self.freq_nodes[1] = [new_freqnode, new_listnode]

            new_freqnode.next_fnode = self.head_freqnode
            if self.head_freqnode is not None:
                self.head_freqnode.prev_fnode = new_freqnode

            self.head_freqnode = new_freqnode
            if self.tail_freqnode is None:
                self.tail_freqnode = self.head_freqnode


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)