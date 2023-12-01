# Goal: Find the sum of the three numbers that form the grove coordinates after mixing the input file exactly once. 

# The grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers after the value 0, 
# wrapping around the list as necessary. 

# elements={
#   0: {'val':1, 'pos':0},
#   1: {'val':2, 'pos':1},
#   2: {'val':-3, 'pos':2},
#   3: {'val':3, 'pos':3},
#   4: {'val':-2, 'pos':4},
#   5: {'val':0, 'pos':5},
#   6: {'val':4, 'pos':6}
#   }

# inputfile = "input_test.txt"    # expected result = 4 + -3 + 2 = 3
inputfile = "input.txt"

elements={}
i=0

with open(inputfile) as f:
    for line in f:
        elements[i]={'val':int(line.strip()),'pos':i}
        i+=1

# print(elements)
length=len(elements)
# print('there are',length,'elements')

# Mix the file:

# To mix the file, move each number forward or backward in the file a number of positions equal to the value of the number being moved. 
# The list is circular, so moving a number off one end of the list wraps back around to the other end as if the ends were connected.
# The numbers should be moved in the order they originally appear in the encrypted file.

for element in elements:
    elements_to_move={}        # collect list of elements that will move
    value=elements[element]['val']
    old_pos=elements[element]['pos']
    new_pos_1=(old_pos+value)%length
    # print("element",element,"(value",value,", position",old_pos,") moves to position",new_pos)
    if value>0:
        if old_pos<new_pos_1:
            # displace elements between position (old position) and new_pos 1 step to the left
            new_pos=new_pos_1
            elements_to_move[element]={'new_pos':new_pos}
            for i in range(old_pos+1,new_pos+1):
                e_to_move_new_pos=i-1
                element_to_move=[k for k, v in elements.items() if v['pos'] == i][0]
                if element_to_move!=element:
                    elements_to_move[element_to_move]={'new_pos':e_to_move_new_pos}
                    # print("  element",element_to_move,"displaced to position",e_to_move_new_pos)
        elif old_pos>new_pos_1:
            new_pos=new_pos_1+1
            elements_to_move[element]={'new_pos':new_pos}
            # displace elements between position (old position) and new_pos 1 step to the right
            for i in range(new_pos,old_pos):
                e_to_move_new_pos=i+1
                element_to_move=[k for k, v in elements.items() if v['pos'] == i][0]
                if element_to_move!=element:
                    elements_to_move[element_to_move]={'new_pos':e_to_move_new_pos}
                    # print("  element",element_to_move,"displaced to position",e_to_move_new_pos)
    elif value<0:
        if old_pos<(new_pos_1-1)%length:
            new_pos=(new_pos_1-1)%length
            elements_to_move[element]={'new_pos':new_pos}
            # displace elements between position (old position) and new_pos 1 step to the left
            for i in range(old_pos+1,new_pos+1):
                e_to_move_new_pos=i-1
                element_to_move=[k for k, v in elements.items() if v['pos'] == i][0]
                if element_to_move!=element:
                    elements_to_move[element_to_move]={'new_pos':e_to_move_new_pos}
                    # print("  element",element_to_move,"displaced to position",e_to_move_new_pos)
        elif old_pos>new_pos_1:
            new_pos=new_pos_1
            elements_to_move[element]={'new_pos':new_pos}
            # displace elements between position (old position) and new_pos 1 step to the right
            for i in range(new_pos,old_pos):
                e_to_move_new_pos=i+1
                element_to_move=[k for k, v in elements.items() if v['pos'] == i][0]
                if element_to_move!=element:
                    elements_to_move[element_to_move]={'new_pos':e_to_move_new_pos}
                    # print("  element",element_to_move,"displaced to position",e_to_move_new_pos)

    for element in elements_to_move:
        elements[element]['pos'] = elements_to_move[element]['new_pos']

# print('new order:')
# for i in range(length):
#     print('  ',elements[[k for k, v in elements.items() if v['pos'] == i][0]]['val'])

zero_element=[k for k, v in elements.items() if v['val'] == 0][0]
zero_position= elements[zero_element]['pos']

# print('zero is in position',zero_position)

grove_coordinates=0

# print(elements)

for i in range(3):
    position=(zero_position + 1000*(i+1))%length
    element=[k for k, v in elements.items() if v['pos'] == position][0]
    # print(i+1,"thousandth element after 0 is in position",position)
    # print("element",element,"is in position",position)
    value = elements[element]['val']
    # print('value',value,'in position',position)
    grove_coordinates+=value

print(grove_coordinates)