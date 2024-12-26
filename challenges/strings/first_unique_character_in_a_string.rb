# @param {String} s
# @return {Integer}
def first_uniq_char_first_attempt(s)
  chars_indexes = {}
  # O(n)
  (0...s.chars.count).each do |i|
    chars_indexes[s[i]] ||= []
    chars_indexes[s[i]] << i
  end
  # O(26) = O(1)
  chars_indexes.each_value do |indexes|
    if indexes.count == 1
      return indexes[0]
    end
  end
  return -1
end

def first_uniq_char_best_time(s)
  # Not sure why this is faster with many O(n) operations
  # but using a limited character set for O(1) is a good strategy
  first_unique = Float::INFINITY

  ("a".."z").each do |c|
    if s.include?(c)
      if s.index(c) == s.rindex(c)
        first_unique = [first_unique, s.index(c)].min
      end
    end
  end

  first_unique == Float::INFINITY ? -1 : first_unique
end

def first_good_char_tally(s)
  # O(n) + O(26) + O(n) = O(n)
  s.chars.tally.each do |k, v|
    return s.index(k) if v == 1
  end
  -1
end
