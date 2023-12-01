# Goal: Calculate number of units of sand that come to rest before sand starts flowing into the abyss below

# Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, 
# where x represents distance to the right and y represents distance down. 
# Each path appears as a single line of text in your scan. 
# After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. 

# For example:

# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9

# This scan means that there are two paths of rock; 
# the first path consists of two straight lines, 
# and the second path consists of three straight lines. 

# The sand is pouring into the cave from point 500,0.

# Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. 
# A unit of sand is large enough to fill one tile of air in your scan.

# A unit of sand always falls down one step if possible. 
# If the tile immediately below is blocked (by rock or sand), 
# the unit of sand attempts to instead move diagonally one step down and to the left. 
# If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. 

# Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. 
# If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, 
# at which point the next unit of sand is created back at the source.

inputfile = "input_test.txt"    # expected result = 24
# inputfile = "input.txt"

# process input file



paths=[]
with open(inputfile) as f:
    for line in f:
        endpoints=[]
        for p in line.strip().split(' -> '):
            coords=p.split(',')
            endpoint=(int(coords[0]),int(coords[1]))
            endpoints.append(endpoint)
        paths.append(endpoints)

# Grid: set of lines
# Line: set of points of rock
rocks=[]

for path in paths:
    # find the rocks between the start and end of each path segment
    # don't want to add any that already exist. Want to store in order to make checking easier later
    for i in range(len(path)-1):
        start_x = path[i][0]
        start_y = path[i][1]
        end_x = path[i+1][0]
        end_y = path[i+1][1]
        if start_x > end_x:
            # horizontal line
            for i in range(end_x,start_x+1):
                rocks.append((i,start_y))
        elif end_x > start_x:
            # horizontal line
            for i in range(start_x,end_x+1):
                rocks.append((i,start_y))
        if start_y > end_y:
            # vertical line
            for i in range(end_y,start_y+1):
                rocks.append((start_x,i))
        elif end_y > start_y:
            # vertical line
            for i in range(start_y,end_y+1):
                rocks.append((start_x,i))
        else:
            # point
            rocks.append((start_x,i))
        print('plotting path from (',start_x,',',start_y,') to (',end_x,',',end_y,')')


print(rocks)

