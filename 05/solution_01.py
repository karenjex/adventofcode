# Goal: Find the crate on the top of each stack after they are rearranged

# Sample starting positions:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# Sample moves (crates are moved one at a time):

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

# want to get the following as starting positions:
# stack 1: ['Z','N']
# stack 2: ['M','C','D']
# stack 3: ['P']
# stacks = [['Z','N'],['M','C','D'],['P']]

inputfile = "input.txt"
start_rows=[]       # the lines from the input file containing the initial positions of the crates
stack_ids=[]        # the line from the input file containing the numbers representing the numbers that identify the individual stacks
moves=[]            # the lines from the input file containing the moves

get_starting_positions=True
with open(inputfile) as f:
    for line in f:
        if line=="\n":          # we are processing the blank line that separates the crate info from the move info
            get_starting_positions=False
        elif get_starting_positions:        # we haven't yet got to the blank line
            if "[" in line:                 # the line contains crate IDs - add it to the list of start rows
                start_rows.append(line)
            else:                           
                stack_ids = line.strip().split()  # stack_ids is list of stack numbers (remove newline and split on blank space)
        else:                   # we have processed the blank line - get the move info
            moves.append(line.strip())

# Create list of stacks - one per stack ID, in preparation for proccessing the rows of crates
stacks = []
for stack in range(len(stack_ids)):
    stacks.append([])

# process start_rows to get stacks of crates:
for start_row in reversed(start_rows): # work from the bottom (ie the last entry in start_rows) to create the stacks
    crates=[start_row[i:i+4] for i in range(0, len(start_row), 4)]      # split row into 4-character chunks
    # print("Processing row",crates)
    for stack_id in stack_ids:
        crate_id=crates[int(stack_id)-1].strip()
        # print("stack ID:",stack_id,"Crate ID:",crate_id)
        if crate_id!='': # there is a crate in this stack:
            stacks[int(stack_id)-1].append(crate_id)

# print("Stacks:",stacks)

for move in moves:
    move_words=move.split()
    num_crates=int(move_words[1]) # number after "move", ie 2nd word in string
    from_stack=int(move_words[3]) # number after "from", ie 4th word in string
    to_stack=int(move_words[5]) #  number after "to", ie 6th word in string
    # print("moving:",num_crates,"from",from_stack,"to",to_stack)
    for i in range(0,num_crates):
        # move a crate from from_stack to to_stack
        crate_to_move = stacks[from_stack - 1].pop()
        # print("Crate to move: ",crate_to_move)
        stacks[to_stack - 1].append(crate_to_move)
    # print("Stacks after move:")
    # print(stacks)

top_crates=''     #string containing the IDs of the crates currently at the top of each stack
for stack in stacks:
    top_crate=stack[len(stack)-1]
    for char in top_crate:
        if char not in '[] ':
            top_crate_id=char
    top_crates+=top_crate_id

print("Top crate on each stack:",top_crates)