# The code needs a complete overhaul! The function to add the numbers should be recursive

# Goal: Find the sum (in SNAFU) of the list of SNAFU numbers

# SNAFU uses powers of five, and instead of using digits four through zero, the digits are 2, 1, 0, "-" (-1) and "=" (-2)

# inputfile = "input_test.txt"    # expected result: "2=-1=0" (SNAFU for 4890)
inputfile = "input.txt"

# Read input file line by line, starting at r.h.s of each line

numbers=[]
max_len=0       # find length of longest number in the list

with open(inputfile) as f:
    for line in f:
        number=[]
        print(line)
        for char in line.strip():
            if char=="-":
                number.append(-1)
            elif char=="=":
                number.append(-2)
            else:
                number.append(int(char))
        numbers.append(number)
        if len(number)>max_len:
            max_len=len(number)

print("longest number:",max_len)

reversed_snafus=[]
for number in numbers:
    reversed_snafu=[]
    for i in range(len(number)-1,-1,-1):        # work from right to left, adding each col
        reversed_snafu.append(number[i])
    reversed_snafus.append(reversed_snafu)

def add_column(chars):
    total=0
    carryover=0
    for char in chars:
        total+=char
    if total%5 <=2:
        col_sum=total%5
        carryover=int((total-col_sum)/5)
    else :
        col_sum=(total%5)-5
        carryover=int((total-col_sum)/5)
    return(col_sum,carryover)

snafu_sum=[]

carryover=0
for i in range(max_len):
    column=[]
    column.append(carryover)
    for snafu in reversed_snafus:
        if len(snafu)>i:
            column.append(snafu[i])
    col_sum=add_column(column)
    total=col_sum[0]
    carryover=col_sum[1]
    print("sum of column =",total,"ammount to carry over =",carryover)
    snafu_sum.append(total)
if carryover<=2 and carryover!=0:
    snafu_sum.append(carryover)
else:
    to_add=[carryover]
    col_sum=add_column(to_add)
    carryover=col_sum[1]
    snafu_sum.append(col_sum[0])
    if carryover<=2 and carryover!=0:
        snafu_sum.append(carryover)

# print(snafu_sum)

return_snafu=''
for i in range(len(snafu_sum)-1,-1,-1):        # work from right to left, adding each col
    char=snafu_sum[i]
    if char==-1:
        return_snafu=return_snafu+"-"
    elif char==-2:
        return_snafu=return_snafu+"="
    else:
        return_snafu=return_snafu+str(char)

print("SNAFU to enter into console:",return_snafu)
