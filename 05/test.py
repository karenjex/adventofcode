stacks = []
stack_ids=[1,2,3]
rows=['A','B','C']

for stack in stack_ids:
    stacks.append([])
    for row in rows:
        stacks[stack-1].append(row)

print(stacks) 
