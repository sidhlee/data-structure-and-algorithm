# Probabilistic Data Structures

## 1. Bloom Filter

- **What**: Test membership of an element
- **How**: Uses hash functions to map elements to a bit array
- **Why**: Space efficient
- **Where**: Database, web cache, network routers

## 2. Cuckoo Filter

- **What**: Test membership of an element
- **How**: Uses cuckoo hashing and a table of buckets to store the fingerprints of elements
- **Why**: Supports deletion and has better performance in certain cases
- **Where**: Databases, networking

## 3. HyperLogLog

- **What**: Counting the number of unique elements
- **How**: Uses hash functions and an algorithm to estimate the number of unique elements
- **Why**: Space efficient
- **Where**: Big data analytics, network traffic analysis

## 4. Count-Min Sketch

- **What**: Frequency estimation of events in data streams
- **How**: Uses hash functions to map elements to a 2D array and increments counters
- **Why**: Space efficient
- **Where**: Network monitoring, search engines, databases

## 5. MinHash

- **What**: Estimating similarity between sets
- **How**: Applies hash functions to elements of sets to produce signatures
- **Why**: Space efficient and useful for large-scale similarity computations
- **Where**: Document similarity, duplicate detection, clustering

## 6. Skip List

- **What**: Ordered data structure with fast search, insertion, and deletion operations
- **How**: Uses a layered linked list where each layer skips over a fixed number of elements
- **Why**: Easier to set up than balanced trees and logarithmic performance
- **Where**: Memory management, databases
