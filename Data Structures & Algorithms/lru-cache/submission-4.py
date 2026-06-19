class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to nodes

        self.left = Node(0, 0) # least recent used
        self.right = Node(0, 0) # most recent used
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node): # remove from left
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node): # insert from right
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # TODO: update the most recent used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from list and delete LRU from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
