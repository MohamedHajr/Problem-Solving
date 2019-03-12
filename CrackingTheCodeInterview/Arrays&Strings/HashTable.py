class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class HashTable:
    def __init__(self, length):
        self.length = length
        self.store = [None] * length

    # core functionality
    def add(self, key, value):
        new_node = Node(key, value)
        key_hash = self.gen_hash(key)
        bucket = self.store[key_hash]
        if not bucket:
            self.store[key_hash] = new_node
        else:
            self.append_to_ll(bucket, new_node)

    def get(self, key):
        key_hash = self.gen_hash(key)
        bucket = self.store[key_hash]
        if not bucket:
            return -1
        else:
            while bucket:
                if bucket.key == key:
                    return bucket.val
                bucket = bucket.next
            return -1

    # helpers
    def get_key_sum(self, key):
        return sum([ord(x) for x in key])

    def gen_hash(self, key):
        return self.get_key_sum(key) % self.length

    def append_to_ll(self, head, node):
        while not head.next:
            head = head.next
        head.next = node


hash_table = HashTable(1000)
hash_table.add('wait what', 'destroying yo all...')
hash_table.add('a7a', 'al shbshb da3')
print(hash_table.get('wait what'))
print(hash_table.get('a7a'))
