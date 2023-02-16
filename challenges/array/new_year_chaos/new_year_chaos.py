def minimumBribes_logic_too_complex(q):
    """
    Tried to keep O(n) by breaking down to cases,
    but in general, stay away from many if statements for
    algorithm questions.

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
    count = 0
    for i, v in enumerate(q):
        o_idx = v - 1
        if o_idx > i + 2:  # bribed more than 2 times.
            print("Too chaotic")
            return
        bribed_only = o_idx > i

        # for debugging
        if i > 5:
            visual = q[i - 5 : i + 5]

        is_last = i == len(q) - 1
        paid_and_bribed_once = (o_idx < i and (not is_last and q[i + 1] < v)) or (
            o_idx == i and i > 0 and q[i - 1] > v
        )
        paid_only = o_idx < i and (is_last or (q[i + 1] > o_idx))
        if bribed_only:
            continue
        elif paid_and_bribed_once:
            # you can only bribe 1 person when you got paid
            num_paid = (i - o_idx) + 1
            count += num_paid
        elif paid_only:
            num_paid = i - o_idx
            count += num_paid

    print(count)


def min_bribes_look_behind(q):
    """
    2023-02-11 14:15:42

    original index can still be same as current index
    after getting paid when a person behind you bribes you and
    person ahead of you, then you bribe the person ahead of you
    to get back to the original position.
    """
    bribes = 0
    for i, v in enumerate(q):
        o_idx = v - 1
        if i + 2 < o_idx:
            # more than 2 steps ahead of original position
            print("Too chaotic")
            return
        if i >= o_idx:
            # if at original position or behind,
            # find people who bribed the current person b/w
            # original idx - 1 and current index - 1
            for j in range(max(0, o_idx - 1), i):
                if q[j] > v:
                    bribes += 1
    print(bribes)


new_year_chaos = min_bribes_look_behind
