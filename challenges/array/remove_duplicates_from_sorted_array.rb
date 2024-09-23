def remove_duplicates_v2(nums)
  k = 0
  (1...nums.length).each do |i|
      if nums[i] > nums[k]
          k += 1
          nums[k] = nums[i]
      end
  end
  return k + 1
end

def remove_duplicates_unique(nums)
  # Don't need to check for empty array because of 1 <= nums.length constraint
  nums.uniq!
  nums.length

def remove_duplicates_manual_using_constraint(nums)
  k = 1 # at least one element in array that is automatically unique
  (1...nums.length).each do |i|
    nums[k] = nums[i]
    k += 1
  k
end
