# GOAL: 

# rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

# In particular, here is what the third example history looks like when extrapolating back in time:

# 5  10  13  16  21  30  45
#   5   3   3   5   9  15
#    -2   0   2   4   6
#       2   2   2   2
#         0   0   0

# Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: 5.

# Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the second history. Adding all three new values together produces 2.

inputfile = "input.txt"
f = open(inputfile, "r")

history=[]

for line in f:
    sequences=[]
    sequence=[]
    numbers=line.split('\n')[0].split(' ')
    for num in numbers:
        sequence.append(int(num))
    sequences.append(sequence)
    history.append(sequences)

def get_new_seq(ind,seq):
    new_seq=[]
    all_zeros=True
    for index, num in enumerate(seq):
        if index < len(seq)-1:
            # print ('number',num,'is in position',index)
            new_val=seq[index+1]-seq[index]
            if new_val!=0:
                all_zeros=False
            new_seq.append(new_val)
    history[ind].append(new_seq)
    return new_seq if all_zeros else get_new_seq(ind,new_seq)

sum_of_next_vals=0

for i,sequences in enumerate(history):
    new_seq=get_new_seq(i,sequences[0])
    val=0
    for x in range (len(sequences)-1,-1,-1):
        val=sequences[x][0]-val
    # print(sequences)
    print('previous value:',val)
    sum_of_next_vals+=val

f.close()

print(sum_of_next_vals)