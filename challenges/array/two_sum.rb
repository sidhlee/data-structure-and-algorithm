def two_sum_first_attempt(nums, target)
  # Time: 96% O(n)
  # Space: 26% O(n)
  complements_to_index = {}
  nums.each_with_index do |num, i|
    complement = target - num
    index = complements_to_index[num]
    if index
      return [index, i]
    else
      complements_to_index[complement] = i
    end
  end
end

def two_sum_using_key(nums, target)
  complements_to_index = {}

  nums.each_with_index do |num, i|
    complement = target - num

    if complements_to_index.key?(num)
      return [complements_to_index[num], i]
    end

    complements_to_index[complement] = i
  end

  # If no solution is found, return nil or raise an error
  nil
end
