# Goal: Find first round where no elf moves

# inputfile = "input_test.txt"    # expected result: 20
inputfile = "input.txt"

# process input:

elves=[]
checking_order=['N','S','W','E']
#elf={position:(), proposed_position:()}

y=0
with open(inputfile) as f:
    for line in f:
        x=0
        for tile in line.strip():
            if tile=='#':
                elf={'position': (x,y), 'proposed_position': ()}
                elves.append(elf)
            x+=1    # increase x coord for next column
        y+=1        # increase y coord for next line

elf_count=len(elves)

# for elf in elves:
#     print(elf)

# define required functions:

def check_surroundings(current_position):
    # print(current_position)
    x = current_position[0]
    y = current_position[1]
    N_clear=True    # N: (x,y-1)
    NE_clear=True   # NE: (x+1,y-1)
    E_clear=True    # E: (x+1,y)
    SE_clear=True   # SE: (x+1,y+1)
    S_clear=True    # S: (x,y+1)
    SW_clear=True   # SW: (x-1,y+1)
    W_clear=True    # W: (x-1,y)
    NW_clear=True   # NW: (x-1,y-1)
    for elf in elves:
        if elf['position']==(x,y-1):
            N_clear=False
        elif elf['position']==(x+1,y-1):
            NE_clear=False
        elif elf['position']==(x+1,y):
            E_clear=False
        elif elf['position']==(x+1,y+1):
            SE_clear=False
        elif elf['position']==(x,y+1):
            S_clear=False
        elif elf['position']==(x-1,y+1):
            SW_clear=False
        elif elf['position']==(x-1,y):
            W_clear=False
        elif elf['position']==(x-1,y-1):
            NW_clear=False
    N_sector_clear=(N_clear and NE_clear and NW_clear)
    E_sector_clear=(NE_clear and E_clear and SE_clear)
    S_sector_clear=(SE_clear and S_clear and SW_clear)
    W_sector_clear=(SW_clear and W_clear and NW_clear)
    return(N_sector_clear, E_sector_clear, S_sector_clear, W_sector_clear)

# process rounds until first round where no elf moves

stop=False
i=1
while not stop:
    # print()
    # print()
    # print("round",i, 'part 1')
    elves_moved=0
    proposed_positions=[]
    # part 1 (decide where to move):
    for elf in elves:
        position=elf['position']
        # print('checking elf in position',position)
        # 1a. If all 8 surrounding positions are empty, DO NOTHING
        position_info=check_surroundings(position)
        # print(position_info)
        N_sector_clear=position_info[0]
        E_sector_clear=position_info[1]
        S_sector_clear=position_info[2]
        W_sector_clear=position_info[3]
        if not (N_sector_clear and E_sector_clear and S_sector_clear and W_sector_clear):
            # 1b. Check each sector in turn and decide where to move
            for sector in checking_order:
                # print('checking sector',sector)
                if elf['proposed_position']==():        # only check and propose a move if we haven't already proposed a move
                    if sector=='N':
                        # print('North sector clear:',N_sector_clear)
                        # check North sector and propose moving one setp North if no elf there
                        if N_sector_clear:
                            proposed_position=(position[0],position[1]-1)
                            # print('propose move N to',proposed_position)
                            elf['proposed_position']=proposed_position
                            proposed_positions.append(proposed_position)
                    elif sector=='S':
                        # print('South sector clear:',S_sector_clear)
                        # check South sector and propose moving one setp South if no elf there
                        if S_sector_clear:
                            proposed_position=(position[0],position[1]+1)
                            # print('propose move S to',proposed_position)
                            elf['proposed_position']=proposed_position
                            proposed_positions.append(proposed_position)
                    elif sector=='W':
                        # print('West sector clear:',W_sector_clear)
                        # check West sector and propose moving one setp West if no elf there
                        if W_sector_clear:
                            proposed_position=(position[0]-1,position[1])
                            # print('propose move W to',proposed_position)
                            elf['proposed_position']=proposed_position
                            proposed_positions.append(proposed_position)
                    elif sector=='E':
                        # print('East sector clear:',E_sector_clear)
                        # check East sector and propose moving one setp East if no elf there
                        if E_sector_clear:
                            proposed_position=(position[0]+1,position[1])
                            # print('propose move E to',proposed_position)
                            elf['proposed_position']=proposed_position
                            proposed_positions.append(proposed_position)

    # print('elves have proposed moves to the following tiles:')
    # print(proposed_positions)

    # part 2 (move):
    # print("round",i, 'part 2')
    for elf in elves:
        # if proposed_position is not empty and no other elves have proposed moving to the same tile:
        proposed_position=elf['proposed_position']
        # print('Elf in position',elf['position'],'has proposed moving to',elf['proposed_position'])
        if proposed_position!=():
            num_proposed=0
            for p in proposed_positions:
                if p==proposed_position:
                    num_proposed+=1
            # print(num_proposed,'elves have proposed moving to position',proposed_position)
            if num_proposed<2:
                elf['position']=proposed_position
                # print('elf moved to',elf['position'])
                elves_moved+=1
            elf['proposed_position']=()
    # change checking order - move first element to the end
    a=checking_order.pop(0)
    checking_order.append(a)
    print("number of elves moved this round:",elves_moved)
    if elves_moved==0:
        print("First round where no elf moved = ",i)
        stop=True
    i+=1
    # for elf in elves:
    #     print(elf['position'])

