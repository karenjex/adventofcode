# GOAL:

# Any number adjacent to a symbol, even diagonally, is a "part number".
# Find the sum of all of the part numbers in the engine schematic (periods (.) do not count as a symbol).

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

# 114 (top right) and 58 (middle right) are not part numbers because they are not adjacent to a symbol. 
# Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

inputfile = "input.txt"
f = open(inputfile, "r")

symbols=[]          # for each line, list of symbol positions
numbers=[]          # list of numbers and their coordinates

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

for y_coord,line in enumerate(f):
    line_length=len(line)
    line_symbols=[]     # create list of x_coordinates of symbols found on this line
    num_digits=[]
    num_x_coords=[]
    for x_coord, val in enumerate(line):
        if val in ['0','1','2','3','4','5','6','7','8','9']:
            num_digits.append(int(val))
            num_x_coords.append(x_coord)
        else:
            if num_digits!=[]:
                num_val=calculate_number(num_digits)
                # print(num_val)
                num={'val': num_val, 'y': y_coord, 'x': num_x_coords}
                numbers.append(num)
                # reset num_digits and line_digits
                num_digits=[]
                num_x_coords=[]
            if val != '\n' and val != '.':
                # add position of this symbol to list for this line
                line_symbols.append(x_coord)
    symbols.append(line_symbols)

num_lines=len(symbols)

sum_part_nums=0     # keep running total of part numbers

for num in numbers:
    # check if this is a part number (i.e. there's a symbol adjacent to the number). If so, add number to the sum
    # print('Checking number:',num['val'])
    val=num['val']
    y_coord = num['y']
    x_coords = num['x']     # list of x_coords
    symbol_found=False

    # get list of lines to check
    lines_to_check = [y_coord]
    if y_coord > 0:
        # if number not on first line, add line y-1 to lines to check 
        lines_to_check.append(y_coord-1)
    if y_coord < num_lines-1:
        # if number on last line, add line y+1 to lines to check
        lines_to_check.append(y_coord+1)

    # get list of positions to check
    positions_to_check = []
    for x in x_coords:
        # add x_coords to positions_to_check
        positions_to_check.append(x)
    # if first digit is not in first position, check position min_x-1
    if positions_to_check[0] > 0:
        positions_to_check.append(x_coords[0]-1)
    # if last digit is not in last position, check position max_x+1
    if positions_to_check[-1] < line_length-1:
        positions_to_check.append(x_coords[-1]+1)

    for line_num in lines_to_check:
        if not symbol_found:     # we haven't yet found a matching symbol - keep looking
            print('  checking line',line_num)
            line_to_check=symbols[line_num]
            for position in positions_to_check:
                if not symbol_found:     # we haven't yet found a matching symbol - keep looking
                    print('    checking position',position)
                    if position in line_to_check:
                        # this is a part number. Add it to the sum of part numbers and stop checking
                        symbol_found=True
                        print(val,'is a part number')
                        sum_part_nums+=val

f.close()

print(sum_part_nums)