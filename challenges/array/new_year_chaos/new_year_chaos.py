def minimumBribes(q):
    q = [x - 1 for x in q]  # map number to the index position
    count = 0
    for i, n in enumerate(q):
        if n > i + 2:  # bribed more than 2 times.
            print("Too chaotic")
            return
        is_last = i == len(q) - 1
        bribed_once_and_paid_once = n == i and (not is_last and q[i + 1] < n)
        bribed_many_and_paid_once = n < i and (not is_last and q[i + 1] < n)
        paid_and_not_bribed = n < i and (is_last or q[i + 1] > n)
        if bribed_once_and_paid_once:
            count += 1
        elif bribed_many_and_paid_once:
            count += (i - n) + 1
        elif paid_and_not_bribed:
            count += i - n

    print(count)


"""
[3, 2, 1, 4]
0 3: (3-1) - 0 = 2 -> 2 bribes
1 2: (2-1) - 1 = 0, but still bribed 1. if latest_bribed > curr then 
     original_index = (n - 1) - i + bribes
     -> we cannot use this because we don't know how many of the bribes
     are paid by the ones that were already ahead of the current.
     
[3, 2, 1, 4]
3: 0
2: 0
1: 2

[1, 2, 3, 4]
[3, 1, 2, 4]
[3, 2, 1, 4]

[2, 1, 5, 3, 4]
- 3 was initially at index 2 but now at index 3
- 5 bribed 3 but 2 was already ahead of 3. So 3 is pushed back only once.

[4, 2, 1, 3]
[2, 4, 1, 3]
[2, 1, 4, 3] -> Too chaotic



[2, 1, 5, 3, 4]
[1, 2, 5, 3, 4]
[1, 2, 3, 5, 4]
[1, 2, 3, 4, 5]



[1, 2, 5, 3, 4, 7, 8, 6, 4]

[3, 2, 1]
[1, 4, 3, 2] -> why do we need to look at i - 1 when 3's in the correct position?
[1, 2, 3, 4, 5]
[1, 3, 4, 5, 2]
[1, 5, 3, 4, 2]
[1, 5, 2, 3, 4]





[3, 4, 1, 2]
[4, 3, 1, 2]
[4, 1, 3, 2] -> Too chaotic (3 is not after 2)

[3, 1, 4, 2]
[3, 1, 2, 4]
[1, 3, 2, 4]
[1, 2, 3, 4] going bottom up, 3 swaps 2 times and 4 swaps once.

[3, 1, 4, 2]
[1, 3, 4, 2]
[1, 4, 3, 2] -> after 2 swaps, 3 falls into expected position
[1, 3, 4, 2]
[1, 3, 2, 4] -> after 2 swaps, 4 falls into expected position
[1, 2, 3, 4] -> after 1 swaps, 3 falls into " ".



[3, 1, 4, 2]
[3, 1, 2, 4]
[3, 2, 1, 4]
[3, 1, 2, 4]
[1, 3, 2, 4]




[2, 3, 1]
[1, 2, 4, 5, 3]
[1, 2, 5, 4, 3]

"""

new_year_chaos = minimumBribes
