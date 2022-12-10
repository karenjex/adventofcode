# Goal: considering horizontal, vertical and diagonal lines, find number of points with at least 2 overlapping lines

inputfile = "input.txt"

points_in_line=[]
points_covered=[]           # list of points covered and number of times the point is covered
                            # point_covered=((x,y),n) where x = x-coord, y = y-coord, n = num times covered

with open(inputfile) as f:
    for line in f:
        #print("Processing line",line)
        words=line.strip().split()
        start=words[0]
        start_coords=start.split(",")
        x1=int(start_coords[0])
        y1=int(start_coords[1])
        stop=words[2]
        stop_coords=stop.split(",")
        x2=int(stop_coords[0])
        y2=int(stop_coords[1])
        points_in_line=[]
        if x1==x2:       # this is a vertical line
            # print("vertical line")
            if y1<y2:
                for i in range(y1,y2+1):
                    points_in_line.append((x1,i))
            elif y1>y2:
                for i in range(y2,y1+1):
                    points_in_line.append((x1,i))
            else: # line is a point
                points_in_line.append((x1,y1))
        elif y1==y2:      # this is a horizontal line
            # print("horizontal line")
            if x1<x2:
                for j in range(x1,x2+1):
                    points_in_line.append((j,y1))
            elif x1>x2:
                for j in range(x2,x1+1):
                    points_in_line.append((j,y1))
        else:             # this is a diagonal line
            if x1<x2 and y1<y2:
                for k in range(x2+1-x1):
                    points_in_line.append((x1+k,y1+k))
            elif x1<x2 and y1>y2:
                for k in range(x2+1-x1):
                    points_in_line.append((x1+k,y1-k))
            elif x1>x2 and y1>y2:
                for k in range(x1+1-x2):
                    points_in_line.append((x2+k,y2+k))
            elif x1>x2 and y1<y2:
                for k in range(x1+1-x2):
                    points_in_line.append((x2+k,y2-k))

        for point in points_in_line:                         # check each point and add to points_covered
            already_listed=False                             # assume we haven't yet recorded this point
            for e_idx, (entry) in enumerate(points_covered):                     # check the points listed so far
                entry_coords=entry[0]
                num_times=entry[1]
                if entry_coords==point:                             # we've already recorded this point
                    # print("we've already listed",entry_coords,"x",num_times,"times")
                    already_listed=True
                    point_covered=[point,num_times+1]
                    points_covered[e_idx]=point_covered
            if not(already_listed):                          # we haven't yet listed this point
                point_covered=[point,1]
                points_covered.append(point_covered)         # add to list of points covered
                # print("point",point,"added to list of points covered")

score=0
for point_covered in points_covered:
    # print("point",point_covered[0],"has",point_covered[1],"overlapping lines")
    if point_covered[1]>=2:
        score+=1

print("Score:",score)