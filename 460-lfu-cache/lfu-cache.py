class Node:
    def __init__(self, key, value, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_tail(self):
        if self.tail.prev == self.head:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node

    def is_empty(self):
        return self.head.next == self.tail

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.node_map = {}  # key → node
        self.freq_map = defaultdict(DoublyLinkedList)  # freq → DLL of nodes

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._update(node)
        else:
            if len(self.node_map) == self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                evicted = lfu_list.pop_tail()
                del self.node_map[evicted.key]
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.freq_map[1].insert_at_head(new_node)
            self.min_freq = 1
    
    def _update(self, node):
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        if self.freq_map[freq].is_empty():
            if freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq].insert_at_head(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)