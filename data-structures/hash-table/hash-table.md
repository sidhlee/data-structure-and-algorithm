# Hash Table

Hash tables are used to store key/value pairs. Unlike arrays, hash tables provide O(1) search, insertion, and deletion for average case, and O(n) for [the worst cases](https://stackoverflow.com/a/9214594).

- It uses hash function to hash keys and store them in a fixed size array.
- A good hash should be deterministic, distribute keys uniformly, and be fast.
- **Separate chaining** and **linear probing** are two strategies to deal with hash collision.

## Hash Functions

A hash function converts keys into a valid indices to store data into an array.

- Python exposes a built-in `hash` function.

In order to be a good hash function, it must:

- be fast (constant time)
- don't cluster outputs at specific indices, but distribute uniformly
- deterministic (the same input always results in the same output)

## Handling Collisions

### Separate Chaining

Separate Chaining stores values that have the same hashed key value in the nested data structure (eg. array) within the array.

### Linear Probing

With Linear Probing, we search the next empty spot upon collision. This allow us to keep the array normalized.

## Language Implementations

### JavaScript

If you need a _guaranteed_ insertion order on an object, use `Map` instead.

> **Current Language Spec (since ES2015)**
> insertion order is preserved, except in the case of keys that parse as integers (eg "7" or "99"), where behavior varies between browsers. For example, Chrome/V8 does not respect insertion order when the keys are parse as numeric.
> **Old Language Spec (before ES2015)**:
> Iteration order was technically undefined, but all major browsers complied with the ES2015 behavior.

### Python

TODO: add python hash-table implementation details
