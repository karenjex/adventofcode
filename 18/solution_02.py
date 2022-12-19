# Goal: Find *exterior* surface area of scanned lava droplet
#       Exclude any cubes of air trapped within the lava droplet

# TO DO - HAVE NOT YET IMPLEMENTED LOGIC TO IDENTIFY CUBES OF TRAPPED AIR #

inputfile = "input_test.txt"    # expected result 58
# inputfile = "input.txt"
surface_area=0
cubes=[]

with open(inputfile) as f:
    for line in f:
      cube=(int(line.strip().split(',')[0]),int(line.strip().split(',')[1]),int(line.strip().split(',')[2]))
      cubes.append(cube)


matched_sides=[]

def check_sides(c):
  matches=0
  # print(c)
  for cube in cubes:
    # print("  cube",cube)
    if c[0]==cube[0] and c[1]==cube[1]:
      if abs(c[2]-cube[2])==1:
        matches+=1
        matched_sides.append()
    if c[0]==cube[0] and c[2]==cube[2]:
      if abs(c[1]-cube[1])==1:
        matches+=1
    if c[2]==cube[2] and c[1]==cube[1]:
      if abs(c[0]-cube[0])==1:
        matches+=1
  return matches

num_cubes=len(cubes)
total_sides=num_cubes*6

sides_covered=0

for cube in cubes:
  sides_covered+=check_sides(cube)

sides_visible=total_sides-sides_covered

print(sides_visible)