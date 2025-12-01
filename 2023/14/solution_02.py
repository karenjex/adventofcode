# GOAL: 

# Calculate the total load caused by all of the rounded rocks after 1000000000 spin cycles.
# Each cycle tilts the platform so the rounded rocks all roll north as far as they will go, then west, then south, then east 

class RockGrid:

    def __init__(self, rock_columns):
        self.rock_columns = rock_columns
        self.num_cols=len(rock_columns)
        self.num_rows=len(rock_columns[0])

    def rows_to_cols(self,rows):
        # convert a list of rows to a list of columns
        rock_columns=[]
        for y,line in enumerate(rows):        # process each row in rows
            # print('converting row',y,':',line,'into columns')
            for x in line:   # process each position (col index) in the row
                # print('the value of this entry is',line[x])
                if y==0:        # we're processing the first row
                    column={y:line[x]}  # create a dictionary to contain the values this column and add it to the list of rock_columns
                    rock_columns.append(column)
                else:
                    rock_columns[x][y]=line[x]        # add the value to the current column
        # print('rows_to_columns:',rock_columns)
        return rock_columns

    def tilt_north(self):
        # tilt each column north
        tilted_to_north=[]
        for col in self.rock_columns:   # process one column of rocks at a time
            # print('tilting column',col)
            new_col={}                  # create a dictionary to contain the new rock positions
            furthest_roll_point=0       # track the furthest point a rock can roll back to
                                        # this will either be the first row (0), or the position of the last rock found in the column
            for index in range(0,self.num_rows):
                rock=col[index]
                # print('processing position',index,'(',rock,')')
                if rock=='#':           # this is a square rock. It doesn't move
                    new_col[index]='#'
                    furthest_roll_point=index+1       # future rocks can now only roll back as far as the next position after the current rock
                    # print('rocks can roll back to',index+1)
                elif rock=='.':         # there is no rock here. There may be a round rock ahead that will roll here. Let's wait and see
                    new_col[index]='.'
                elif rock=='O':         # this is a round rock. It might roll if there's space behind it, and if it's not already in the first row.
                    if index==0:        # The rock's in the first row so it can't roll
                        new_col[index]='O'
                        furthest_roll_point=index+1       # this is the new furthest point that a rock can roll back to
                        # print('rocks can roll back to',index+1)
                    else:           # if furthest_roll_point is before the current position, roll the rock backwards
                        if furthest_roll_point<index:
                            new_col[furthest_roll_point]='O'
                            furthest_roll_point+=1       # this is the new furthest point that a rock can roll back to
                            # print('rocks can roll back to',index+1)
                            for i in range(furthest_roll_point,index+1):      # fill the spaces between the rolled rock and current position with spaces
                                new_col[i]='.'
                        else:
                            new_col[index]='O'
                            furthest_roll_point=index+1       # this is the new furthest point that a rock can roll back to
                            # print('rocks can roll back to',index+1)
            tilted_to_north.append(new_col)
        self.rock_columns=tilted_to_north
        return tilted_to_north

    def get_row(self,row_id):
        # for the given row_id, get the entire row, i.e. c1[row_id],c2[row_id],...,cn[row_id] for each column c
        row={}
        for col_id in range(0,self.num_cols):    # for each column in rock_columns
            value=self.rock_columns[col_id][row_id]
            # print('value in position',row_id,'of column',col_id,'is:',value)
            # get the value in position "row_id" from column i
            row[col_id]=value
        return row

    def tilt_west(self):
        # tilt each row west
        tilted_to_west=[]
        for row_id in range(0,self.num_rows):
            row_to_tilt=self.get_row(row_id)
            # print('tilting row',row_to_tilt)
            new_row={}                  # create a dictionary to contain the new rock positions
            furthest_roll_point=0       # track the furthest point a rock can roll back to
                                        # this will either be the first col (0), or the position of the last rock found in the row
            for index in range(0,self.num_cols):
                rock=row_to_tilt[index]
                # print('processing position',index,'(',rock,')')
                if rock=='#':           # this is a square rock. It doesn't move
                    new_row[index]='#'
                    furthest_roll_point=index+1       # future rocks can now only roll back as far as the next position after the current rock
                    # print('rocks can roll back to',index+1)
                elif rock=='.':         # there is no rock here. There may be a round rock ahead that will roll here. Let's wait and see
                    new_row[index]='.'
                elif rock=='O':         # this is a round rock. It might roll if there's space behind it, and if it's not already in the first row.
                    if index==0:        # The rock's in the first row so it can't roll
                        new_row[index]='O'
                        furthest_roll_point=index+1       # this is the new furthest point that a rock can roll back to
                        # print('rocks can roll back to',index+1)
                    else:           # if furthest_roll_point is before the current position, roll the rock backwards
                        if furthest_roll_point<index:
                            new_row[furthest_roll_point]='O'
                            furthest_roll_point+=1       # this is the new furthest point that a rock can roll back to
                            # print('rocks can roll back to',index+1)
                            for i in range(furthest_roll_point,index+1):      # fill the spaces between the rolled rock and current position with spaces
                                new_row[i]='.'
                        else:
                            new_row[index]='O'
                            furthest_roll_point=index+1       # this is the new furthest point that a rock can roll back to
                            # print('rocks can roll back to',index+1)
            tilted_to_west.append(new_row)
        self.rock_columns=self.rows_to_cols(tilted_to_west)
        return tilted_to_west

    def tilt_south(self):
        # tilt each column south
        tilted_to_south=[]
        for col in self.rock_columns:   # process one column of rocks at a time
            # print('tilting column',col)
            new_col={}                       # create a dictionary to contain the new rock positions
            furthest_roll_point=self.num_rows-1   # track the furthest point a rock can roll forward to
                                                  # this will either be the last row (num_rows-1), or the position before the last rock found in the column
            for index in range(self.num_rows-1,-1,-1):  # this time, start at the end of the column and work backwards
                rock=col[index]
                # print('processing position',index,'(',rock,')')
                if rock=='#':           # this is a square rock. It doesn't move
                    new_col[index]='#'
                    furthest_roll_point=index-1       # future rocks can now only roll forward as far as the position before the current rock
                    # print('rocks can roll forward to',index+1)
                elif rock=='.':         # there is no rock here. There may be a round rock that will roll here. Let's wait and see
                    new_col[index]='.'
                elif rock=='O':         # this is a round rock. It might roll if there's space ahead it, and if it's not already in the last row.
                    if index==self.num_rows-1:        # The rock's in the last row so it can't roll
                        new_col[index]='O'
                        furthest_roll_point=index-1       # this is the new furthest point that a rock can roll forward to
                        # print('rocks can roll forward to',index+1)
                    else:           # if furthest_roll_point is after the current position, roll the rock forwards
                        if furthest_roll_point>index:
                            new_col[furthest_roll_point]='O'
                            furthest_roll_point-=1       # this is the new furthest point that a rock can roll forward to
                            # print('rocks can roll forward to',furthest_roll_point)
                            for i in range(index,furthest_roll_point+1):      # fill the spaces between the current position and the rolled rock with spaces
                                new_col[i]='.'
                        else:
                            new_col[index]='O'
                            furthest_roll_point=index-1       # this is the new furthest point that a rock can roll back to
                            # print('rocks can roll forward to',furthest_roll_point)
            tilted_to_south.append(new_col)
        self.rock_columns=tilted_to_south
        return tilted_to_south

    def tilt_east(self):
        # tilt each row east
        tilted_to_east=[]
        for row_id in range(0,self.num_rows):
            row_to_tilt=self.get_row(row_id)
            # print('tilting row',row_to_tilt)
            new_row={}                  # create a dictionary to contain the new rock positions
            furthest_roll_point=0       # track the furthest point a rock can roll forward to
                                        # this will either be the last col (num_cols-1), or the position of the last rock found in the row
            for index in range(self.num_cols-1,-1,-1):
                rock=row_to_tilt[index]
                # print('processing position',index,'(',rock,')')
                if rock=='#':           # this is a square rock. It doesn't move
                    new_row[index]='#'
                    furthest_roll_point=index-1       # future rocks can now only roll back as far as the next position after the current rock
                    # print('rocks can roll back to',furthest_roll_point)
                elif rock=='.':         # there is no rock here. There may be a round rock ahead that will roll here. Let's wait and see
                    new_row[index]='.'
                elif rock=='O':         # this is a round rock. It might roll if there's space ahead of it, and if it's not already in the last row.
                    if index==self.num_cols-1:        # The rock's in the last position so it can't roll
                        new_row[index]='O'
                        furthest_roll_point=index-1       # this is the new furthest point that a rock can roll back to
                        # print('rocks can roll forward to',furthest_roll_point)
                    else:           # if furthest_roll_point is after the current position, roll the rock forwards
                        if furthest_roll_point>index:
                            new_row[furthest_roll_point]='O'
                            furthest_roll_point-=1       # this is the new furthest point that a rock can roll forward to
                            # print('rocks can roll forward to',furthest_roll_point)
                            for i in range(index,furthest_roll_point+1):      # fill the spaces between the current position and the rolled rock with spaces
                                new_row[i]='.'
                        else:
                            new_row[index]='O'
                            furthest_roll_point=index-1       # this is the new furthest point that a rock can roll back to
                            # print('rocks can roll forward to',furthest_roll_point)
            # print('new row:',new_row)
            tilted_to_east.append(new_row)
        tilted_to_east_cols=self.rows_to_cols(tilted_to_east)
        tilted_to_east_cols.reverse()
        self.rock_columns=tilted_to_east
        # self.rock_columns.reverse()
        return tilted_to_east

    def spin_cycle(self):
        self.tilt_north()
        self.tilt_west()
        self.tilt_south()
        self.tilt_east()

    def get_total_load(self):
        # calculate total load
        total_load=0
        for row_id in range(0,self.num_rows):
            # print('calculating load for row',row_id)
            row_load_multiplier=self.num_rows - row_id      # distance from far edge
            num_rocks=0
            for col in self.rock_columns:
                if col[row_id]=='O':
                    num_rocks+=1
            row_load = num_rocks*row_load_multiplier
            # print('row:',row_id,'has',num_rocks,'rocks and multiplier',row_load_multiplier,'i.e. a load of',row_load)
            total_load+=row_load
        return total_load

