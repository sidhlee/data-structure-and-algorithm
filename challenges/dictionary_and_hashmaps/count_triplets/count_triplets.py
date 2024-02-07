from math import factorial


def countTriplets_first_try(arr, r):
    """
    Only works for sorted array.
    """
    nums = {}
    for val in arr:
        nums[val] = nums[val] + 1 if val in nums else 1
    count = 0
    # num is unique number
    if r == 1:
        for num in nums:
            if nums[num] >= 3:
                # 1, 1, 1 -> 1
                # 1, 1, 1, 1 -> 012, 013, 023, 123 = 4 = 4! / (4-1)! / 3! = 4
                # 1, 1, 1, 1, 1 -> 012, 013, 014, 023, 024, 034, 123, 124, 134, 234 = 10 = 5! / (5-3)! / 3! = 5 * 4 / 2 = 2
                count += int(factorial(nums[num]) / factorial(nums[num] - 3))
    else:
        for num in nums:
            if num * r in nums and num * r * r in nums:
                count += nums[num] * nums[num * r] * nums[num * r * r]
    return count


def countTriplets_unsorted(arr, r):
    """
    store a list of indexes for each number
    {
        4: [0, 3],
        2: [1, 4],
        1: [2, 5]
    }
    iterate from the lower number. Find n * r then check if the index is greater
        - nested loop
        if exists, find n * r * r then check the index again.
        Count number of all indexes greater than n * r -> add to the count

    arr[x], arr[y], arr[z] should be in geometric sequence where x < y < z
    """
    nums = {}
    for num in arr:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1

    sorted_nums = sorted(nums.keys())
    count = 0
    for num in sorted_nums:
        if num * r in nums and num * r * r in nums:
            count += nums[num] * nums[num * r] * nums[num * r * r]
    return count


def countTriplets_answer(arr, r):
    count = 0
    bWant = {}
    cWant = {}

    for key in arr:
        if key in cWant:
            # key is a cValue
            c = key

            # Increase count 'n' times
            count += cWant[c]

        if key in bWant:
            # key is a 'b' value, therefore we expect a c value
            b = key
            c = key * r

            if c in cWant:
                cWant[c] += bWant[b]
            else:
                cWant[c] = bWant[b]

        # (ignore this extra block)
        # key is an 'a' value, therefore we expect a b value
        a = key
        b = key * r

        if b in bWant:
            bWant[b] += 1
        else:
            bWant[b] = 1

    return count


def countTriplets_rework(numbers, r):
    # Number of combinations that makes the complete geometric sequence in fhe form of a - b - c
    count = 0
    
    # Number of A's that needs B to complete the sequence. B: count(A)
    # counting number of a's for each b eg. given [1, 1, 1, 2], { 2: 3 }
    # -> target 2 has 3 previous numbers that becomes 2 when multiplied by r.
    b_needed_by_as = {}
    # Number of B's that needs C to complete the sequence. C: count(B)
    c_needed_by_bs = {}

    for curr_num in numbers:
        # Current num makes c for some previous numbers
        # Sequence is made. Add to count the combination of a's and b's every time curr_num is found from dict.
        # eg. [1, 1, 2, 2, 2, 4, 4] -> every 4 has 2 * 3 combinations
        if curr_num in c_needed_by_bs:
            combinations_with_curr_num_in_c = c_needed_by_bs[curr_num]
            count += combinations_with_curr_num_in_c

        # curr_num can be found in both c and b bucket eg. 4 in [1, 2, 4, 8]

        # current num makes b for some previous numbers
        # if curr_num is found in b bucket, increment the value of the key, c, by available combinations
        # or initialize key value with the combinations
        if curr_num in b_needed_by_as:
            # Calculate c for curr num as b then register to the c bucket
            c_needed_by_b = curr_num * r
            combinations_with_curr_num_in_b = b_needed_by_as[curr_num]

            # 
            if c_needed_by_b in c_needed_by_bs:
                c_needed_by_bs[c_needed_by_b] += combinations_with_curr_num_in_b
            else:
                c_needed_by_bs[c_needed_by_b] = b_needed_by_as[curr_num]

        # create target with current number as a, and add to the b bucket
        b_needed_by_a = curr_num * r
        # handles the case where curr_num is repeated eg. [1, 1, 2, 4]
        if b_needed_by_a in b_needed_by_as:
            b_needed_by_as[b_needed_by_a] += 1
        else:
            b_needed_by_as[b_needed_by_a] = 1

    return count


"""
[1, 2, 2, 4]
seconds = {}
thirds = {}

curr_num = 1
second = 1 * r = 2
second is not in seconds: seconds = {2: 1}
curr_num is not in seconds
curr_num is not in thirds

curr_num = 2, second = 2 * 2 = 4
second is not in seconds: seconds = {2: 1, 4: 1}
curr_num is in seconds:
    second is not in thirds: thirds = {4: 1}
curr_num is not in thirds

curr_num = 2, second = 4
second is in seconds: seconds = {2: 1, 4: 2}
curr_num is in seconds:
    second is in thirds:



"""

count_triplets = countTriplets_rework
