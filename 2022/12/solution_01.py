# Goal: Find the fewest steps required to move from your current position to the location that should get the best signal

# Input represents heightmap of surrounding area.
# Elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, z is the highest
# Your current position is marked S (has elevation a)
# Location that gets best signal is marked E (has elevation z) 

# During each step, you can move exactly one square up, down, left, or right. 
# The elevation of the destination square can be at most one higher than the elevation of your current square (can be one higher, same or lower)

# Convert the grid into a directed graph: a series of vertices and (directed) edges
#   Vertices: coordinates for each point in the grid
#   Edges (directed): list of possible routes between two points. 
#                     There will be at most 4 edges from each point: to the square above, below, left and/or right

# example grid:
# ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm']       <-- call this row 0 or grid[0]
# ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l']
# ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k']
# ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j']
# ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']       <-- call this row 4 (or grid[4])

#   ^                                  ^
#   |                                  |
#  col 0                               col 7

V=[(0,0),(0,1),...,(0,7),...,(4,0),(4,1),...,(4,7)]
E=[[(0,0),(0,1)],[(0,0),(1,0)],...[(4,7),(3,7)],[(4,7),(4,6)]]

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

    print("current position:",current_coords)
    print("desired horizontal direction:",desired_h(current_coords))
    print("desired verical direction:",desired_v(current_coords))
    print("available left, right, up and down moves:")
    print("Can move right:",can_move(current_coords,"r"))
    print("Can move left:",can_move(current_coords,"l"))
    print("Can move up:",can_move(current_coords,"u"))
    print("Can move down:",can_move(current_coords,"d"))

    have_moved=False
    horizontal_dir=desired_h(current_coords)                         # first try to move in desired horizontal direction
    tried_l=False                 
    tried_r=False                 
    if horizontal_dir!='n':                                          # we want to move to the left or right
        if horizontal_dir=='r':                                      #     record that we have tried moving right
            tried_r=True
        else:                                                        #     record that we have tried moving left
            tried_l=True
        if can_move(current_coords,horizontal_dir):                  #     the move is allowed
            current_coords=move(current_coords,horizontal_dir)       #         move a step in the required horizontal direction
            print("have moved",horizontal_dir,"(required direction)")
            have_moved=True
        else:                                                        # we can't move in the required horizontal direction
            vertical_dir=desired_v(current_coords)                   #     now try to move in desired verticl direction
            if vertical_dir!='n':                                    #     we want to move up or down
                if horizontal_dir=='u':                              #     record that we have tried moving up
                    tried_u=True
                else:                                                #     record that we have tried moving down
                    tried_d=True
                if can_move(current_coords,vertical_dir):            #     the move is allowed 
                    current_coords=move(current_coords,vertical_dir) #         move a step in the required vertical direction
                    print("have moved",vertical_dir,"(required direction)")
                    have_moved=True
    else:                                                            # didn't want to move horizontally - try moving left then right
        if can_move(current_coords,"l"):                             #     can move left
            current_coords=move(current_coords,"l")                  #         move a step left
            print("didn't want to move horizontally but have moved left")
            have_moved=True
        elif can_move(current_coords,"r"):                           #     can move left
            current_coords=move(current_coords,"r")                  #         move a step left
            print("didn't want to move horizontally but have moved right")
            have_moved=True
    if have_moved==False and vertical_dir=="n":                      # if we still haven't moved and didn't want to move vertically - try moving up then down
        if can_move(current_coords,"u"):                             #     can move left
            current_coords=move(current_coords,"u")                  #         move a step left
            print("didn't want to move vertically but have moved up")
            have_moved=True
        elif can_move(current_coords,"d"):                           #     can move down
            current_coords=move(current_coords,"d")                  #         move a step down
            print("didn't want to move vertically but have moved down")
            have_moved=True
    if have_moved==False:                    # we haven't been able to move in the required direction.
        print("we weren't able to move in required vertical or horizontal direction")
    at_end=not(have_moved)
    # at_end=(current_coords==end_coords)         # stop when we get to "E"
    steps_moved+=1

print("steps moved:",steps_moved)