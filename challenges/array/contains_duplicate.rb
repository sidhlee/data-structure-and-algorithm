def contains_duplicate_uniq(nums)
  # Time: 62% O(n) because of uniq
  # Space: 90% O(n) because of uniq
  nums.uniq.length != nums.length
end

def contains_duplicate_without_uniq(nums)
  # Time: 22% O(nlogn) because of sort
  # Space: 99% O(n) we can conservatively estimate sort to be O(n) for recursion or temp storage
  # but since we are sorting integers with limited array size, we can say O(1)
  nums.sort!
  (1...nums.length).each do |i|
    return true if nums[i] == nums[i - 1]
  end
  false
end

def contains_duplicate_without_sort(nums)
  # Time: 72% O(n) but stops early if duplicate is found
  # Space: 66% O(n)
  hash = {}
  nums.each do |num|
    return true if hash[num]
    hash[num] = true
  end
  false
end
