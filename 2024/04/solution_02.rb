# GOAL: Find number of times MAS appears in a cross

# Test input contains 9 occurences

xmas_count=0

lines=[]

# Store input as an array of arrays
# File.foreach("input_test.txt") do
File.foreach("input.txt") do
  |line|
  line_vals=line.chomp.chars   # create an array of the characters in the line (minus the newline)
  line_length=line_vals.length
  lines.append(line_vals)
end

num_lines=lines.length
num_chars=lines[0].length

# For each line in the grid, check each letter to see if it's an "A"
for line, line_num in lines.map.with_index
  if line_num>0 and line_num < num_lines-1 # don't need to check the first or last line
    for char, char_postn in line.map.with_index
      if char=='A'
        # We found an "A" in position (x,y)
        # puts "Found A in position ("+char_postn.to_s+","+line_num.to_s+")"
        # If the A has space for a character to the left and to the right,
        # check for "M" and "S" in each of the 4 diagonals around (x,y).

        if char_postn > 0 and char_postn < (num_chars - 1)
          al=lines[line_num-1][char_postn-1]           # character found ABOVE LEFT
          ar=lines[line_num-1][char_postn+1]           # character found ABOVE RIGHT
          bl=lines[line_num+1][char_postn-1]           # character found BELOW LEFT
          br=lines[line_num+1][char_postn+1]           # character found BELOW RIGHT
          # puts al+" "+ar
          # puts " A "
          # puts bl+" "+br
          # puts
          ms=["M","S"]
          if  (ms.include? al) and (ms.include? ar) and (ms.include? bl) and (ms.include? br) # only the letters "M" and "S" have been found
            if (al == ar and bl == br and al != bl) or (al == bl and ar == br and al != ar)   # found 2 pairs of letters: top and bottom or right and left
              # puts "FOUND X-MAS"
              xmas_count+=1
            end
          end


        end
      end
    end
  end
end

puts xmas_count