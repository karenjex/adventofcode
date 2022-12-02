# A = R = Rock = 1 shapee point
# B = P = Paper = 2 shape points
# C = S = Scissors = 3 shape points

# Win chart (Z = WIN = 6 points, Y = DRAW = 3 points, X = LOSE = 0 points)
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

#   | R P S
#   | 1 2 3
# ------------
# A | Y Z X
# B | X Y Z
# C | Z X Y

total_score = 0
inputfile = "input.txt"

with open(inputfile) as f:
    for line in f:
        opponent_shape = line.split()[0] 
        outcome = line.split()[1] 
        if outcome == 'X':
            win_score=0
            if opponent_shape == 'A':
                shape_score = 3
            elif opponent_shape == 'B':
                shape_score = 1
            elif opponent_shape == 'C':
                shape_score = 2
        elif outcome == 'Y':
            win_score=3
            if opponent_shape == 'A':
                shape_score = 1
            elif opponent_shape == 'B':
                shape_score = 2
            elif opponent_shape == 'C':
                shape_score = 3
        elif outcome == 'Z':
            win_score=6
            if opponent_shape == 'A':
                shape_score = 2
            elif opponent_shape == 'B':
                shape_score = 3
            elif opponent_shape == 'C':
                shape_score = 1
       
        round_score = shape_score + win_score
        total_score += round_score

print("Your total score is ",total_score)