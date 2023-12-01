# Goal: Calculate level of monkey business after 10k rounds

# Level of monkey business: multiply the number of items inspected by each of the two most active monkeys

# Monkey attributes:

#     starting_items: (ordered) list of your worry_level for each item the monkey is currently holding
#     operation: how your worry level changes as that monkey inspects an item.
#         e.g. new = old * 5 means that your worry level after inspection is five times your worry level before inspection
#     test: how the monkey uses your worry level to decide where to throw an item next

# First, process input (get monkey attributes)

# for each line in file:
#     if 1st word is "Monkey":      # create entry for next monkey
#         2nd word is monkey id
#     elif 1st word is "Starting":
#         items after ":" are starting_items
#     elif 1st word is "Operation":
#         words 5 and 6 are operator and operand 
#     elif 1st word is "Test":
#         last (4th) word is divisible_by
#     elif 1st word is "If"
#         if 2nd word is "true":
#             last (6th) word is to_if_true monkey
#         if 2nd word is "false":
#         last (6th) word is to_if_false monkey

inputfile = "input.txt"

monkeys={}          # better to create a dictionary of monkeys
monkey_count=0

with open(inputfile) as f:
    for line in f:
        words=line.strip().split()
        if words==[]:
            monkey={"starting_items":starting_items,
                    "operator":operator,
                    "operand":operand,
                    "divisible_by":divisible_by,
                    "to_if_true":to_if_true,
                    "to_if_false":to_if_false,
                    "items_inspected":0}
            monkeys[monkey_id]=monkey
            monkey_count+=1
        elif words[0] == "Monkey":      # creating entry for next monkey
            monkey_id=monkey_count
        elif words[0] == "Starting":
            newline=line.strip().split(": ")
            items=newline[1].split(",") # everything after the colon is the list of starting items
            starting_items=[]
            for item in items:
                starting_items.append(int(item)) 
            starting_items
        elif words[0] == "Operation:":
            operator = words[4]
            operand = words[5]
        elif words[0] == "Test:":
            divisible_by = int(words[3])
        elif words[0] == "If":
            if words[1] == "true:":
                to_if_true = int(words[5])   # last (6th) word is monkey to throw to if test is true
            if words[1] == "false:":
                to_if_false = int(words[5])  # last (6th) word is monkey to throw to if test is false
monkey={"starting_items":starting_items,
        "operator":operator,
        "operand":operand,
        "divisible_by":divisible_by,
        "to_if_true":to_if_true,
        "to_if_false":to_if_false,
        "items_inspected":0}
monkeys[monkey_id]=monkey

print(monkeys)

# for 20 rounds:
#     for each monkey:

for round in range(10000):
    for monkey in monkeys:
        # print("round",round,"monkey",m_idx)
        # print(monkey)
        starting_items=monkeys[monkey]["starting_items"]
        inspected_count=monkeys[monkey]["items_inspected"]
        operand=monkeys[monkey]["operand"]
        operator=monkeys[monkey]["operator"]
        divisible_by=monkeys[monkey]["divisible_by"]
        to_if_true=monkeys[monkey]["to_if_true"]
        to_if_false=monkeys[monkey]["to_if_false"]
        # print("throw to",to_if_true,"if test is true, throw to",to_if_false,"if test is false")
        # print("operator: ",operator,"operand:",operand)
        for i, (item) in enumerate(starting_items):
            # print("inspecting item:",item)
            worry_level=item
            inspected_count+=1
            if operator=="+":
                if operand=="old":
                    worry_level+=worry_level
                else:
                    worry_level+=int(operand)
            elif operator=="*":
                if operand=="old":
                    worry_level=worry_level*worry_level
                else:
                    worry_level=worry_level*int(operand)
            # print("    worry level changed to",worry_level)
            # worry_level=worry_level//3         # worry level divided by 3 as monkey gets bored
            # print("    worry level changed to",worry_level)
            if worry_level%divisible_by==0:    # worry_level is divisible by divisible_by
                # print("    test is true, throw",worry_level,"to",to_if_true)
                monkeys[to_if_true]["starting_items"].append(worry_level)  # throw to to_if_true (add to end of their list)
            else:
                # print("    test is false, throw",worry_level,"to",to_if_false)
                monkeys[to_if_false]["starting_items"].append(worry_level)  # throw to to_if_false (add to end of their list)
        # update monkey with changed values
        monkeys[monkey]["items_inspected"]=inspected_count
        monkeys[monkey]["starting_items"]=[]


item_counts=[]

for monkey in monkeys:
    item_counts.append(monkeys[monkey]["items_inspected"])
    # print("monkey",monkey["monkey_id"],"inspected",monkey["items_inspected"])
    # print(monkey["starting_items"])

item_counts.sort(reverse=True)

print("level of monkey business = ",item_counts[0]*item_counts[1])