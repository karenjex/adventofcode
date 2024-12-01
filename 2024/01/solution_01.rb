# Test input:
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3

# Pair up the smallest number in the left list with the smallest number in the right list, 
# then the second-smallest left number with the second-smallest right number, and so on.

# Within each pair, figure out how far apart the two numbers are; 
# Add up all of those distances. 

# In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

total_dist=0

left_list=[]
right_list=[]

# left_list=[3,4,2,1,3,3]
# right_list=[4,3,5,3,9,3]

File.foreach("input.txt") do
    |line|
    left_list.append(line.split[0].to_i)  # get first (left) item in line, convert to integer, append to left_list
    right_list.append(line.split[1].to_i) # get second (right) item in line, convert to integer, append to right_list
end

# sort the lists
left_list_sorted=left_list.sort
right_list_sorted=right_list.sort

for i in 0..left_list.length-1      # loop through lists, getting distance between each pair
  left_val=left_list_sorted[i]
  right_val=right_list_sorted[i]
  dist = (left_val-right_val).abs
  total_dist+=dist
end

puts total_dist