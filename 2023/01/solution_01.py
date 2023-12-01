# GOAL:
#   Recover calibration value from each line of puzzle input 
#   Return the sum of the calibration values
#   Calibration value: combine first digit and last digit (in that order) to form a two-digit number

# examples:

# 1abc2         calibration value = 12
# pqr3stu8vwx   calibration value = 38
# a1b2c3d4e5f   calibration value = 15
# treb7uchet    calibration value = 77

#               SUM = 142

inputfile = "input.txt"
# inputfile = "input_test.txt"
f = open(inputfile, "r")

def concat_digits(first_digit,last_digit):
    return 10*first_digit + last_digit
#    return cval

def find_first(input_string):
    found_first=False
    for x in input_string:
        if not found_first and x.isdigit():
            found_first=True
            first_digit=int(x)
    return first_digit

cval_total = 0

for line in f:
    first_digit=find_first(line)
    last_digit=find_first(reversed(line))
    cval=concat_digits(first_digit, last_digit)
    cval_total+=cval

f.close()

print("Sum of calibration values:",cval_total)