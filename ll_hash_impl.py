# Caleb Barger Aug 4 2020

# Node implementation here
class Node:
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

    def __str__(self):
        rs = f"({self.key}, {self.value})"
        while self.next_node:
            rs += f" --> ({self.next_node.key}, {self.next_node.value})"
            self = self.next_node
        return rs

# HashMap implementation here
class HashMap:
    def __init__(self, inital_size=40):
        # self.data = [new Node()] * inital_size
        self.item_count = 0
        self.data = [None] * inital_size
        
        for i in range(inital_size):
            self.data[i] = Node()

    def get_length(self):
        return len(self.data)

    def _hash_FNV1a(self, key):
        OFFSET_BASIS = 14695981039346656037
        FNV_PRIME = 1099511628211

        the_hash = OFFSET_BASIS
        bts = key.encode()

        for b in bts:
            the_hash = the_hash ^ b
            the_hash = the_hash * FNV_PRIME

        return the_hash % self.get_length() # returns the insertion index

    def _load_OK(self):
        print(self.item_count/len(self.data))
        if (self.item_count/len(self.data) > 0.7):
            return False
        return True

    def insert(self, key, value):
        # get the index that we want to insert into
        index = self._hash_FNV1a(key) 
        
        # store a refrence to the current node
        # and perv node, (initalizing it to some arb value)
        cur = self.data[index]
        # prev = cur

        # if there are currently more nodes to traverse 
        while cur.next_node is not None:
            # than we want to step through until we reach the last node
            # prev = cur
            cur = cur.next_node
        
        # if there was more than one node transversed than
        if not cur.next_node and cur.key:
            # prev.next_node = cur
            # cur.key = key
            # cur.value = value
            cur.next_node = Node(key, value)
        
        # otherwise this is the first node being stored
        else:
            cur.key = key
            cur.value = value

    def lookup(self, key):
        index = self._hash_FNV1a(key)

        while not self.data[index].get_next():
            if key == self.data[index].get_key():
                return self.data[index].get_value()
            else:
                index += 1
        
        if self.data[index].get_key() == key:
            return self.data[index].get_value()

        return None

hm = HashMap(1)

hm.insert("A", "1")
hm.insert("B", "2")
hm.insert("C", "3")
hm.insert("D", "4")
hm.insert("E", "5")
hm.insert("F", "6")
hm.insert("G", "7")
hm.insert("H", "8")
hm.insert("I", "9")
hm.insert("J", "10")


print(hm._load_OK())

for s in hm.data:
    print(s)




    
