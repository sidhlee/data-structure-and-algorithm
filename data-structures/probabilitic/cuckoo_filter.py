import random


class CuckooFilter:
    """
    Cuckoo Filter is a probabilistic data structure that is used to test whether an element is a member of a set.
    False positive matches are possible (Value not added can return True),
    but false negatives are not (added value will always return True).
    Elements can be added to the set, but not removed (though this can be addressed with a counting filter).
    The more elements that are added to the set, the larger the probability of false positives.

    Cuckoo Filter is different from Bloom Filter in that it supports deletion of elements.

    When to Prefer Cuckoo Filter
    - Deletions: If you need to support deletions, a Cuckoo filter is a better choice. Bloom filters do not support deletions efficiently, whereas Cuckoo filters can handle deletions by removing the fingerprint from the appropriate bucket.
    - Lower False Positive Rate: Cuckoo filters can achieve a lower false positive rate for the same amount of space compared to Bloom filters. This is because Cuckoo filters use a more sophisticated hashing and placement strategy.
    - Dynamic Resizing: If you need to dynamically resize the filter, Cuckoo filters can be resized more easily than Bloom filters. Bloom filters require a complete rebuild to resize, while Cuckoo filters can be resized by rehashing and redistributing the elements.
    - Counting: If you need to count the number of occurrences of an element, Cuckoo filters can be extended to support counting, whereas Bloom filters require a separate counting Bloom filter, which is more complex and space-consuming.
    - Space Efficiency: For certain configurations and workloads, Cuckoo filters can be more space-efficient than Bloom filters, especially when the false positive rate needs to be very low.

    Example Use Cases for Cuckoo Filter
    - Network Security: In network security applications, where you need to quickly insert, query, and delete IP addresses or URLs, a Cuckoo filter is advantageous due to its support for deletions and lower false positive rate.
    - Database Indexing: For database indexing, where entries might need to be removed or updated frequently, a Cuckoo filter's ability to handle deletions and dynamic resizing makes it a better choice.
    - Cache Management: In cache management systems, where items are frequently added and removed, a Cuckoo filter's support for deletions and efficient space usage can improve performance.
    """

    def __init__(self, capacity, bucket_size, max_kicks):
        self.capacity = capacity
        self.bucket_size = bucket_size
        self.max_kicks = max_kicks
        self.buckets = [None] * capacity
        self.size = 0

    def insert(self, key):
        if self.contains(key):
            return False

        if self.size >= self.capacity:
            return False

        idx1 = self.hash1(key)
        idx2 = self.hash2(key, idx1)

        if self.buckets[idx1] is None:
            self.buckets[idx1] = [None] * self.bucket_size
            self.buckets[idx1][0] = key
            self.size += 1
            return True

        if self.buckets[idx2] is None:
            self.buckets[idx2] = [None] * self.bucket_size
            self.buckets[idx2][0] = key
            self.size += 1
            return True

        idx = idx1
        for _ in range(self.max_kicks):
            i = random.randint(0, self.bucket_size - 1)
            key, self.buckets[idx][i] = self.buckets[idx][i], key
            idx = idx1 if idx == idx2 else idx2

            if key is None:
                self.size += 1
                return True

            idx = idx1 if idx == idx2 else idx2

        return False

    def delete(self, key):
        idx1 = self.hash1(key)
        idx2 = self.hash2(key, idx1)

        if self.buckets[idx1] is not None and key in self.buckets[idx1]:
            self.buckets[idx1].remove(key)
            self.size -= 1
            return True

        if self.buckets[idx2] is not None and key in self.buckets[idx2]:
            self.buckets[idx2].remove(key)
            self.size -= 1
            return True

        return False

    def contains(self, key):
        idx1 = self.hash1(key)
        idx2 = self.hash2(key, idx1)

        return (
            self.buckets[idx1] is not None
            and key in self.buckets[idx1]
            or self.buckets[idx2] is not None
            and key in self.buckets[idx2]
        )

    def hash1(self, key):
        return hash(key) % self.capacity

    def hash2(self, key, idx1):
        return (idx1 ^ hash(key)) % self.capacity

    def __str__(self):
        return str(self.buckets)

    def __repr__(self):
        return str(self.buckets)
