def hourglassSum_brute_force(arr):
    """
    2023-02-16 06:56:03
    array range is limited so we can run in O(n).
    - can be further optimized by subtracting prev columns/rows and
      adding new columns/rows instead of summing again.
    - but also there are only max 3 numbers in sum function,
      so the pref gain is small.
    """
    mx = -81
    for i in range(4):
        s1 = sum(arr[i][0:3]) + arr[i + 1][1] + sum(arr[i + 2][0:3])
        s2 = sum(arr[i][1:4]) + arr[i + 1][2] + sum(arr[i + 2][1:4])
        s3 = sum(arr[i][2:5]) + arr[i + 1][3] + sum(arr[i + 2][2:5])
        s4 = sum(arr[i][3:6]) + arr[i + 1][4] + sum(arr[i + 2][3:6])
        mx = max(mx, max(s1, s2, s3, s4))
    return mx


hourglass_sum = hourglassSum_brute_force
