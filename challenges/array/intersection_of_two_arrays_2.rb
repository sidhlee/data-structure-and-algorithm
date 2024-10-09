def intersect_manual_with_hash_first_attempt(nums1, nums2)
  # Time: 68% O(n) with upper bound of 1000
  # Space: 76% O(n) with upper bound of 1000
  output = []
  hash = {}
  nums1.each do |num|
    if hash[num]
      hash[num] += 1
    else
      hash[num] = 1
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
  hash = nums1.reduce({}) do |acc, num|
    acc[num] = acc[num].to_i + 1
    acc
  end

  nums2.reduce([]) do |acc, num|
    hash[num].to_i > 0 ? (acc << num; hash[num] -= 1) : acc
  end
end

def intersect_with_default_hash_value(nums1, nums2)
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
