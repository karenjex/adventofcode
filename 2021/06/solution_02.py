# Goal: Find number of lanternfish after 256 days

# ** NEEDS SOME (LOTS OF) OPTIMISATION FOR 256 DAYS ! **
#     Find pattern of increase in size instead of looping through entire population each day?

inputfile = "input_test_2.txt"
fish_list=[]                    # track internal timer of each fish

with open(inputfile) as f:
    for line in f:
        for word in line.strip().split(","):
            fish_list.append(word)

# print("fish list at day 0:",fish_list)

popsizes=[len(fish_list)]

for day in range(80):
    # print("day",day+1)
    for fish_idx, fish in enumerate(fish_list):
        new_age=int(fish)-1
        fish_list[fish_idx]=new_age
        if new_age==-1:
            fish_list[fish_idx]=6
            fish_list.append(9)
    popsizes.append(len(fish_list))

for popsize in popsizes:
    print(popsize)

# fish_count=len(fish_list)
# print("Number of lanternfish:",fish_count)
