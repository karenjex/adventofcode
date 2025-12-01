# GOAL: 

# figure out how many different arrangements of operational and broken springs fit the given criteria in each row.

# For each row, the condition records show every spring and whether it is operational (.) or damaged (#). 
# for some springs, it is simply unknown (?) whether the spring is operational or damaged.

# After the list of springs for a given row, the size of each contiguous group of damaged springs is listed in the order those groups appear in the row. 
# This list always accounts for every damaged spring, and each number is the entire size of its contiguous group 
# (that is, groups are always separated by at least one operational spring: #### would always be 4, never 2,2).


# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1


# In this example, the number of possible arrangements for each row is:

#     ???.### 1,1,3 - 1 arrangement
#     .??..??...?##. 1,1,3 - 4 arrangements
#     ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
#     ????.#...#... 4,1,1 - 1 arrangement
#     ????.######..#####. 1,6,5 - 4 arrangements
#     ?###???????? 3,2,1 - 10 arrangements

# Adding all of the possible arrangement counts together produces a total of 21 arrangements.
# Should we convert # and . to "True" (for broken) and "False" (for not broken)
# Or to 1 (for broken) and 0 (for not broken)?
# If we use 0 and 1 we can just count the distinct binary values

num_arrangements=0

inputfile = "input_test.txt"
f = open(inputfile, "r")

for index, line in enumerate(f):
    springs=[]                      # list of "?","." and "# characters representing a line of springs"
    total_broken=0                  # sum of group sizes gives total number of broken springs
    known_broken=0                  # total "#" characters gives number of known broken springs (don't know if this is useful)
    unknowns=0                      # total "?" characters gives number of unknowns

    line_text=line.split('\n')[0]               # get rid of the newline character
    spring_text=line_text.split(' ')[0]         # characters found before the space represent the springs
    groups=line_text.split(' ')[1].split(',')   # characters found after the space contain comma-separated list of group sizes

    num_groups=len(groups)                      # number of distinct groups (separated by at least one working spring ".") of broken springs

    for spring in spring_text:
        if spring=='#':
            known_broken+=1                     # count up number of (known) broken springs
        elif spring=='?':
            unknowns+=1                         # count up number of (known) broken springs
        springs.append(spring)                  # add spring character to list of springs

    if known_broken==total_broken:
        num_arrangements=1                      # 
    num_springs=len(springs)

    for group in groups:
        total_broken+=int(group)                # sum the group sizes to get total number of broken springs in the list

    line_arrangements=0
    num_arrangements+=line_arrangements

    print("there are ",num_groups,"groups containing a total of",total_broken,"broken springs")

f.close()

print('Number of possible arrangements:',num_arrangements)