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

total_calories=0    # calculate the total calories carried by the 3 elves with the most calories
for i in range(3):
    highest_calories=max(elf_calories)    # get the highest value from the elf_calories list
    total_calories+=highest_calories      # add it to total_calories
    elf_calories.remove(highest_calories) # remove this value from the list

print("The 3 elves carrying the most calories are carrying a total of ",total_calories," calories")