def plus_one_first_attempt(digits)
  # Time: 19% O(n)
  # Space: 55% O(1) modifying in-place and temp variables
  digits.reverse_each.with_index do |digit, rev_i|
    i = digits.length - 1 - rev_i
    if digit == 9
      digits[i] = 0
    else
      digits[i] += 1
      return digits
    end
  end
  digits.unshift(1)
end

def plus_one_next(digits)
  # 2026-01-24 07:38:19
  (0..digits.length-1).reverse_each do |i|
      if digits[i] == 9
          digits[i] = 0
          # if next digit is less than 9, we increment and return
          # if next digit is 9, we continue setting it to 0 until we find a digit less than 9
          next
      end
      # All previous digits have been set to 0.
      digits[i] += 1
      return digits
  end
  [1] + digits
end

def plus_one_downto_return_earlier(digits)
  # Time: 19% O(n)
  # Space: 97% O(1)
  (digits.length - 1).downto(0) do |i|
    if digits[i] < 9
      digits[i] += 1
      return digits
    else
      digits[i] = 0
    end
    digits.unshift(1)
  end
end

def plus_one_convert_to_string(digits)
  # Time: 96%
  # Space: 52%
  (digits.join('').to_i + 1).to_s.split('').map(&:to_i)
end
