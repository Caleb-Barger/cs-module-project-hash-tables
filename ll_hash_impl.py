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
    def __init__(self, inital_size=20):
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
            cur = cur.next_node
        
        # if there was more than one node transversed than
        if not cur.next_node and cur.key:

            if cur.key == key:
                cur.value = value
                return

            self.item_count += 1
            cur.next_node = Node(key, value)
        
        # otherwise this is the first node being stored
        else:
            self.item_count += 1
            cur.key = key
            cur.value = value

    def lookup(self, key):
        # get the index of the key
        index = self._hash_FNV1a(key)
        
        # store a refrence to the current node
        cur = self.data[index]

        # check if the cur node's key matches
        if cur.key == key:
            # if it does return its value
            return cur.value

        # otherwise check if there are other nodes
        while cur.next_node:
            # if there are assign the cur node to the next node
            cur = cur.next_node
            if cur.key == key:
                return cur.value

        return None

    def __str__(self):
        rs = ""
        for n in self.data:
            rs += n.__str__() + "\n"
        return rs

hm = HashMap(5)

hm.insert("caleb", 18)
hm.insert("jameie", 46) # will overwrite the node
hm.insert("kevin", 47)
hm.insert("cam", 16)
hm.insert("caryss", 12)
hm.insert("dan", 18)
hm.insert("jim", 46) # will overwrite the node
hm.insert("jemmmy", 47)
hm.insert("sarahs", 16)
hm.insert("trey", 12)
hm.insert("Kyle", 18)
hm.insert("Nathan", 46) # will overwrite the node
hm.insert("Quinn", "HALL")
hm.insert("Etahn", 16)
hm.insert("Farkis", 12)

print(f"LOAD FACTOR OK - {hm._load_OK()}")

print(hm.lookup("Quinn")) # should now be 46

print(hm)





    
