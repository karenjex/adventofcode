# Goal: Find the item type that corresponds to the badges of each three-Elf group and calculate the sum of the priorities of those item types
#       The badge is the only item type carried by all 3 elves in a group. Each group can gave a different badge item type

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

elf_counter=0
priority_sum=0

with open(inputfile) as f:
    for line in f:
        if elf_counter == 0:
            found_common_element=False
            elf1_contents = line
            #print("elf",elf_counter,": ",elf1_contents)
            elf_counter+=1
        elif elf_counter == 1:
            elf2_contents = line
            #print("elf",elf_counter,": ",elf2_contents)
            elf_counter+=1
        elif elf_counter == 2:
            elf3_contents = line
            #print("elf",elf_counter,": ",elf3_contents)
            # compare the group contents lines and find the common item
            for i in elf1_contents:
                if (not(found_common_element) and (i in elf2_contents) and (i in elf3_contents)):
                    common_item_type=i
                    common_item_priority=priority_val(common_item_type)
                    found_common_element=True
                    priority_sum+=common_item_priority
            # start new group of 3 elves
            elf_counter=0

print("Priority sum:",priority_sum)