# ["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]

# ["8", "3", ".", "6", ".", ".", ".", "9", "8"],
# [".", "7", ".", "1", "9", "5", ".", ".", "."],
# [".", ".", ".", ".", ".", ".", ".", "6", "."],
# ["8", ".", ".", "4", ".", ".", "7", ".", "."],
# [".", "6", ".", "8", ".", "3", ".", "2", "."],
# [".", ".", "3", ".", ".", "1", ".", ".", "6"],
# [".", "6", ".", ".", ".", ".", ".", ".", "."],
# [".", ".", ".", "4", "1", "9", ".", "8", "."],
# ["2", "8", ".", ".", ".", "5", ".", "7", "9"]

def valid?(cells)
  digits = cells.select { |item| item =~ /\d/ }
  digits.uniq.length == digits.length
end

def subgrids(board)
  cells = []
  (0...3).each do |i|
    (0...3).each do |j|
      cell = []
      cell += board[i * 3][j * 3...(j + 1) * 3]
      cell += board[i * 3 + 1][j * 3...(j + 1) * 3]
      cell += board[i * 3 + 2][j * 3...(j + 1) * 3]
      cells << cell
    end
  end
  cells
end

# @param {Character[][]} board
# @return {Boolean}
def is_valid_sudoku_first_attempt(board)
  board.each do |row|
    return false unless valid?(row)
  end

  board.transpose.each do |col|
    return false unless valid?(col)
  end

  subgrids(board).each do |subgrid|
    return false unless valid?(subgrid)
  end

  true
end

def is_valid_sudoku_array_of_sets(board)
  # Time: 99% O(1) Set!
  # Space: 26% O(1) for setting up the sets

  # Initialize sets to track seen numbers in rows, columns, and subgrids
  # Sets -> checking for duplicates is O(1)
  rows = Array.new(9) { Set.new }
  cols = Array.new(9) { Set.new }
  subgrids = Array.new(9) { Set.new }

  (0...9).each do |i|
    (0...9).each do |j|
      num = board[i][j]
      next if num == "."

      # In ruby, division of integers drops the remainder
      # (i / 3) * 3: [0, 0], [1, 0], [2, 0], [3, 3], [4, 3], [5, 3], [6, 6], ...
      # (j / 3): [0, 0], [1, 0], [2, 0], [3, 1], [4, 1], [5, 1], [6, 2], ...
      # (i / 3) * 3 returns the starting row index of the subgrid
      # (j / 3) returns the starting column index of the subgrid
      # (i / 3) * 3 + (j / 3) returns:
      # when i = 0 and as j increases: 0, 0, 0, 1, 1, 1, 2, 2, 2
      # when i = 1 and as j increases: 0, 0, 0, 1, 1, 1, 2, 2, 2
      # when i = 2 and as j increases: 0, 0, 0, 1, 1, 1, 2, 2, 2
      # when i = 3 and as j increases: 3, 3, 3, 4, 4, 4, 5, 5, 5
      # when i = 4 and as j increases: 3, 3, 3, 4, 4, 4, 5, 5, 5
      # when i = 5 and as j increases: 3, 3, 3, 4, 4, 4, 5, 5, 5
      # when i = 6 and as j increases: 6, 6, 6, 7, 7, 7, 8, 8, 8
      # when i = 7 and as j increases: 6, 6, 6, 7, 7, 7, 8, 8, 8
      # when i = 8 and as j increases: 6, 6, 6, 7, 7, 7, 8, 8, 8

      subgrid_index = (i / 3) * 3 + (j / 3)

      # Check for duplicates in rows, columns, and subgrids
      if rows[i].include?(num) ||
         cols[j].include?(num) ||
         subgrids[subgrid_index].include?(num)
        return false
      end

      # Add the number to the sets
      rows[i].add(num)
      cols[j].add(num)
      subgrids[subgrid_index].add(num)
    end
  end

  true
end
