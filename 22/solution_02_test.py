# Goal: Find the final password, calculated as follows:
#   (1000 x final_row) + (4 x final_column) + final_facing
#      Rows start from 1 at the top and count downward (including empty spaces)
#      Columns start from 1 at the left and count rightward (including empty spaces)
#      Facing: 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)

# This time, consider the map as a cube, so the wrapping rules change.
  
import re

inputfile = "input_test.txt"    # expected result:  1000 * 5 + 4 * 7 + 3 = 5031

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

# 1. Find shape of cube's net. We're cheating for now - looked at the input to determine the shape

#      0     1      2      3
#                -------
# 0              | 2,0 |
#    -------------------
# 1  | 0,1 | 1,1 | 2,1 |
#    -------------------------
# 2              | 2,2 | 3,2 | 
#                ------------- 

# L (2) from 2,0: D (1) to 1,1 (same)
# U (3) from 2,0: D (1) to 0,1 (opp)
# R (0) from 2,0: L (2) to 3,2 (opp)
# R (0) from 2,1: D (1) to 3,2 (opp)
# U (3) from 3,2: L (2) to 2,1 (opp)
# R (0) from 3,2: L (2) to 2,0 (opp)
# D (1) from 3,2: R (0) to 0,1 (opp)
# D (1) from 2,2: U (3) to 0,1 (opp)
# L (2) from 2,2: U (3) to 1,1 (opp)
# D (1) from 1,1: R (0) to 2,2 (opp)
# D (1) from 0,1: U (3) to 2,2 (opp)
# L (2) from 0,1: U (3) to 3,2 (opp)
# U (3) from 0,1: D (1) to 2,0 (opp)
# U (3) from 1,1: R (0) to 2,0 (same)

max_row_len=0
for row in map:
    if len(row)>max_row_len:
        max_row_len=len(row)

section_length=int(max_row_len/4)       # length of sides of cube

# find coordinates of edges of each side of the cube

sides={}

