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

def is_valid_sudoku_return_early(board)
    # 2026-02-21 10:37:45
    # tries to return false as soon as it finds a duplicate, instead of waiting to check the whole board
    # but this might be overkill since the board is always 9x9, so the time complexity is O(1) regardless of how we check for duplicates

    # 1. validate row
    board.each do |row|
        cleaned_up = row.filter { |val| val != '.' }
        return false if cleaned_up.count != cleaned_up.uniq.count
    end

    # 2. validate col
    (0...9).each do |i|
        col = Set.new
        (0...9).each do |j|
            return false if col.include?(board[j][i])
            col.add(board[j][i]) unless board[j][i] == '.'
        end
    end

    # 3. validate subgrid
    (0...3).each do |i|
        (0...3).each do |j|
            grid = board[i*3][j*3...(j+1)*3] +
                    board[i*3 + 1][j*3...(j+1)*3] +
                    board[i*3 + 2][j*3...(j+1)*3]
            cleaned_up = grid.filter { |val| val != '.' }
            return false if cleaned_up.count != cleaned_up.uniq.count
        end
    end

    true
end

def is_valid_sudoku_return_early_ai_improved(board)
    # 2026-02-21 10:37:45
    # Validates sudoku board by checking rows, columns, and 3x3 subgrids
    # Returns false as soon as a duplicate is found
    # Time: O(1) - always checks fixed 9x9 board
    # Space: O(1) - uses only a single Set

    # 1. validate row
    board.each do |row|
        seen = Set.new
        row.each do |val|
            next if val == '.'
            return false if seen.include?(val)
            seen.add(val)
        end
    end

    # 2. validate col
    (0...9).each do |i|
        seen = Set.new
        (0...9).each do |j|
            val = board[j][i]
            next if val == '.'
            return false if seen.include?(val)
            seen.add(val)
        end
    end

    # 3. validate subgrid
    (0...3).each do |i|
        (0...3).each do |j|
            seen = Set.new
            (0...3).each do |di|
                (0...3).each do |dj|
                    val = board[i * 3 + di][j * 3 + dj]
                    next if val == '.'
                    return false if seen.include?(val)
                    seen.add(val)
                end
            end
        end
    end

    true
end
