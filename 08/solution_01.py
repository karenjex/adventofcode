# Goal: Find number of trees that are visible from outside the grid

# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. 
# Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
# All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. 

inputfile = "input.txt"
num_visible=0
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
    if current_row_num==0 or current_row_num==len(map)-1:   # all trees in first and last row are visible
        num_visible+=len(row)
    else:                                                   # this is not first or last row - need to check trees
        for tree_idx, tree in enumerate(row):
            current_tree_height=tree
            current_tree_position=tree_idx
            if current_tree_position==0 or current_tree_position==len(row)-1:         # if tree is in first or last column, it is visible
                num_visible+=1
            else:
                # check current tree against other trees that are above, below, to left and to right of it
                is_visible_l=True    #   Assume current tree is visible from left unless a tree is found that is as tall as or taller than it
                is_visible_r=True    #   Assume current tree is visible from right unless a tree is found that is as tall as or taller than it
                is_visible_t=True    #   Assume current tree is visible from top unless a tree is found that is as tall as or taller than it
                is_visible_b=True    #   Assume current tree is visible from bottom unless a tree is found that is as tall as or taller than it
                # print("Checking tree in position",tree_idx,"of row",row_idx,"which is",tree,"high")
                for r_idx, r in enumerate(map):
                    other_row_num=r_idx
                    if other_row_num<current_row_num:
                        other_tree_height=r[tree_idx]
                        if other_tree_height>=current_tree_height:   # this tree is above and is as tall as or taller than current tree
                            # print("other tree is",other_tree_height,"which is the same as or taller than",current_tree_height,"so current tree is hidden")
                            is_visible_t=False 
                    elif other_row_num>current_row_num:
                        other_tree_height=r[tree_idx]
                        if other_tree_height>=current_tree_height: # this tree is below and is as tall as or taller than current tree
                            # print("other tree is",other_tree_height,"which is the same as or taller than",current_tree_height,"so current tree is hidden")
                            is_visible_b=False 
                    elif other_row_num==current_row_num:
                        for t_idx, t in enumerate(r):
                            other_tree_position=t_idx
                            other_tree_height=t
                            if other_tree_position<current_tree_position:
                                if other_tree_height>=current_tree_height:   # tree is to the left and is as tall as or taller than current tree
                                    # print("other tree is",other_tree_height,"which is the same as or taller than",current_tree_height,"so current tree is hidden")
                                    is_visible_l=False
                            if other_tree_position>current_tree_position:
                                if other_tree_height>=current_tree_height:   # tree is to the right and is as tall as or taller than current tree
                                    # print("other tree is",other_tree_height,"which is the same as or taller than",current_tree_height,"so current tree is hidden")
                                    is_visible_r=False
                if (is_visible_t or is_visible_b or is_visible_l or is_visible_r):
                    num_visible+=1

print("Number of visible trees:",num_visible)
