# Goal: Find the highest scenic score possible for any tree

# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; 
# stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. 
# (If a tree is right on the edge, at least one of its viewing distances will be zero.)
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. 

# scenic score = viewing_distance_t * viewing_distance_b * viewing_distance_l * viewing_distance_r


inputfile = "input.txt"
max_scenic_score=0
map=[]
row=[]

with open(inputfile) as f:
    for line in f:
        for char in line.strip():
            row.append(char)
        map.append(row)
        row=[]

for row_idx, row in enumerate(map):
    current_row_num=row_idx
    row_length=len(row)
    if current_row_num!=0 and current_row_num!=len(map)-1:           # ignore top and bottom row - will have viewing_distance=0
        for tree_idx, tree in enumerate(row):
            current_tree_height=tree
            current_tree_position=tree_idx
            if current_tree_position!=0 and current_tree_position!=row_length-1:   # ignore trees at beginning or end of row - will have viewing_distance=0
                viewing_distance_t=0
                viewing_distance_b=0
                viewing_distance_l=0
                viewing_distance_r=0
                # print("Checking tree in position",tree_idx,"of row",row_idx,"which is",tree,"high")
                # check trees above current tree
                # print("    Checking trees above (from",current_row_num-1,"to -1)")
                keep_checking=True
                for i in range(current_row_num-1,-1,-1):
                    if keep_checking:
                        viewing_distance_t+=1
                        other_tree_height=map[i][current_tree_position]
                        if other_tree_height>=current_tree_height:
                            keep_checking=False
                # print("      viewing distance above",viewing_distance_t)
                # check trees below current tree
                # print("    Checking trees below (from",current_row_num+1,"to ",len(map),")")
                keep_checking=True
                for i in range(current_row_num+1,len(map)):
                    if keep_checking:
                        viewing_distance_b+=1
                        other_tree_height=map[i][current_tree_position]
                        if other_tree_height>=current_tree_height:
                            keep_checking=False
                # print("      viewing distance below",viewing_distance_b)
                # check trees to the left of current tree
                # print("    Checking trees to left (from",current_tree_position-1,"to -1)")
                keep_checking=True
                for j in range(current_tree_position-1,-1,-1):
                    if keep_checking:
                        viewing_distance_l+=1
                        other_tree_height=map[current_row_num][j]
                        if other_tree_height>=current_tree_height:
                            keep_checking=False
                # print("      viewing distance to left",viewing_distance_l)
                # check trees to the right of current tree
                # print("    Checking trees to right (from",current_tree_position+1,"to ",row_length,")")
                keep_checking=True
                for j in range(current_tree_position+1,row_length):
                    if keep_checking:
                        viewing_distance_r+=1
                        other_tree_height=map[current_row_num][j]
                        if other_tree_height>=current_tree_height:
                            keep_checking=False
                # print("      viewing distance to right",viewing_distance_r)
                scenic_score=viewing_distance_l*viewing_distance_r*viewing_distance_t*viewing_distance_b
                # print("max scenic score",max_scenic_score)
                # print("scenic score",scenic_score)
                if scenic_score>max_scenic_score:
                    max_scenic_score=scenic_score

print("Highest scenic score:",max_scenic_score)
