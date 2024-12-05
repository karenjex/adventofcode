# GOAL: Find number of times XMAS appears in the wordsearch

# Words can be horizontal, vertical, diagonal, written backwards, or even overlapping other words.

# Test input (contains 18 occurences of XMAS):

# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX

xmas_count=0

lines=[]

# Store input as an array of arrays
File.foreach("input.txt") do
  |line|
  line_vals=line.chomp.chars   # create an array of the characters in the line (minus the newline)
  line_length=line_vals.length
  lines.append(line_vals)
end

num_lines=lines.length
num_chars=lines[0].length

puts "number of lines: "+num_lines.to_s
puts "number of chars per line: "+num_chars.to_s
puts

# The X has to be in position...
# x < num_chars - 3 (i.e. 4 in the grid below) to go to the right
# x > 2             to go to the left
# y < num_lines - 3 (i.e. 3 in the grid below) to go down
# y > 2             to go up

#   0 1 2 3 4 5 6
# 0       X M A S
# 1 S A M X     A
# 2 X           M
# 3 M           X
# 4 A
# 5 S

# For each line in the grid, check each letter to see if it's an "X"
for line, line_num in lines.map.with_index
  for char, char_postn in line.map.with_index
    if char=='X'
      # We found an "X" in position (x,y)
      # Check each of the 8 directions around (x,y) for the letters "M" "A" and "S" in sequence
      # Only check if there's enough space in the given direction for the whole word
      puts "Found X in position ("+char_postn.to_s+","+line_num.to_s+")"
      puts  

      # 1. ABOVE
      puts "Checking ABOVE"
      if line_num > 2
        if lines[line_num-1][char_postn] == "M" and lines[line_num-2][char_postn] == "A" and lines[line_num-3][char_postn] == "S"
          puts "FOUND "+lines[line_num][char_postn]+lines[line_num-1][char_postn]+lines[line_num-2][char_postn]+lines[line_num-3][char_postn]
          puts
          xmas_count+=1
        end
      end       

      # 2. ABOVE & RIGHT
      puts "Checking ABOVE RIGHT"
      if (line_num > 2 and char_postn < (num_chars - 3))
        if lines[line_num-1][char_postn+1] == "M" and lines[line_num-2][char_postn+2] == "A" and lines[line_num-3][char_postn+3] == "S"
          puts "FOUND "+lines[line_num][char_postn]+lines[line_num-1][char_postn+1]+lines[line_num-2][char_postn+2]+lines[line_num-3][char_postn+3]
          puts
          xmas_count+=1
        end
      end         

      # 3. RIGHT
      puts "Checking RIGHT"
      if char_postn < (num_chars - 3)
        if lines[line_num][char_postn+1] == "M" and lines[line_num][char_postn+2] == "A" and lines[line_num][char_postn+3] == "S"
          puts "FOUND "+lines[line_num][char_postn]+lines[line_num][char_postn+1]+lines[line_num][char_postn+2]+lines[line_num][char_postn+3]
          puts
          xmas_count+=1
        end
      end       

      # 4. BELOW & RIGHT
      puts "Checking BELOW RIGHT"
      if line_num < (num_lines - 3) and char_postn < (num_chars - 3)
        if lines[line_num+1][char_postn+1] == "M" and lines[line_num+2][char_postn+2] == "A" and lines[line_num+3][char_postn+3] == "S"
          puts "FOUND "+lines[line_num][char_postn]+lines[line_num+1][char_postn+1]+lines[line_num+2][char_postn+2]+lines[line_num+3][char_postn+3]
          puts
          xmas_count+=1
        end
      end       

      # 5. BELOW
      puts "Checking BELOW"
      if line_num < (num_lines - 3)
        if lines[line_num+1][char_postn] == "M" and lines[line_num+2][char_postn] == "A" and lines[line_num+3][char_postn] == "S"
          puts "FOUND "+lines[line_num][char_postn]+lines[line_num+1][char_postn]+lines[line_num+2][char_postn]+lines[line_num+3][char_postn]
          puts
          xmas_count+=1
        end
      end       

      # 6. BELOW & LEFT
      puts "Checking BELOW LEFT"
      if line_num < (num_lines - 3) and char_postn > 2
        if lines[line_num+1][char_postn-1] == "M" and lines[line_num+2][char_postn-2] == "A" and lines[line_num+3][char_postn-3] == "S"
          puts "FOUND "+lines[line_num][char_postn]+lines[line_num+1][char_postn-1]+lines[line_num+2][char_postn-2]+lines[line_num+3][char_postn-3]
          puts
          xmas_count+=1
        end
      end       

      # 7. LEFT
      puts "Checking LEFT"
      if char_postn > 2
        if lines[line_num][char_postn-1] == "M" and lines[line_num][char_postn-2] == "A" and lines[line_num][char_postn-3] == "S"
          puts "FOUND "+lines[line_num][char_postn]+lines[line_num][char_postn-1]+lines[line_num][char_postn-2]+lines[line_num][char_postn-3]
          puts
          xmas_count+=1
        end
      end       

      # 8. ABOVE & LEFT
      puts "Checking ABOVE LEFT"
      if char_postn > 2 and line_num > 2
        if lines[line_num-1][char_postn-1] == "M" and lines[line_num-2][char_postn-2] == "A" and lines[line_num-3][char_postn-3] == "S"
          puts "FOUND "+lines[line_num][char_postn]+lines[line_num-1][char_postn-1]+lines[line_num-2][char_postn-2]+lines[line_num-3][char_postn-3]
          puts
          xmas_count+=1
        end
      end       

    end
  end
end

puts xmas_count