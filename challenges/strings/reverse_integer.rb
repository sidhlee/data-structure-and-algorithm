def reverse_first_attempt(x)
  # Time: O(n) 58%
  # Space: O(1) 42%
  sign = x > 0 ? 1 : -1
  x = x.abs
  res = 0
  while x > 0
    lsd = x % 10
    return 0 if (res * 10 + lsd) > (2 ** 31 - 1)
    res *= 10
    res += lsd
    x /= 10
  end
  res * sign
end

def reverse_integer_copilot(x)
  # Time: O(n)
  # Space: O(1)
  sign = x < 0 ? -1 : 1
  x = x.abs
  res = 0

  while x > 0
    digit = x % 10
    x /= 10

    # Check for overflow
    if res > (2 ** 31 - 1) / 10 || (res == (2 ** 31 - 1) / 10 && digit > 7)
      return 0
    end

    res = res * 10 + digit
  end

  res * sign
end
