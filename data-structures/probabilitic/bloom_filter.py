import hashlib

# Bloom Filter


class BloomFilter:
    """
    A Bloom filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set.
    False positive matches are possible (Value not added can return True),
    but false negatives are not (added value will always return True).
    Elements can be added to the set, but not removed (though this can be addressed with a counting filter).
    The more elements that are added to the set, the larger the probability of false positives.

    Use cases:
    - Check if an element is present in a set with  (e.g. spell checker, password checker, existing id checker)
    - If returns False, the element is definitely not in the set
    - When returns True, the element might be in the set -> check the database to confirm
    """

    def __init__(self, size: int, hash_count: int):
        self.size = (
            size  # size of the bit array that stores the filter (the hash values)
        )
        self.hash_count = hash_count  # number of hash functions to be used
        self.bit_array = [0] * size

    def _hash(self, item: str, i: int) -> int:
        # Combine the item with the index to generate a unique hash
        hash_input = f"{item}{i}".encode()
        return int(hashlib.md5(hash_input).hexdigest(), 16) % self.size

    def add(self, item: str) -> None:
        for i in range(self.hash_count):
            # hash(item, i) is a hash function that returns a unique integer for each item
            # i is used to vary the hash function across multiple iterations for generating different hash value for the same item
            digest = self._hash(item, i)
            self.bit_array[digest] = 1

    def check(self, item: str) -> bool:
        for i in range(self.hash_count):
            digest = self._hash(item, i)
            if self.bit_array[digest] == 0:
                return False
        return True

    def __str__(self):
        return str(self.bit_array)

    def __repr__(self):
        return str(self.bit_array)

    def __eq__(self, other):
        return self.bit_array == other.bit_array
