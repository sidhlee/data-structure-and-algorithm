def intersect_manual_with_hash_first_attempt(nums1, nums2)
  # Time: O(n + m) where n = nums1.length, m = nums2.length
  # Space: O(n) extra space for the hash (plus O(k) for output), where n = nums1.length
  output = []
  hash = {}
  nums1.each do |num|
    if hash[num]
      hash[num] += 1
    else
      hash[num] = 1
    end
  end
  nums2.each do |num|
    if hash[num] and hash[num] > 0
      output << num
      hash[num] -= 1
    end
  end
  return output
end


def intersect_manual_with_hash(nums1, nums2)
  # Time: O(n + m) where n = nums1.length, m = nums2.length
  # Space: O(n) extra space for the hash (plus O(k) for output)
  hash = {}
  nums1.each do |num|
    # to_i converts nil to 0. Use for incrementing counter.
    hash[num] = hash[num].to_i + 1
  end

  result = []
  nums2.each do |num|
    # Use to_i when you don't know if the counter key exists.
    if hash[num].to_i > 0
      result << num
      hash[num] -= 1
    end
  end
  result
end

def intersect_manual_with_hash_reduce(nums1, nums2)
  # Time: O(n + m) where n = nums1.length, m = nums2.length
  # Space: O(n) extra space for the hash (plus O(k) for output)
  hash = nums1.reduce({}) do |acc, num|
    acc[num] = acc[num].to_i + 1
    acc
  end

  nums2.reduce([]) do |acc, num|
    if hash[num].to_i > 0
      acc << num
      hash[num] -= 1
    end
    acc
  end
end

def intersect_manual_with_hash_reduce_short(nums1, nums2)
  # Time: O(n + m) where n = nums1.length, m = nums2.length
  # Space: O(n) extra space for the hash (plus O(k) for output)
  hash = nums1.reduce({}) do |acc, num|
    acc[num] = acc[num].to_i + 1
    acc
  end

  nums2.reduce([]) do |acc, num|
    hash[num].to_i > 0 ? (acc << num; hash[num] -= 1) : acc
  end
end

def intersect_with_default_hash_value(nums1, nums2)
  # Time: O(n + m) where n = nums1.length, m = nums2.length
  # Space: O(n) extra space for the hash (plus O(k) for output)
  # Reduces to_i calls
  hash = Hash.new(0)

  # Build the hash with counts from nums1
  nums1.each { |num| hash[num] += 1 }

  # Find the intersection
  nums2.each_with_object([]) do |num, result|
    if hash[num] > 0
      result << num
      hash[num] -= 1
    end
  end
end

def intersect_without_hash_first_attempt(nums1, nums2)
  # Time: O(n log n + m log m) due to sorting (n = nums1.length, m = nums2.length)
  # Space: O(1) extra (ignoring output); output uses O(k)
  nums1.sort!
  nums2.sort!
  res = []
  i = 0
  # This will keep looping when nums1 have 10k elements but nums2 have only 1 element
  nums1.each do |num|
      (i...nums2.length).each do |j|
          if num == nums2[j]
              res << num
              i = j + 1
              break
          end
          break if num < nums2[j]
      end
  end
  res
end

def intersect_without_hash_two_pointers(nums1, nums2)
  # Time: O(n log n + m log m) due to sorting (n = nums1.length, m = nums2.length)
  # Space: O(1) extra (ignoring output); output uses O(k)
  # More efficient because it stops looping once pointer reaches the end of either array
  nums1.sort!
  nums2.sort!

  i = 0
  j = 0
  result = []

  while i < nums1.length && j < nums2.length
    if nums1[i] < nums2[j]
      i += 1
    elsif nums1[i] > nums2[j]
      j += 1
    else
      result << nums1[i]
      i += 1
      j += 1
    end
  end

  result
end
