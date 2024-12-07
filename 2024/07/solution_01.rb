# GOAL: Determine which equations could be true and calculate their total calibration result

# Each line represents a single equation. 
# The test value appears before the colon on each line; 
# Determine whether the remaining numbers can be combined with + and * operators to produce the test value.

# Operators are always evaluated left-to-right. 
# Numbers in the equations cannot be rearranged. 

# Test input (sum of the three equations that could be true is 3749):

# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20

calibration_result=0

File.foreach("input.txt") do
  |line|
  test_val=line.split(":")[0].to_i          # find the value to the left of the colon
  numbers=line.chomp.split(":")[1].split    # generate an array of the values to the right of the colon
  # puts
  # puts "Trying to make:"+line.split(":")[0]
  # puts
  could_be_true=false  # start by assuming the equation could not be true
  possible_results=[]  # we will keep track of the different possible results as we add or multiply by the next number in the series
  for num, idx in numbers.map.with_index
    # puts "Number "+idx.to_s+": "+num
    if idx==0
      # puts"(first number)"
      possible_results.append(num.to_i)  
    else
      new_possible_results=[]
      for possible_result in possible_results
        new_possible_results.append(possible_result+num.to_i)    # append the result of adding the next number
        new_possible_results.append(possible_result*num.to_i)    # append the result of multiplying by the next number
      end
      possible_results=new_possible_results   # replace the old running_totals with the one we just created
    end
  end
  for result in possible_results
    # puts "Checking against possible result: "+result.to_s
    if result == test_val   
      could_be_true=true
    end
  end
  if could_be_true
    calibration_result+=test_val
  end
end

puts calibration_result