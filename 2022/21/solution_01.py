# Goal: work out the number the monkey named root will yell

# Each monkey either yells a specific number or yells the result of a math operation. 

# Each line contains the name of a monkey, a colon, and then the job of that monkey:

#     A lone number means the monkey's job is simply to yell that number.
#     aaaa + bbbb : yell the sum of the numers yelled by monkeys aaaa and bbbb
#     aaaa - bbbb : yell aaaa's number minus bbbb's number.
#     aaaa * bbbb : yell aaaa's number multiplied by bbbb's number.
#     aaaa / bbbb will yell aaaa's number divided by bbbb's number.

# So, in the above example, monkey drzm has to wait for monkeys hmdt and zczc to yell their numbers. Fortunately, both hmdt and zczc have jobs that involve simply yelling a single number, so they do this immediately: 32 and 2. Monkey drzm can then yell its number by finding 32 minus 2: 30.

# Then, monkey sjmn has one of its numbers (30, from monkey drzm), and already has its other number, 5, from dbpl. This allows it to yell its own number by finding 30 multiplied by 5: 150.

# This process continues until root yells a number: 152.

# inputfile = "input_test.txt"    # expected result: 152
inputfile = "input.txt"

# monkeys=[]
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

for monkey in monkeys:
    print(monkeys[monkey])

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

yell_value = get_yell_value(monkeys['root'])

print("root's yell value:",yell_value)
