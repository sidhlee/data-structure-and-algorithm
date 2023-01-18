def FindIntersection_two_pointers(strArr):
    """
    2023-01-17 07:10:58
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
