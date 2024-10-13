def move_zeroes_first_attempt(nums)
  # Time: 53% O(n)
  # Space: 88% O(1)
  insert_at = 0
  nums.each do |num|
    if num != 0
      nums[insert_at] = num
      insert_at += 1
    end
  end
  (nums.length - insert_at).times do |i|
    nums[insert_at + 1] = 0
  end
  nums
end

def move_zeros_use_ranged_each(nums)
  insert_at = 0
  nums.each do |num|
    if num != 0
      nums[insert_at] = num
      insert_at += 1
    end
  end
  (insert_at...nums.length).each { |i| nums[i] = 0 }
  nums
end
