# Goal: Find the fewest steps required to move from your current position to the location that should get the best signal

# Input represents heightmap of surrounding area.
# Elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, z is the highest
# Your current position is marked S (has elevation a)
# Location that gets best signal is marked E (has elevation z) 

# During each step, you can move exactly one square up, down, left, or right. 
# The elevation of the destination square can be at most one higher than the elevation of your current square (can be one higher, same or lower)

# for each square, consider where we can go and where we want to go
# eg, for grid[0,0] in the following example,
#    move_l = False     (can not move left)
#    move_r = True      (can move right)
#    move_u = False     (can not move up)
#    move_d = True      ( can move down)
#    desired_h = r       (desired horizontal movement to get to E is "right" - could alternatively be l "left" or n "none")
#    desired_v = d       (desired vertical movement to get to E is "down" - could alternatively be u "up" or n "none")

# example:
# ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm']
# ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l']
# ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k']
# ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j']
# ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']

inputfile="input_test.txt"

grid=[]                 # each gridline in grid represents one set of y-coords
steps_moved=0
start_coords=()
end_coords=()
current_row=0

with open(inputfile) as f:
    for line in f:
        gridline=[]                # each char in gridline represents x-coord
        current_col=0
        for char in line.strip():
            if char=='S':
                start_coords=(current_col,current_row)
                gridline.append(ord('a'))                     # store integer representation of 'a'
            elif char=='E':
                end_coords=(current_col,current_row)
                gridline.append(ord('z'))                     # store integer representation of 'z'
            else:
                gridline.append(ord(char))                    # store integer representation of char
            current_col+=1
        print(gridline)
        grid.append(gridline)
        current_row+=1

numrows=len(grid)
numcols=len(gridline)
print(start_coords)
print(end_coords)

def can_move(coords,dir):
    # returns True if we can move in drection "dir" ("l","r","u" or "d") from the given coordinates
    current_x = coords[0]
    current_y = coords[1]
    can_move=False
    if dir=='l':
        # can move left from current_coords if not in first col and value at square to left is at most one more than value at current coords
        if current_x!=0:
            if (grid[current_y][current_x-1]<=grid[current_y][current_x]+1):
                can_move=True
    elif dir=='r':
        # can move right from current_coords if not in last col and value at square to right is at most one more than value at current coords
        if current_x!=numcols-1:
            if grid[current_y][current_x+1]<=grid[current_y][current_x]+1:
                can_move=True
    elif dir=='u':
    # can move up from current_coords if value at square above is at most one more than value at current coords
        if current_y!=0:
            if grid[current_y-1][current_x]<=grid[current_y][current_x]+1:
                can_move=True
    elif dir=='d':
        # can move down from current_coords if not in bottom row value at square below is at most one more than value at current coords
        if current_y!=numrows-1:
            if grid[current_y+1][current_x]<=grid[current_y][current_x]+1:
                can_move=True
    return can_move    

def desired_v(coords):
    # desired_v = vertical movement needed to get to "E" : "n" = none, "u" = up, "d" = down
    # check difference between current y and y coord of "E"
    current_y = coords[1]
    end_y = end_coords[1]
    if current_y == end_y:
        dir='n'
    elif current_y < end_y:
        dir='d'
    elif current_y > end_y:
        dir='u'
    return dir

def desired_h(coords):
    # desired_h = horizontal movement needed to get to E : "n" = none, "l" = left, "r" = right
    # check difference between current x and x coord of "E"
    current_x = coords[0]
    end_x = end_coords[0]
    if current_x == end_x:
        dir='n'
    elif current_x < end_x:
        dir='r'
    elif current_x > end_x:
        dir='l'
    return dir

def move(coords,dir):
    # move one square in specified direction
    current_x=coords[0]
    current_y=coords[1]
    if dir=='r':
        new_x=current_x+1
        new_y=current_y
    elif dir=='l':
        new_x=current_x-1
        new_y=current_y
    elif dir=='u':
        new_x=current_x
        new_y=current_y-1
    elif dir=='d':
        new_x=current_x
        new_y=current_y+1
    return(new_x,new_y)

# Start at S, continue until we reach E, moving one step at a time
current_coords=start_coords
at_end=False
while not at_end:
    print(current_coords)
    print("desired horizontal and verical direction:")
    print(desired_h(current_coords),desired_v(current_coords))
    print("available left, right, up and down moves:")
    print(can_move(current_coords,"l"),can_move(current_coords,"r"),can_move(current_coords,"u"),can_move(current_coords,"d"))
    # move one step
    # attempt to move in the required horizontal or vertical direction:
    have_moved=False
    horizontal_dir=desired_h(current_coords)                         # first try to move in desired horizontal direction
    tried_l=False       # record whether or not we have attempted to move left
    tried_r=False       # record whether or not we have attempted to move right
    if horizontal_dir!='n':                                          # we want to move to the left or right
        if horizontal_dir=='r':         # record that we have tried moving right
            tried_r=True
        else:                           # record that we have tried moving left
            tried_l=True
        if can_move(current_coords,horizontal_dir):                  #     the move is allowed
            current_coords=move(current_coords,horizontal_dir)       #     move a step in the required horizontal direction
            have_moved=True
        else:                                                        # we can't move in the required horizontal direction
            vertical_dir=desired_v(current_coords)                   #     now try to move in desired verticl direction
            if vertical_dir!='n':                                    #     we want to move up or down
                if horizontal_dir=='u':         # record that we have tried moving up
                    tried_u=True
                else:                           # record that we have tried moving down
                    tried_d=True
                if can_move(current_coords,vertical_dir):            #         the move is allowed 
                    current_coords=move(current_coords,vertical_dir) #     move a step in the required vertical direction
                    have_moved=True
    else:                                                            # didn't want to move horizontally - try moving left then right
        if can_move(current_coords,"l"):                             #     can move left
            current_coords=move(current_coords,"l")                  #         move a step left
            have_moved=True
        elif can_move(current_coords,"r"):                           #     can move left
            current_coords=move(current_coords,"r")                  #         move a step left
            have_moved=True
    if have_moved==False and vertical_dir=="n":                      # didn't want to move vertically - try moving up then down
        if can_move(current_coords,"u"):                             #     can move left
            current_coords=move(current_coords,"u")                  #         move a step left
            have_moved=True
        elif can_move(current_coords,"d"):                           #     can move down
            current_coords=move(current_coords,"d")                  #         move a step down
            have_moved=True

    if have_moved==False:                    # we haven't been able to move in the required direction.
        print("we weren't able to move in required vertical or horizontal direction")
    # at_end=True
    at_end=(current_coords==end_coords)         # stop when we get to "E"
    steps_moved+=1

print("steps moved:",steps_moved)