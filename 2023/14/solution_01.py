# GOAL: 

# Calculate the total load caused by all of the rounded rocks after tilting the platform so the rounded rocks all roll north

#   0 = rounded rock (moves when you tilt the lever)
#   # = square rock (does not move and does not contribute to load)
#   . = no rock

# Example:

# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....

# Tilt the lever so all of the rocks will slide north as far as they will go:

# OOOO.#.O..
# OO..#....#
# OO..O##..O
# O..#.OO...
# ........#.
# ..#....#.#
# ..O..#.O.O
# ..O.......
# #....###..
# #....#....

# The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on.
# The amount of load caused by each rock in each row is as follows:

#               values with 10 rows on the platform (i.e. num_rows = 10)
#            load_multiplier    row_id
# OOOO.#.O..   10               0              10 - 0 = 10 (i.e. num_rows - row_id = multiplier)
# OO..#....#    9               1              ...
# OO..O##..O    8               2              ...
# O..#.OO...    7               3              ...
# ........#.    6               4              ...
# ..#....#.#    5               5              ...
# ..O..#.O.O    4               6              ...
# ..O.......    3               7              ...
# #....###..    2               8              10 - 8 = 2 (i.e. num_rows - row_id = multiplier)
# #....#....    1               9              10 - 9 = 1 (i.e. num_rows - row_id = multiplier)

# The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.


class RockGrid:

    def __init__(self, rock_columns):
        self.rock_columns = rock_columns
        self.num_cols=len(rock_columns)
        self.num_rows=len(rock_columns[0])
        self.tilted_to_north = self.tilt_north()

    def tilt_north(self):
        # tilt each column north
        tilted_to_north=[]
        for col in self.rock_columns:   # process one column of rocks at a time
            print('tilting column',col)
            new_col={}                  # create a dictionary to contain the new rock positions
            furthest_roll_point=0       # track the furthest point a rock can roll back to
                                        # this will either be the first row (0), or the position of the last rock found in the column
            for index, rock in enumerate(col):
                print('processing position',index,'(',rock,')')
                if rock=='#':           # this is a square rock. It doesn't move
                    new_col[index]='#'
                    furthest_roll_point=index+1       # future rocks can now only roll back as far as the next position after the current rock
                    print('rocks can roll back to',index+1)
                elif rock=='.':         # there is no rock here. There may be a round rock ahead that will roll here. Let's wait and see
                    new_col[index]='.'
                elif rock=='O':         # this is a round rock. It might roll if there's space behind it, and if it's not already in the first row.
                    if index==0:        # The rock's in the first row so it can't roll
                        new_col[index]='O'
                        furthest_roll_point=index+1       # this is the new furthest point that a rock can roll back to
                        print('rocks can roll back to',index+1)
                    else:           # if furthest_roll_point is before the current position, roll the rock backwards
                        if furthest_roll_point<index:
                            new_col[furthest_roll_point]='O'
                            furthest_roll_point+=1       # this is the new furthest point that a rock can roll back to
                            print('rocks can roll back to',index+1)
                            for i in range(furthest_roll_point,index+1):      # fill the spaces between the rolled rock and current position with spaces
                                new_col[i]='.'
                        else:
                            new_col[index]='O'
                            furthest_roll_point=index+1       # this is the new furthest point that a rock can roll back to
                            print('rocks can roll back to',index+1)

            tilted_to_north.append(new_col)
        return tilted_to_north

    def get_total_load(self):
        # calculate total load once grid has been tilted north
        total_load=0
        for row_id in range(0,self.num_rows):
            print('calculating load for row',row_id)
            row_load_multiplier=self.num_rows - row_id      # distance from far edge
            num_rocks=0
            for col in self.tilted_to_north:
                if col[row_id]=='O':
                    num_rocks+=1
            row_load = num_rocks*row_load_multiplier
            print('row:',row_id,'has',num_rocks,'rocks and multiplier',row_load_multiplier,'i.e. a load of',row_load)
            total_load+=row_load
        return total_load

inputfile = "input.txt"
f = open(inputfile, "r")

total_load=0

rock_columns=[]

for row_index,line in enumerate(f):     # process each line in the input file
    # print('processing input line',row_index)
    line=line.split('\n')[0]        # remove the newline character
    for col_index,value in enumerate(line):         # process each position in the line
        if row_index==0:        # we're processing the first row
            column=[value]                       # create a list to contain the values this column and add it to the list of rock_columns
            rock_columns.append(column)
        else:
            rock_columns[col_index].append(value)        # add the value to the current column
    
# now we have our grid as a list of columns

rock_grid=RockGrid(rock_columns)
for col in rock_grid.tilted_to_north:
    print(col)


f.close()

print('Total Load:',rock_grid.get_total_load())