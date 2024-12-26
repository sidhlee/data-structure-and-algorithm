# Log-Structured Merge-Tree (LSM-Tree)

A Log-Structured Merge-Tree (LSM-Tree) is a data structure that is used to store and manage large amounts of data efficiently. It is commonly used in database systems to provide fast read and write access to data.

The LSM-Tree is composed of two main components: a memory buffer and a set of disk-based storage structures. The memory buffer is used to store incoming data writes before they are flushed to disk. The disk-based storage structures are used to store the data in a way that allows for efficient read and write access.

The LSM-Tree works by using a technique called log-structuring, where data is written to disk sequentially in a log-like fashion. This allows for fast write access, as data can be written to disk in a single sequential write operation. When the memory buffer is full, the data is flushed to disk and merged with the existing data in the disk-based storage structures.

The disk-based storage structures in an LSM-Tree typically consist of multiple levels of sorted files, with each level containing files of increasing size. When data is written to the LSM-Tree, it is first written to the memory buffer and then flushed to the first level of the disk-based storage structures. As data is merged and compacted, it is moved to higher levels of the storage structures.

The LSM-Tree provides fast read access by using a technique called bloom filters, which are used to quickly determine if a key exists in the LSM-Tree. When a read request is made, the bloom filters are used to check if the key exists in the LSM-Tree. If the key is found, the LSM-Tree is searched for the key in the disk-based storage structures.

Overall, the LSM-Tree is a powerful data structure that provides efficient read and write access to large amounts of data. It is commonly used in database systems to provide fast access to data and is an important component of many modern database systems.

## References

- [Wikipedia - Log-structured merge-tree](https://en.wikipedia.org/wiki/Log-structured_merge-tree)
- [Youtube - The Secret Sauce Behind NoSQL: LSM Tree](https://www.youtube.com/watch?v=I6jB0nM9SKU)
- [Cockroach Labs - LSM Tree](https://www.cockroachlabs.com/docs/stable/architecture/rocksdb.html#lsm-tree)
