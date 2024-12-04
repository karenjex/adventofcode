# instructions are mul(X,Y), where X and Y are each 1-3 digit numbers. 
# mul(44,46) = 44 x 46 = 2024

# There may be invalid characters that should be ignored
# mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing

# GOAL: Find the sum of the result of all the uncorrupted mul instructions.

# Test input:
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

# Result for test input:
# mul(2,4) + mul(5,5) + mul(11,8) + mul(8,5) = 2*4 + 5*5 + 11*8 + 8*5 = 161

result=0

instructions=File.open("input.txt").read

# use regex to find all uncorrupted mul(x,y) instrcutions, i.e. occurences of mul\(\d{1,3},\d{1,3}\)
uncorrupted=instructions.scan(/mul\(\d{1,3},\d{1,3}\)/)

for i in uncorrupted
  input_vals=i.scan(/\d{1,3}/)
  result+=input_vals[0].to_i*input_vals[1].to_i
end

puts result