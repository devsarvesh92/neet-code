from hashlib import md5


class Node:
    def __init__(self, key, val, nxt) -> None:
        self.key = key
        self.val = val
        self.nxt = nxt


class HashTable:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def _get_index(self, key, capacity) -> int:
        hashed_val = md5(str(key).encode("UTF-8")).hexdigest()
        return int(hashed_val, 16) % capacity

    def insert(self, key: int, value: int) -> None:
        hashval = self._get_index(key=key, capacity=self.capacity)
        node = self.table[hashval]
        prev = None
        if node:
            while node:
                prev = node
                if node.key == key:
                    node.val = value
                    return
                node = node.nxt
            prev.nxt = Node(key=key, val=value, nxt=None)
            self.size += 1
        else:
            self.table[hashval] = Node(key=key, val=value, nxt=None)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self._get_index(key=key, capacity=self.capacity)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.val
            node = node.nxt
        return -1

    def remove(self, key: int) -> None:
        index = self._get_index(key=key, capacity=self.capacity)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.nxt = node.nxt
                    del node
                    self.size -= 1
                    return True
                else:
                    self.table[index] = node.nxt
                    del node
                    self.size -= 1
                    return True
            prev = node
            node = node.nxt
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self):
        new_cap = self.capacity * 2
        new_table = [None] * new_cap

        for node in self.table:
            while node:
                new_index = self._get_index(key=node.key, capacity=new_cap)
                n_node = new_table[new_index]
                if n_node is None:
                    new_table[new_index] = Node(key=node.key, val=node.val, nxt=None)
                else:
                    nxt_node = n_node.nxt
                    new_node = Node(key=node.key, val=node.val, nxt=nxt_node)
                    n_node.nxt = new_node
                node = node.nxt
        self.table = new_table
        self.capacity = new_cap


if __name__ == "__main__":
    h = HashTable(capacity=4)
    h.insert(1, 1)
    h.insert(2, 2)
    h.insert(3, 3)
    h.insert(4, 4)
    h.getCapacity()
    h.insert(5, 5)
    h.get(1)
    h.get(2)
    h.get(3)
    h.get(4)
    # [
    #     "getCapacity",
    #     "get",
    #     1,
    #     "get",
    #     2,
    #     "get",
    #     3,
    #     "get",
    #     4,
    #     "get",
    #     5,
    #     "remove",
    #     1,
    #     "remove",
    #     2,
    #     "remove",
    #     3,
    #     "remove",
    #     4,
    #     "remove",
    #     5,
    #     "getSize",
    # ]
