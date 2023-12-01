# Goal: Find the item type that appears in both compartments of each rucksack and return the sum of the priorities of those item types
#       1st compartment: 1st half of list
#       2nd compartment: 2nd half of list

priority_sum=0
inputfile = "input.txt"

def priority_val(item_type):
    # use ord(item_type) to return numeric value of letter and convert to priority score
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    if ord(item_type) >= 97:
        item_priority_val=(ord(item_type)-96)
    else:
        item_priority_val=(ord(item_type)-38)
    return item_priority_val

with open(inputfile) as f:
    for line in f:
        # split line in half
        compartment1=slice(0,len(line)//2)
        compartment2=slice(len(line)//2,len(line))
        c1_contents=line[compartment1]
        c2_contents=line[compartment2]
        # compare the two lines and find the common item
        for i in c1_contents:
            if i in c2_contents:
                common_item_type=i
                common_item_priority=priority_val(common_item_type)
                priority_sum+=common_item_priority

print("Your priority sum is ",priority_sum)