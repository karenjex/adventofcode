# GOAL:

# For each game, find the minimum set of cubes that must have been present and calculate the sum of the power of these sets
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. 

# Example:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

#     In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes.
#     Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
#     Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
#     Game 4 required at least 14 red, 3 green, and 15 blue cubes.
#     Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

# The power of the minimum set of cubes in game 1 is 48. 
# In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

from GameClass import Game

inputfile = "input.txt"
# inputfile = "input_test.txt"
f = open(inputfile, "r")

running_total=0

def check_handfull(max_colours,handfull):
    is_possible=True
    if max_colours['blue']<handfull['blue']:      # handfull not possible - it contains more blues than the bag contains
        is_possible=False
    if max_colours['red']<handfull['red']:      # handfull not possible - it contains more reds than the bag contains
        is_possible=False
    if max_colours['green']<handfull['green']:      # handfull not possible - it contains more greens than the bag contains
        is_possible=False
    return is_possible

for line in f:
    game=Game(line)
    min_set={'red':0,'green':0,'blue':0}
    handfulls=game.get_handfulls()
    for handfull in handfulls:
        print(handfull)
        if handfull['red'] > min_set['red']:
            min_set['red'] = handfull['red']
        if handfull['green'] > min_set['green']:
            min_set['green'] = handfull['green']
        if handfull['blue'] > min_set['blue']:
            min_set['blue'] = handfull['blue']
    set_power = min_set['red'] * min_set['blue'] * min_set['green']
    print('set_power:',set_power)
    running_total+=set_power
    # print(line)

f.close()

print("Sum of possible game IDs:",running_total)