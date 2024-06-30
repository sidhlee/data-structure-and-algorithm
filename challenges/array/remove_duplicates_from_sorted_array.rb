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