inputfile = "input_test2.txt"
f = open(inputfile, "r")

total_load=0

rock_columns=[]

for row_index,line in enumerate(f):     # process each line in the input file
    # print('processing input line',row_index)
    line=line.split('\n')[0]        # remove the newline character
    for col_index,value in enumerate(line):         # process each position in the line
        if row_index==0:        # we're processing the first row
            column={row_index:value}  # create a dictionary to contain the values this column and add it to the list of rock_columns
            rock_columns.append(column)
        else:
            rock_columns[col_index][row_index]=value        # add the value to the current column
    
# now we have our grid represented by a list of columns:
#   each column is a dictionary where the column_id is the key and the rock type is the value

rock_grid=RockGrid(rock_columns)

print('Original grid:')
for column in rock_grid.rock_columns:
    print(column)

# rock_grid.tilt_north()

# print('Grid after tilt North:')
# for column in rock_grid.rock_columns:
#     print(column)

# rock_grid.tilt_west()

# print('Grid after tilt West:')
# for column in rock_grid.rock_columns:
#     print(column)

# rock_grid.tilt_south()

# print('Grid after tilt South:')
# for column in rock_grid.rock_columns:
#     print(column)

# rock_grid.tilt_east()

# print('Grid after tilt East:')
# for column in rock_grid.rock_columns:
#     print(column)

# for i in range(0,1000000000):
for i in range(0,10):
    rock_grid.spin_cycle()
    print('After spin cycle',i)
    print('Grid:')
    for column in rock_grid.rock_columns:
        print(column)
    print('Total Load:',rock_grid.get_total_load())

f.close()