# GOAL:

# Calculate the sum of the IDs of the games that would have been possible if the bag had been loaded with
#   12 red cubes
#   13 green cubes
#   14 blue cubes

# Each game is listed with its ID number followed by a semicolon-separated list of subsets of cubes that were revealed from the bag

# Examples:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# Anser: 

# Games 1, 2, and 5 would have been possible so sum is 8

from GameClass import Game

inputfile = "input.txt"
# inputfile = "input_test.txt"
f = open(inputfile, "r")

max_colours={'red':12,'green':13,'blue':14}
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
    game_id=game.calculate_game_id()
    handfulls=game.get_handfulls()
    game_is_possible=True
    for handfull in handfulls:
        print(handfull)
        handfull_is_possible=check_handfull(max_colours,handfull)
        if not handfull_is_possible:
            game_is_possible=False
    if game_is_possible:
        running_total+=game_id
    # print(line)

f.close()

print("Sum of possible game IDs:",running_total)