def rotate_image_diagonal_swap_and_column_reverse(matrix)
  # Time: O(n^2)
  # Space: O(1)

  n = matrix.length
  (0...n).each do |i|
    (0...n).each do |j|
      next if i >= j
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    end
  end

  matrix.each do |row|
    row.reverse!
  end
  matrix
end

def rotate_image_diagonal_use_each_with_proc(matrix)
  n = matrix.length
  (0...n).each do |i|
    (0...n).each do |j|
      next if i >= j
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    end
  end

  matrix.each(&:reverse!)

  matrix
end
