from collections import Counter
from math import factorial


def sherlockAndAnagrams_wrong_math(s):
    # brute forcing
    pairs = 0
    for length in range(1, len(s)):
        c = Counter()
        for i in range(len(s) + 1 - length):
            sub = s[i : i + length]
            sub = "".join(sorted(sub))
            c[sub] += 1
        num_pairs = [int(factorial(count) / 2) for count in c.values() if count > 1]

        pairs += sum(num_pairs)
        print(c, num_pairs, pairs)
    return pairs


def sherlockAndAnagrams_correct_math(s):
    """
    2023-03-14 08:57:45
    O(n^2) but works due to upper bound in input: len(s) <= 100
    """
    # brute forcing
    pairs = 0
    for length in range(1, len(s)):
        # this could be a plain dict
        c = Counter()
        for i in range(len(s) + 1 - length):
            sub = s[i : i + length]
            sub = "".join(sorted(sub))
            c[sub] += 1
        # n! * (n-1)! / 2
        num_pairs = [int(count * (count - 1) / 2) for count in c.values() if count > 1]
        pairs += sum(num_pairs)
    return pairs


sherlock_and_anagrams = sherlockAndAnagrams_correct_math
