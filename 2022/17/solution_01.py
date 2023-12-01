# Goal: Find how many units tall the tower of rocks will be after 2022 rocks have stopped falling
# (but before the 2023rd rock begins falling)
# 
# . In this example, the tower of rocks will be

inputfile = "input_test.txt"    # expected result 3068 units tall.
# inputfile = "input.txt"
tower_height=0

with open(inputfile) as f:
    for char in f:
        
