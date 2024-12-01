# Test input:
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3

# Find the similarity score for the two lists.

# Figure out exactly how often each number from the left list appears in the right list. 
# Calculate a total similarity score by adding up each number in the left list 
# after multiplying it by the number of times that number appears in the right list.

# For the example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

total_similarity=0

left_list=[]
right_list=[]

# left_list=[3,4,2,1,3,3]
# right_list=[4,3,5,3,9,3]

File.foreach("input.txt") do
    |line|
    left_list.append(line.split[0].to_i)    # get first (left) item in line, convert to integer, append to left_list
    right_list.append(line.split[1].to_i)    # get second (right) item in line, convert to integer, append to right_list
end

for i in 0..left_list.length-1       # loop through left_list
  left_val=left_list[i]
  right_count=right_list.count(left_val) # would probably be better to go through right_list once to get the counts rather than check for each val in left_list
  similarity= left_val*right_count
  total_similarity+=similarity
end

puts total_similarity