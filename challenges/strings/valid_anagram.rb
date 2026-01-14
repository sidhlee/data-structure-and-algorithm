def is_anagram_first_attempt_with_counter(s, t)
  # Runtime: 83 ms
  # Memory Usage: 218.3 MB

  # Ruby compares Hash by its contents. (key order doesn't matter)
  # reduce is effectively same as .tally
  s_counter = s.split("").sort.reduce(Hash.new(0)) { |a, c| a[c] += 1; a }
  t_counter = t.split("").sort.reduce(Hash.new(0)) { |a, c| a[c] += 1; a }
  s_counter == t_counter
end

def is_anagram_use_tally(s, t)
  # tally is a Hash counter similar to collections.Counter in Python
  # Ruby compares Hash by its contents. (key order doesn't matter)
  # chars is faster than split('') because split uses regex
  s.chars.tally == t.chars.tally
end
