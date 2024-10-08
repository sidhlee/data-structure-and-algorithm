def single_number_xor(nums)
  # Time: 24% O(n)
  # Space: 90% O(1)
  res = nums[0]
  (1...nums.length).each do |i|
    res ^= nums[i]
  end
  res
end

def single_number_xor_reduce(nums)
  nums.reduce(:^)
end
