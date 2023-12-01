# Improved version of solution

inputfile = "input.txt"
f = open(inputfile, "r")

elf_calories=[]  # list of total calories carried per elf

calorie_total=0  # keep track of calories carried by current elf
for line in f:
    if line == '\n':  # if blank line, add calorie_total to the elf_calories list and reset calorie_total for the next elf
        elf_calories.append(calorie_total)
        calorie_total=0
    else:    # add the (integer) value in the current line to the current elf's calorie total
        calories=int(line)
        calorie_total+=calories

f.close()

highest_calories=max(elf_calories)    # get the highest value from the elf_calories list

print("The elf carrying the most calories is carrying a total of ",highest_calories," calories")