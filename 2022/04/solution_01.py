# Goal: Find the number of assignment pairs where one range fully contain the other

# Every section has a unique ID number, and each Elf is assigned a range of section IDs.

# looking for either:
#
# assignment1_start<=assignment2_start and assignment2_end <= assignment1_end
#
# assignment1_start                                      assignment1_end
#                   assignment2_start   assignment2_end
# or:
#
# assignment2_start<=assignment1_start and assignment1_end <= assignment2_end
#
#                   assignment1_start   assignment1_end
# assignment2_start                                      assignment2_end

matched_pairs=0
inputfile = "input.txt"

with open(inputfile) as f:
    for line in f:
        assignment_text = line.strip()                        # remove newline
        assignments = assignment_text.split(",")
        a1 = assignments[0]
        a2 = assignments[1]
        a1_start=int(a1.split("-")[0])           # get the number before the "-"
        a1_end=int(a1.split("-")[1])             # get the number after the "-"
        a2_start=int(a2.split("-")[0])           # get the number before the "-"
        a2_end=int(a2.split("-")[1])             # get the number after the "-"
        if (a1_start <= a2_start and a2_end <= a1_end) or (a2_start <= a1_start and a1_end <= a2_end): 
            matched_pairs+=1

print("Number of pairs where one range contains the other:",matched_pairs)