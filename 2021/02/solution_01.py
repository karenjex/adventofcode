# Goal: 

inputfile = "input.txt"

num_increases=0
prev_line=False
current_buffer=[]
current_sum=0

with open(inputfile) as f:
    for line in f:


print("Number of measures larger than previous", num_increases)