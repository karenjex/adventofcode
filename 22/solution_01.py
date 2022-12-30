# Goal: Find the final password, calculated as follows:
#   (1000 x final_row) + (4 x final_column) + final_facing
#      Rows start from 1 at the top and count downward (including empty spaces)
#      Columns start from 1 at the left and count rightward (including empty spaces)
#      Facing: 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)

import re

# inputfile = "input_test.txt"    # expected result:  1000 * 6 + 4 * 8 + 0 = 6032
inputfile = "input.txt"

# process input to get map:

map=[]   # list of rows of tiles
row=[]   # list of spaces:  0 = blank, 1 = open tile, 2 = wall

process_instructions=False
with open(inputfile) as f:
    for line in f:
        if not process_instructions:
            for tile in line:
                if tile==' ':
                    row.append(0)       # space
                elif tile=='.':
                    row.append(1)       # open tile
                elif tile=='#':
                    row.append(2)       # wall
            if row != []:
                map.append(row)         # add row to map if it's not empty
                row=[]                  # clear row ready for next line
            else:
                process_instructions=True  # if last row was empty, next line contains instructions
        elif process_instructions:
            instruction_line=re.split('(\d+)',line.strip())     # split instructions into numbers and directions


# print('map:')
# for row in map:
#     print(row)

max_row_len=0
for row in map:
    if len(row)>max_row_len:
        max_row_len=len(row)

# Find position of first tile/wall per row:
first_cols=[]
for row in map:
    col=0
    for space in row:
        if space==0:
            col+=1
        else:
            first_cols.append(col)
            break
# print('first column of each row that contains a tile or wall:',first_cols)

# Find position of last tile/wall per row:
last_cols=[]
for row in map:
    for col in range(len(row)-1,-1,-1):
        if row[col]!=0:
            last_cols.append(col)
            break
# print('last column of each row that contains a tile or wall:',last_cols)

# Find position of first tile/wall per col:
first_rows=[]
for c in range(max_row_len):        # for each (potential) column c
    for r in range(len(map)):       # check column c of each row r
        if len(map[r])>c and map[r][c]!=0:
            first_rows.append(r)
            break
# print('first row of each column that contains a tile or wall:',first_rows)

# Find position of last tile/wall per col:
last_rows=[]
for c in range(max_row_len):                # for each column c
    for r in range(len(map)-1,-1,-1):       # check column c of each row r
        if len(map[r])>c and map[r][c]!=0: 
            last_rows.append(r)
            break
# print('last row of each column that contains a tile or wall:',last_rows)

def take_a_step(row, col, facing):
    # move one step in the proposed direction if there is no wall
    if facing==0:               # right (>)
        proposed_new_row=row
        proposed_new_col=col+1
        if col==last_cols[row]:        # we're currently at the last col for this row - wraparound to first col
            proposed_new_col=first_cols[row]
    elif facing==1:             # down (v)
        proposed_new_row=row+1
        proposed_new_col=col
        if row==last_rows[col]:        # we're currently at the last row for this col - wraparound to first row
            proposed_new_row=first_rows[col]
    elif facing==2:             # left (<)
        proposed_new_row=row
        proposed_new_col=col-1
        if col==first_cols[row]:        # we're currently at the first col for this row - wraparound to last col
            proposed_new_col=last_cols[row]
    elif facing==3:              # up (^)
        proposed_new_row=row-1
        proposed_new_col=col
        if row==first_rows[col]:        # we're currently at the first row for this col - wraparound to last row
            proposed_new_row=last_rows[col]
    if map[proposed_new_row][proposed_new_col]==2:      # we've hit a wall - don't move
        hit_a_wall=True
        new_row=row
        new_col=col
    else:                              # move to new position
        hit_a_wall=False
        new_row=proposed_new_row
        new_col=proposed_new_col
    return(new_row, new_col, hit_a_wall)

current_row=0                       # first row in map
current_column=first_cols[0]        # first open tile in first row
current_facing=0                    # 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)

get_count=True
for i in instruction_line:
    if i!='':
        if get_count:
            step_count=int(i)
            get_count=False
            hit_a_wall=False
            for x in range(step_count):
                if not hit_a_wall:
                    # move 1 step in current direction
                    step_info=take_a_step(current_row, current_column, current_facing)
                    current_row=step_info[0]
                    current_column=step_info[1]
                    hit_a_wall=step_info[2]
                    # print('after step',x,': row',current_row,'col',current_column,' hit a wall?',hit_a_wall)
        else:
            direction=i
            get_count=True
            if direction=='R':
                current_facing=(current_facing+1)%4
            elif direction=='L':
                current_facing=(current_facing-1)%4
            # print('now at row',current_row,'col',current_column,'facing',current_facing)

final_row=current_row+1         # add 1 to row index to get row number
final_column=current_column+1   # add 1 to col index to get col number

final_password = (1000 * final_row) + (4 * final_column) + current_facing

print("final password = 1000 * ",final_row,'+ 4 *',final_column,'+',current_facing,'=',final_password)
