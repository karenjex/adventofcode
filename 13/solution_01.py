# Goal: Find the sum of the indices of the pairs of packets that are already in the right order (first pair has index 1, second has index 2 etc)

# Input consists of pairs of packets; pairs are separated by a blank line. 
# Packet data consists of lists and integers. Each list starts with [, ends with ], and contains zero or more comma-separated values

# When comparing two values, the first value is called left and the second value is called right. Then:

#     If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
#     If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
#     If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].

# Using these rules, you can determine which of the pairs in the example are in the right order:

# What are the indices of the pairs that are already in the right order? (The first pair has index 1, the second pair has index 2, and so on.) In the above example, the pairs in the right order are 1, 2, 4, and 6; the sum of these indices is 13.

import json

inputfile="input_test_1.txt"

with open(inputfile) as f:
    pair=[]
    pairs=[]
    for line in f:
        if line=='\n':
            pairs.append(pair)
            pair=[]
        else:
            str=line.strip()
            json_str=json.loads(str)
            pair.append(json_str)
    pairs.append(pair)

# def check(left,right,finished_checking):
#     print("finished_checking:",finished_checking)
#     print("checking left:",left, "against right:",right)
#     print("left is type:",type(left),"right is type:",type(right))
#     if not(finished_checking):
#         if type(left)!=list and type(right)!=list:          # if neither is a list, compare left and right values
#             print("both left and right are integers")
#             left=int(left)
#             right=int(right)
#             if left<right:                                # if left is less than right - pair is in correct order - stop checking
#                 print("left < right")
#                 finished_checking=True
#                 return True
#             elif left>right:                              # left is more than right - pair is *NOT* in correct order - stop checking
#                 print("left > right")
#                 finished_checking=True
#                 return False
#             else:
#                 print("left == right")
#         else:
#             if type(left)==int:
#                     left=[left]
#             elif type(right)==int:
#                     right=[right]
#             for i in range(max(len(left),len(right))):
#                 if not(finished_checking):
#                     left_val=left[i] if len(left) > i else 'null'
#                     right_val=right[i] if len(right) > i else 'null'
#                     if left_val=='null':
#                         finished_checking=True
#                         return True
#                     elif right_val=='null':
#                         finished_checking=True
#                         return False
#                     else:
#                         print("Now check",left_val,"against",right_val)
#                         check(left_val,right_val,finished_checking)
#     return finished_checking

def check(left,right,finished):
    print("Starting check of",left,"against",right,"with finished",finished)
    if not finished:
#        is_correct=False    # assume not in correct order unless found otherwise
        print("checking left:",left, "against right:",right)
        if type(left)!=list and type(right)!=list:          # if neither is a list, compare left and right values
                print("both left and right are integers")
                left=int(left)
                right=int(right)
                if left<right:                                # if left is less than right - pair is in correct order - stop checking
                    print("left < right")
                    finished=True
                    is_correct=True
                elif left>right:                              # left is more than right - pair is *NOT* in correct order - stop checking
                    print("left > right")
                    finished=True
                    is_correct=False
                if finished:
                    return is_correct
        else:                             # one or both is a list - if one is an int, convert it to a list
                if type(left)!=list:
                    left=[left]
                    print("converted left to list")
                elif type(right)!=list:
                    print("converted right to list")
                    right=[right]
                for i in range(max(len(left),len(right))):
                        left_val=left[i] if len(left) > i else 'null'
                        right_val=right[i] if len(right) > i else 'null'
                        if left_val=='null':
                            print("no more entries in left")
                            finished=True
                            is_correct=True
                        elif right_val=='null':
                            print("no more entries in right")
                            finished=True
                            is_correct=False
                        if finished:
                            return is_correct
                        else:
                            print("Now check",left_val,"against",right_val,"with finished",finished)
                            check(left_val,right_val,finished)
        if finished: return is_correct

correct_order_index_sum=0

for pair_idx, pair in enumerate(pairs):                   # check each pair
    left=pair[0]
    right=pair[1]
    print("Checking pair",pair_idx+1)
    if check(left,right,False):
        print("pair",pair_idx+1,"is in the correct order")
        correct_order_index_sum+=pair_idx+1
    else:
        print("pair",pair_idx+1,"is NOT in the correct order")

print("Sum of indices of pairs that are in the correct order:",correct_order_index_sum)    




