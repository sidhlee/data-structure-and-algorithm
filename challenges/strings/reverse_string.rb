def reverse_string_first_attempt(s)
  # Time: O(n) 33.7%
  # Space: O(1) 95%
  (0...s.length / 2).each do |i|
    s[i], s[s.length - 1 - i] = s[s.length - 1 - i], s[i]
  end
end

def reverse_string_while(s)
  left = 0
  right = s.length - 1

  while left < right
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
  end
end
