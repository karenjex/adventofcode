# GOAL:

# A gear is any * symbol that is adjacent to exactly two part numbers. 
# Its gear ratio is the result of multiplying those two numbers together.

# Find the gear ratio of every gear and add them all up.

# Example:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# The first gear has part numbers 467 and 35, so its gear ratio is 16345. 
# The second gear is in the lower right; its gear ratio is 451490.
# Adding up all of the gear ratios produces 467835.

inputfile = "input.txt"
f = open(inputfile, "r")

asterisks=[]      # list of asterisk (potential gear) positions
numbers=[]        # list of numbers and their coordinates

def calculate_number(num_digits):
    # calculate number based on series of digits
    num=0
    len_num=len(num_digits)
    for index,digit in enumerate(num_digits):
        # print('digit:',digit,'index:',index)
        power=(len_num-1)-index     # multiply digit by this power of 10
        val = digit*10**power
        num+=val
    return num       

def get_coords_to_check(coords):
    coords_to_check=[]
    x_coord=coords[0]
    y_coord=coords[1]
    # if not in first row, check row above
    if y_coord!=0:
        # if not in first position, check position to left
        if x_coord!=0:
            coords_to_check.append((x_coord-1, y_coord-1))
        coords_to_check.append((x_coord, y_coord-1))
        # if not in last position, check position to right
        if x_coord!=line_length-1:
            coords_to_check.append((x_coord+1, y_coord-1))
    # check current row
    # if not in first position, check position to left
    if x_coord!=0:
        coords_to_check.append((x_coord-1, y_coord))
    # if not in last position, check position to right
    if x_coord!=line_length-1:
        coords_to_check.append((x_coord+1, y_coord))
    # if not last row, check row below
    if y_coord!=final_line:
        # if not in first position, check position to left
        if x_coord!=0:
            coords_to_check.append((x_coord-1, y_coord+1))
        coords_to_check.append((x_coord, y_coord+1))
        # if not in last position, check position to right
        if x_coord!=line_length-1:
            coords_to_check.append((x_coord+1, y_coord+1))
    return coords_to_check

for y_coord,line in enumerate(f):
    line_length=len(line)
    num_digits=[]
    num_coords=[]
    for x_coord, val in enumerate(line):
        if val in ['0','1','2','3','4','5','6','7','8','9']:
            num_digits.append(int(val))
            num_coords.append((x_coord,y_coord))
        else:
            if num_digits!=[]:
                num_val=calculate_number(num_digits)
                # print(num_val)
                num={'val': num_val, 'coords': num_coords}
                numbers.append(num)
                # reset num_digits and line_digits
                num_digits=[]
                num_coords=[]
            if val=='*':
                # add position of this asterisk to list for this line
                asterisks.append((x_coord,y_coord))
    final_line=y_coord

sum_gear_ratios=0     # keep running total of gear ratios

for potential_gear in asterisks:
    # Check each asterisk to find out if it is a gear - i.e. it is connected by 2 nunbers

    num1=0
    num2=0
    
    coords_to_check=get_coords_to_check(potential_gear)

    for number in numbers:
        # if part of number is in coords_to_check, this is num1 or num2
        num_connected_to_gear=False
        for coords in number['coords']:
            if not num_connected_to_gear:                   # don't continue checking if the number has already been identified as part of gear
                for coord_to_check in coords_to_check:
                    if not num_connected_to_gear:                   # don't continue checking if the number has already been identified as part of gear
                        if coords==coord_to_check:
                            num_connected_to_gear=True          # stop checking this number
                            if num1==0:
                                num1=number['val']
                            elif num2==0:
                                num2=number['val']
    if num1>0 and num2>0:
        sum_gear_ratios+=(num1*num2)

f.close()

print(sum_gear_ratios)