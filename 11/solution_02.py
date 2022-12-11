# Goal: Calculate level of monkey business after 10000 rounds

# only difference in process is that worry level no longer divided by 3 when monkey loses interest

# NEED TO FIND EFFICIENT WAY TO CALCULATE RESULT - IDENTIFY PATTERN. WILL NOT WORK IF ATTEMPTING TO RUN THROUGH ALL 10k ROUNDS

inputfile = "input.txt"

monkeys=[]
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
            monkeys.append(monkey)
        # elif words[0] == "Monkey":      # creating entry for next monkey
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
monkeys.append(monkey)

for monkey in monkeys:
    print(monkey)

for round in range(200):
    for m_idx, (monkey) in enumerate(monkeys):
        # print("round",round,"monkey",m_idx)
        # print(monkey)
        inspected_count=monkey["items_inspected"]
        starting_items=[]
        for i in monkey["starting_items"]:
            starting_items.append(i)
        # print("    starting with items",starting_items)
        operand=monkey["operand"]
        operator=monkey["operator"]
        divisible_by=monkey["divisible_by"]
        to_if_true=monkey["to_if_true"]
        to_if_false=monkey["to_if_false"]
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
            # worry_level=worry_level//3         # worry level divided by 3 as monkey gets bored - no longer happening in part 2
            # print("    worry level changed to",worry_level)
            if worry_level%divisible_by==0:    # worry_level is divisible by divisible_by
                # print("    test is true, throw",worry_level,"to",to_if_true)
                monkeys[to_if_true]["starting_items"].append(worry_level)  # throw to to_if_true (add to end of their list)
            else:
                # print("    test is false, throw",worry_level,"to",to_if_false)
                monkeys[to_if_false]["starting_items"].append(worry_level)  # throw to to_if_false (add to end of their list)
        # update monkey with changed values
        monkeys[m_idx]["items_inspected"]=inspected_count
        monkeys[m_idx]["starting_items"]=[]


item_counts=[]

for monkey in monkeys:
    print(monkey["items_inspected"])
    item_counts.append(monkey["items_inspected"])

item_counts.sort(reverse=True)

print("level of monkey business = ",item_counts[0]*item_counts[1])