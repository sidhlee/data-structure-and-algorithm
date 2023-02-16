def array_manipulation_brute_force(n, queries):
    """
    exceeds memory limit
    """
    arr = [0] * n
    for start, end, add in queries:
        arr[start - 1 : end] = map(lambda x: x + add, arr[start - 1 : end])
    return max(arr)


def array_manipulation_hashmap(n, queries):
    """
    too slow
    """
    indexes = {}
    mx = 0
    for a, b, k in queries:
        for i in range(a, b + 1):
            if i in indexes:
                indexes[i] += k
            else:
                indexes[i] = k
            mx = max(mx, indexes[i])
    return mx


def array_manipulation_optimized(n, queries):
    """
    if current range overlaps with prev range
    > take max from overlapping part
    if not:
        if k <= current max, skip
        if k > current max, reset max

    keep max at each layer
    -> no. if next layer adds 1M to a random position, we need
    to know the existing value at that position.

    What if we start with sorted queries by k desc?
    -> no. we have to also consider the position k is accumulated at.

    What if we add to the dict selectively?
    """
    indexes = {}
    mx = 0
    for a, b, k in queries:
        for i in range(a, b + 1):
            if i in indexes:
                indexes[i] += k
            else:
                indexes[i] = k
            mx = max(mx, indexes[i])
    return mx


def array_manipulation_prefix_sum(n, queries):
    """
    2023-02-13 07:36:54
    Did not pass the time limit
    """
    arr = [0] * n
    for a, b, k in queries:
        arr[a - 1] += k
        if b < n:
            arr[b] -= k
    mx = 0
    for i in range(1, n):
        # writing and reading from array is not free
        arr[i] = arr[i - 1] + arr[i]
        mx = max(mx, arr[i])
    return mx


def array_manipulation_prefix_sum_optimized(n, queries):
    """
    2023-02-13 07:40:52
    """
    arr = [0] * n
    for a, b, k in queries:
        arr[a - 1] += k
        if b < n:
            arr[b] -= k
    mx = 0
    acc = 0
    for v in arr:
        # much cheaper to update a number than a list
        acc += v
        mx = max(mx, acc)
    return mx


array_manipulation = array_manipulation_prefix_sum_optimized
