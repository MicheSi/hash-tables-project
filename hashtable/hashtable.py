class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        self.length = len(self.storage)
        return self.length


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.size / self.length


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_Prime = 1099511628211
        FNV_offset_basis = 14695981039346656037

        hash = FNV_offset_basis

        for char in key:
            hash = hash * FNV_Prime
            hash = hash ^ ord(char)
        
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # No Collisions
        # slot = self.hash_index(key)
        # self.storage[slot] = HashTableEntry(key, value)

        # With Collisions
        self.size += 1

        slot = self.hash_index(key)
        cur = self.storage[slot]

        if cur is None:
            self.storage[slot] = HashTableEntry(key, value)
            return
        
        prev = cur

        while cur is not None and cur.key != key:
            prev = cur
            cur = cur.next
        prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # No Collisions
        # if key is None:
        #     print(f'{key} not found')
        # else:
        #     self.put(key, None)

        # With Collisions
        index = self.hash_index(key)
        cur = self.storage[index]

        if cur.key == key:
            self.storage[index] = cur.next
            return cur

        prev = cur
        cur = cur.next

        while cur is not None and cur.key != key:
            prev = cur
            cur = cur.next
        if cur is None:
            print(f'{key} is not found')
            return None
        else:
            self.size -= 1
            prev.next = cur.next



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # No Collisions
        # slot = self.hash_index(key)
        # hash_entry = self.storage[slot]

        # if hash_entry is not None:
        #     return hash_entry.value

        # return None

        # With Collisions
        index = self.hash_index(key)

        cur = self.storage[index]

        while cur is not None and cur.key != key:
            cur = cur.next

        if cur is None:
            return None
        else:
            return cur.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # create new bigger table
        self.capacity = new_capacity
        new_HT = [None] * self.capacity

        # go through current list
        for i in range(len(self.storage)):
            cur = self.storage[i]

            while cur is not None:
                new_slot = self.hash_index(cur.key)
                new_HT[new_slot] = cur
                cur = cur.next

        self.storage = new_HT
        
            



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
