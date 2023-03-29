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
    '''
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
    '''
    num_to_indexes = {}
    for num in arr:
        if num in num_to_indexes:
            num_to_indexes[num] += 1
        else:
            num_to_indexes[num] = 1
    
    sorted_nums = sorted(num_to_indexes.keys())
    for first_triplet in sorted_nums:
        if first_triplet * r in num_to_indexes:
            second_triplet_indexes = [i for i in num_to_indexes[first_triplet * r] if ]
            

count_triplets = countTriplets_first_try
