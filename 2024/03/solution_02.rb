# instructions are mul(X,Y), where X and Y are each 1-3 digit numbers. 
# mul(44,46) = 44 x 46 = 2024

# There may be invalid characters that should be ignored
# mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing

# do() enables future mul instructions
# don't() disables future mul instructions
# Only the most recent do() or don't() instruction applies. mul instructions start out enabled.

# GOAL: Find the sum of the result of all the uncorrupted mul instructions.

# Test input:
# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

# Result for test input:
# mul(2,4) + mul(8,5) = 2*4 + 8*5 = 48

result=0
enabled=true

instructions=File.open("input.txt").read

# split instructions on do() - this indicates the start of each enabled set of instructions
split_instructions=instructions.split(/do\(\)/)
  # for each enabled set of instructions, ignore anything after don't()
  for i in split_instructions
    enabled_instructions=i.split(/don\'t\(\)/)[0]
    # find all uncorrupted mul(x,y) instrcutions, i.e. occurences of mul\(\d{1,3},\d{1,3}\)
    uncorrupted=enabled_instructions.scan(/mul\(\d{1,3},\d{1,3}\)/)
    for i in uncorrupted
      input_vals=i.scan(/\d{1,3}/)
      result+=input_vals[0].to_i*input_vals[1].to_i
    end    
  end

puts result