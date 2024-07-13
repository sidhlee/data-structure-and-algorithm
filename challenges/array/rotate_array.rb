# @param {Integer[]} arr
# @param {Integer} n
# @return {Void} Do not return anything, modify arr in-place instead.
def rotate_array(arr, n)
  n = n % arr.length
  arr.rotate!(-n)
end

def rotate_array(arr, n)
  n = n % arr.length
  arr.replace(arr[-n..-1] + arr[0...-n])
end
