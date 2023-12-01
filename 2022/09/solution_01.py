# Goal: Find how many positions the tail of the rope visits at least once

# Current position of head (h) and tail (t) : both start at (0,0)

h_pos=(0,0)
t_pos=(0,0)

# track positions visited by tail (coordinates and number of times visited):

positions_visited=[(0,0)]        # list of positions visited
num_visited=1

inputfile = "input.txt"

with open(inputfile) as f:
    for line in f:
        # print("\nProcessing instruction:",line)
        direction = line.split()[0]            # 1st word (L, R, U or D) : direction of move
        distance = int(line.split()[1])        # 2nd word (integer) : number of steps to move
        h_pos_x=h_pos[0]
        h_pos_y=h_pos[1]
        t_pos_x=t_pos[0]
        t_pos_y=t_pos[1]
        for i in range(distance):              # move head one step at a time in specified direction
            if direction=="R":
                h_pos_x+=1                         # increase x coord by 1
            elif direction=="L":
                h_pos_x+=-1                        # decrease x coord by 1
            elif direction=="U":
                h_pos_y+=1                         # increase y coord by 1
            elif direction=="D":
                h_pos_y+=-1                        # decrease y coord by 1
            h_pos = (h_pos_x,h_pos_y)
            # print("head has moved to",h_pos)
            # check and move tail if needed:
            if not(t_pos_x-h_pos_x>-2 and t_pos_x-h_pos_x<2 and t_pos_y-h_pos_y>-2 and t_pos_y-h_pos_y<2):    # head and tail not touching
                # print("head and tail are not touching: head is at",h_pos,"tail is at",t_pos)
                if h_pos_y==t_pos_y:                      # head and tail are in the same column:
                    if t_pos_x-h_pos_x>=2:                    # tail too far right, move a step left
                        t_pos_x+=-1
                    elif t_pos_x-h_pos_x<=-2:                 # tail too far left, move a step right
                        t_pos_x+=1
                elif h_pos_x==t_pos_x:                    # head and tail in the same row:
                    if t_pos_y-h_pos_y>=2:                    # tail too far up, move a step down
                        t_pos_y+=-1
                    elif t_pos_y-h_pos_y<=-2:                 # tail too far down, move a step up
                        t_pos_y+=1
                else:                                     # not in same row or column - move diagonally (one step L/R *and* one step U/D)
                    if h_pos_y<t_pos_y:                       # tail above head
                        t_pos_y += -1                             # move a step down
                    elif h_pos_y>t_pos_y:                     # tail below head
                        t_pos_y += 1                              # move a step up
                    if h_pos_x<t_pos_x:                       # tail to right of head
                        t_pos_x += -1                             # move a step left
                    elif h_pos_x>t_pos_x:                     # tail to left of head
                        t_pos_x += 1                              # move a step right
            t_pos=(t_pos_x,t_pos_y)
            # print("tail is now in",t_pos)
            already_visited=False                         # assume we haven't yet visited this position
            for entry in positions_visited:               # check the positions visited so far
                if entry==t_pos:                              # we've already visited this position
                    # print("we've already visited",t_pos,"(we've visited",num_visited,"positions so far)")
                    already_visited=True
            if not(already_visited):                      # we haven't yet visited this position
                positions_visited.append(t_pos)               # add to list of positions we've already visited
                num_visited+=1                                # increase count of positions visited so far
                # print("first time visiting",t_pos,"(we've now visited",num_visited,"positions)")


# Final output:
# print("positions visited:",positions_visited)
print("\nNumber of positions visited by tail at least once:",num_visited)
