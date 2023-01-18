def FindIntersection_two_pointers(strArr):
    """
    2023-01-17 07:10:58
    O(n) time & space
    - Could save space by not creating list and directly parsing from the string
    """
    nums1 = [int(x) for x in strArr[0].split(", ")]
    nums2 = [int(x) for x in strArr[1].split(", ")]
    res = ""
    p1 = p2 = 0
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            res += str(nums1[p1]) + ","
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1
    return res.rstrip(",") if res else "false"


def FindIntersection_declarative(strArr):
    """
    2023-01-18 07:24:57
    O(nLog(n)) time and space

    If we don't want to use two pointers,
    Using set (linear) is faster than list comprehension (quadratic)
    """
    # Don't map to int yet. Always wait until necessary
    str_nums_set_1 = set(strArr[0].split(", "))
    str_nums_set_2 = set(strArr[1].split(", "))
    str_intersection = str_nums_set_1 & str_nums_set_2
    # return early before list conversion and sorting
    if not str_intersection:
        return "false"
    str_intersection_list = list(str_intersection)
    # sorting takes O(Log(n)), and we're doing it inline to save space
    # also only using int mapping for sorting so we don't need to convert back
    str_intersection_list.sort(key=lambda x: int(x))
    # join only inserts delimiter in-between elements
    return ",".join(str_intersection_list)
