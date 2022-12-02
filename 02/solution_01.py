# A = X = Rock = 1 shapee point
# B = Y = Paper = 2 shape points
# C = Z = Scissors = 3 shape points

# Win chart (WIN = 6 points, DRAW = 3 points, LOSE = 0 points)
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

#   | X Y Z
#   | 1 2 3
# ------------
# A | D W L
# B | L D W
# C | W L D

total_score = 0
inputfile = "input.txt"

with open(inputfile) as f:
    for line in f:
        opponent_shape = line.split()[0] 
        your_shape = line.split()[1] 
        if your_shape == 'X':
            shape_score = 1
            if opponent_shape == 'A':
                win_score=3
            elif opponent_shape == 'B':
                win_score=0
            elif opponent_shape == 'C':
                win_score=6
        elif your_shape == 'Y':
            shape_score = 2
            if opponent_shape == 'A':
                win_score=6
            elif opponent_shape == 'B':
                win_score=3
            elif opponent_shape == 'C':
                win_score=0
        elif your_shape == 'Z':
            shape_score = 3
            if opponent_shape == 'A':
                win_score=0
            elif opponent_shape == 'B':
                win_score=6
            elif opponent_shape == 'C':
                win_score=3
       
        round_score = shape_score + win_score
        total_score += round_score

print("Your total score is ",total_score)