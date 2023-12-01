# Goal: Find how many positions the tail of the rope visits at least once. The rope now consists of 10 knots: head = 0, tail = 9

# Current position of head (knots[0]) to tail (knots[9]) : all start at (0,0)

knots=[]
for i in range(10):
   knots.append((0,0))    

# print(knots)

# track positions visited by tail:

positions_visited=[(0,0)]        # list of positions visited (starts at (0,0) so we can add this immediately)
num_visited=1                    # start position (0,0) counted immediately

inputfile = "input.txt"

with open(inputfile) as f:
    for line in f:

        head_pos=knots[0]
        h_pos_x=head_pos[0]
        h_pos_y=head_pos[1]

        # print("\nProcessing instruction:",line)
        direction = line.split()[0]            # 1st word (L, R, U or D) : direction of move
        distance = int(line.split()[1])        # 2nd word (integer) : number of steps to move

        for i in range(distance):              # move head one step at a time in specified direction
            if direction=="R":
                h_pos_x+=1                         # increase x coord by 1
            elif direction=="L":
                h_pos_x+=-1                        # decrease x coord by 1
            elif direction=="U":
                h_pos_y+=1                         # increase y coord by 1
            elif direction=="D":
                h_pos_y+=-1                        # decrease y coord by 1
            head_pos = (h_pos_x,h_pos_y)
            knots[0]=head_pos
            # print("head has moved to",h_pos)

            # for each know from 1 to 9, check and move if needed
            for i in range(1,10):

                prev_knot_pos=knots[i-1]
                prev_knot_pos_x=prev_knot_pos[0]
                prev_knot_pos_y=prev_knot_pos[1]

                curr_knot_pos=knots[i]
                curr_knot_pos_x=curr_knot_pos[0]
                curr_knot_pos_y=curr_knot_pos[1]

                if not(curr_knot_pos_x-prev_knot_pos_x>-2 and curr_knot_pos_x-prev_knot_pos_x<2 and curr_knot_pos_y-prev_knot_pos_y>-2 and curr_knot_pos_y-prev_knot_pos_y<2):    # head and tail not touching
                    # print("head and tail are not touching: head is at",h_pos,"tail is at",t_pos)
                    if prev_knot_pos_y==curr_knot_pos_y:                      # head and tail are in the same column:
                        if curr_knot_pos_x-prev_knot_pos_x>=2:                    # tail too far right, move a step left
                            curr_knot_pos_x+=-1
                        elif curr_knot_pos_x-prev_knot_pos_x<=-2:                 # tail too far left, move a step right
                            curr_knot_pos_x+=1
                    elif prev_knot_pos_x==curr_knot_pos_x:                    # head and tail in the same row:
                        if curr_knot_pos_y-prev_knot_pos_y>=2:                    # tail too far up, move a step down
                            curr_knot_pos_y+=-1
                        elif curr_knot_pos_y-prev_knot_pos_y<=-2:                 # tail too far down, move a step up
                            curr_knot_pos_y+=1
                    else:                                     # not in same row or column - move diagonally (one step L/R *and* one step U/D)
                        if prev_knot_pos_y<curr_knot_pos_y:                       # tail above head
                            curr_knot_pos_y += -1                             # move a step down
                        elif prev_knot_pos_y>curr_knot_pos_y:                     # tail below head
                            curr_knot_pos_y += 1                              # move a step up
                        if prev_knot_pos_x<curr_knot_pos_x:                       # tail to right of head
                            curr_knot_pos_x += -1                             # move a step left
                        elif prev_knot_pos_x>curr_knot_pos_x:                     # tail to left of head
                            curr_knot_pos_x += 1                              # move a step right
                curr_knot_pos=(curr_knot_pos_x,curr_knot_pos_y)
                knots[i]=curr_knot_pos
            # print("tail is now in",t_pos)
            already_visited=False                         # assume we haven't yet visited this position
            for entry in positions_visited:               # check the positions visited so far
                if entry==curr_knot_pos:                              # we've already visited this position
                    # print("we've already visited",t_pos,"(we've visited",num_visited,"positions so far)")
                    already_visited=True
            if not(already_visited):                      # we haven't yet visited this position
                positions_visited.append(curr_knot_pos)               # add to list of positions we've already visited
                num_visited+=1                                # increase count of positions visited so far
                # print("first time visiting",t_pos,"(we've now visited",num_visited,"positions)")


# Final output:
# print("positions visited:",positions_visited)
print("\nNumber of positions visited by tail at least once:",num_visited)