for i in range(4):
    for j in range(3):
        start_col=i*section_length
        end_col=start_col+(section_length-1)
        start_row=j*section_length
        end_row=start_row+(section_length-1)
        side={'start_col':start_col,'end_col':end_col, 'start_row':start_row, 'end_row':end_row}
        sides[(i,j)]=side

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
    proposed_new_facing = facing
    if facing==0:               # right (>)
        proposed_new_row=row
        proposed_new_col=col+1
        if col==last_cols[row]:        # we're currently at the last col for this row - wraparound
            if   row >= 0 and row <= section_length-1:                      # side (2,0) --> L (2) to 3,2 (opp)
                proposed_new_col=sides[(3,2)]['end_col']
                proposed_new_row=sides[(3,2)]['end_row'] - (row - sides[(2,0)]['start_row'])
                proposed_new_facing=2
            elif row >= section_length   and row <= (2*section_length)-1:   # side (2,1) --> D (1) to 3,2 (opp)
                proposed_new_col=sides[(3,2)]['end_col'] - (row - sides[(2,1)]['start_row'])
                proposed_new_row=sides[(3,2)]['start_row']
                proposed_new_facing=1
            elif row >= 2*section_length and row <= (3*section_length)-1:   # side (3,2) --> L (2) to 2,0 (opp)
                proposed_new_col=sides[(2,0)]['end_col']
                proposed_new_row=sides[(2,0)]['end_row'] - (row - sides[(3,2)]['start_row'])
                proposed_new_facing=2
    elif facing==1:             # down (v)
        proposed_new_row=row+1
        proposed_new_col=col
        if row==last_rows[col]:        # we're currently at the last row for this col - wraparound to first row
            if   col >= 0 and col <= section_length-1:                      # side (0,1) --> U (3) to 2,2 (opp)
                proposed_new_col=sides[(2,2)]['end_col'] - (col - sides[(0,1)]['start_col'])
                proposed_new_row=sides[(2,2)]['end_row']
                proposed_new_facing=3
            elif col >= section_length   and col <= (2*section_length)-1:   # side (1,1) --> R (0) to 2,2 (opp)
                proposed_new_col=sides[(2,2)]['start_col']
                proposed_new_row=sides[(2,2)]['end_row'] - [col - sides[(1,1)]['start_col']]
                proposed_new_facing=0
            elif col >= 2*section_length and col <= (3*section_length)-1:   # side (2,2) --> U (3) to 0,1 (opp)
                proposed_new_col=sides[(0,1)]['end_col'] - (col - sides[(2,2)]['start_col'])
                proposed_new_row=sides[(0,1)]['end_row']
                proposed_new_facing=3
            elif col >= 3*section_length and col <= (4*section_length)-1:   # side (3,2) --> R (0) to 0,1 (opp)
                proposed_new_col=sides[(0,1)]['start_col']
                proposed_new_row=sides[(0,1)]['end_row'] - [col - sides[(3,2)]['start_col']]
                proposed_new_facing=0
    elif facing==2:             # left (<)
        proposed_new_row=row
        proposed_new_col=col-1
        if col==first_cols[row]:        # we're currently at the first col for this row - wraparound to last col
            if   row >= 0 and row <= section_length-1:                      # side (2,2) --> U (3) to 1,1 (opp)
                proposed_new_col=sides[(1,1)]['end_col'] - (row - sides[(2,2)]['start_row'])
                proposed_new_row=sides[(1,1)]['end_row']
                proposed_new_facing=3
            elif row >= section_length   and row <= (2*section_length)-1:   # side (0,1) --> U (3) to 3,2 (opp)
                proposed_new_col=sides[(3,2)]['end_col'] - (row - sides[(0,1)]['start_row'])
                proposed_new_row=sides[(3,2)]['end_row']
                proposed_new_facing=3
            elif row >= 2*section_length and row <= (3*section_length)-1:   # side (2,0) --> D (1) to 1,1 (same)
                proposed_new_col=sides[(1,1)]['start_col'] + (row - sides[(2,0)]['start_row'])
                proposed_new_row=sides[(1,1)]['start_row']
                proposed_new_facing=1
    elif facing==3:              # up (^)
        proposed_new_row=row-1
        proposed_new_col=col
        if row==first_rows[col]:        # we're currently at the first row for this col - wraparound to last row
            if   col >= 0 and col <= section_length-1:                      # side (0,1) --> D (1) to 2,0 (opp)
                proposed_new_col=sides[(2,0)]['end_col'] - (col - sides[(0,1)]['start_col'])
                proposed_new_row=sides[(2,0)]['start_row']
                proposed_new_facing=1
            elif col >= section_length   and col <= (2*section_length)-1:   # side (1,1) --> R (0) to 2,0 (same)
                proposed_new_col=sides[(2,0)]['start_col']
                proposed_new_row=sides[(2,0)]['start_row'] + (col - sides[(1,1)]['start_col'])
                proposed_new_facing=0
            elif col >= 2*section_length and col <= (3*section_length)-1:   # side (2,0) --> D (1) to 0,1 (opp)
                proposed_new_col=sides[(0,1)]['end_col'] - (col - sides[(2,0)]['start_col'])
                proposed_new_row=sides[(0,1)]['start_row']
                proposed_new_facing=1
            elif col >= 3*section_length and col <= (4*section_length)-1:   # side (3,2) --> L (2) to 2,1 (opp)
                proposed_new_col=sides[(2,1)]['end_col']
                proposed_new_row=sides[(2,1)]['end_row'] - (col - sides[(3,2)]['start_col'])
                proposed_new_facing=2
    if map[proposed_new_row][proposed_new_col]==2:      # we've hit a wall - don't move
        hit_a_wall=True
        new_row=row
        new_col=col
        new_facing=facing
    else:                              # move to new position
        hit_a_wall=False
        new_row=proposed_new_row
        new_col=proposed_new_col
        new_facing=proposed_new_facing
    return(new_row, new_col, new_facing, hit_a_wall)

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
                    current_facing=step_info[2]
                    hit_a_wall=step_info[3]
                    # print('after step',x,': row',current_row,'col',current_column,' hit a wall?',hit_a_wall)
            print('moved',step_count,'Now at row',current_row,'col',current_column,'facing',current_facing)
        else:
            direction=i
            get_count=True
            if direction=='R':
                current_facing=(current_facing+1)%4
            elif direction=='L':
                current_facing=(current_facing-1)%4
            print('turned',direction,'Now facing',current_facing)

final_row=current_row+1         # add 1 to row index to get row number
final_column=current_column+1   # add 1 to col index to get col number

final_password = (1000 * final_row) + (4 * final_column) + current_facing

print("final password = 1000 * ",final_row,'+ 4 *',final_column,'+',current_facing,'=',final_password)

print('each side is',section_length,'long')
