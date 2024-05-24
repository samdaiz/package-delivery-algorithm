# Hash Chaining class with insert, remove, and search methods
# Source: Zybooks textbook - Data Structures and Algorithms II
class HashMap:

    # Constructor creates hash table with empty indices
    # runtime: O(N) - linear
    def __init__(self, initial_capacity=10):
        self.hash_table = []
        for i in range(initial_capacity):
            self.hash_table.append([])

    # insert/update a given item into the hash table
    # runtime: O(N) - linear
    def insert(self, key, item):
        # obtain the appropriate bucket where the item is located
        bucket = hash(key) % len(self.hash_table)
        bucket_list = self.hash_table[bucket]

        # if the key is already in the bucket... update
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = item
                return True

        # if the key is not already in the bucket...
        # insert item at the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # searches for a given item within the hash chaining table
    # runtime: O(N) - linear
    def lookup(self, key):
        # obtain the appropriate bucket where the item is located
        bucket = hash(key) % len(self.hash_table)
        bucket_list = self.hash_table[bucket]

        # if the key is found... return the item
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]  # value

        # else, the item is not found, return None
        return None
