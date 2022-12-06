# Goal: Count the number of times the sum of measurements in a 3-value sliding window increases from the previous sum. 
#       Stop when there aren't enough measurements left to create a new three-measurement sum.

inputfile = "input.txt"
num_increases=0
prev_line=False
current_buffer=[]
current_sum=0

with open(inputfile) as f:
    for line in f:
        if len(current_buffer)<3:
            current_buffer.append(int(line))
            # print("new_buffer:",current_buffer)
        elif len(current_buffer)==3:
            # remove first entry from current_buffer and add line to the end
            old_val=current_buffer.pop(0)
            new_val=int(line)
            current_buffer.append(new_val)
            if new_val>old_val:             # if the value we're removing is greater than the value we're adding, the sum has increased
                num_increases+=1
            # print("new_buffer:",current_buffer)


print("Number of measures larger than previous", num_increases)