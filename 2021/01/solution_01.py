# Goal: Find how many measurements are larger than the previous measurement

inputfile = "input.txt"
num_increases=0
prev_line=False

with open(inputfile) as f:
    for line in f:
        if prev_line:
            if int(line) > prev_line:
                num_increases+=1
        prev_line=int(line)

print("Number of measures larger than previous", num_increases)