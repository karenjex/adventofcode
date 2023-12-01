# Goal: work out what number you (monkey 'humn') need to yell to pass root's equality test

    # The correct operation for monkey root should be =
    # which means that it still listens for two numbers (from the same two monkeys as before), 
    # but now checks that the two numbers match.

    # The number that appears after humn: in your input is now irrelevant.

# inputfile = "input_test.txt"    # expected result: 301
inputfile = "input.txt"

# monkeys=[]

def get_yell_value(monkey):
    yell_value=monkey['monkey_val']
    # print('calculating yell value for',monkey,'with yell value',yell_value)
    if yell_value is None:
        child1=monkey['children'][0]
        child2=monkey['children'][1]
        operation=monkey['operation']
        # print('child 1:',child1,'child 2:',child2,'operation')
        if operation=='+':
            yell_value=get_yell_value(monkeys[child1]) + get_yell_value(monkeys[child2])
        elif operation=='-':
            yell_value=get_yell_value(monkeys[child1]) - get_yell_value(monkeys[child2])
        elif operation=='*':
            yell_value=get_yell_value(monkeys[child1]) * get_yell_value(monkeys[child2])
        elif operation=='/':
            yell_value=get_yell_value(monkeys[child1]) / get_yell_value(monkeys[child2])
        monkey['monkey_val']=yell_value
    return yell_value

for i in range(500000000000000000000):

    monkeys={}

    with open(inputfile) as f:
        for line in f:
            monkey={}
            children=[]
            operation=None
            monkey_val=None
            monkey_name=line.split(':')[0]   
            instruction=line.split(':')[1].split()     
            if len(instruction)==1:
                monkey_val=int(instruction[0])
            else:       # parse instructions: 1st word is child 1, 2nd word is operation, 3rd word is child 2
                children.append(instruction[0])
                children.append(instruction[2])
                operation=instruction[1]
            # monkey={'monkey_name':monkey_name,'monkey_val':monkey_val,'children':children,'operation':operation}
            # monkeys.append(monkey)
            monkey={'monkey_val':monkey_val,'children':children,'operation':operation}
            monkeys[monkey_name] = monkey

    print('checking with yell value of',i,'for monkey humn')
    monkeys['humn']['monkey_val']=i
    root_child1=monkeys['root']['children'][0]
    root_child2=monkeys['root']['children'][1]
    
    print("root's children:",root_child1,root_child2)

    root_yell_val_1=get_yell_value(monkeys[root_child1])
    root_yell_val_2=get_yell_value(monkeys[root_child2])

    if root_yell_val_1==root_yell_val_2:
        print("humn needs to yell:",i)
        break