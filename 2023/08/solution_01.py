inputfile = "input_test.txt"
f = open(inputfile, "r")

# GOAL: 

# Calculate how many steps are required to reach ZZZ Starting at AAA, following the left/right instructions.

# Example:

    # RL

    # AAA = (BBB, CCC)
    # BBB = (DDD, EEE)
    # CCC = (ZZZ, GGG)
    # DDD = (DDD, DDD)
    # EEE = (EEE, EEE)
    # GGG = (GGG, GGG)
    # ZZZ = (ZZZ, ZZZ)

# Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. 
# In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. 
# Then, L means to choose the left element of CCC, ZZZ. 
# By following the left/right instructions, you reach ZZZ in 2 steps.

# Of course, you might not find ZZZ right away. 
# If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: 
# RL really means RLRLRLRLRLRLRLRL... and so on. 
# For example, here is a situation that takes 6 steps to reach ZZZ:

# LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)

# Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

for line in f:
    print(line)

num_steps=0

f.close()

print('Number of steps:',num_steps)