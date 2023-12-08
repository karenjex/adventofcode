# GOAL:

# Calculate the total points for the cards
# Each card has two lists of numbers separated by a vertical bar (|): 
#   a list of winning numbers
#   a list of numbers you have

# Work out which of the numbers you have appear in the list of winning numbers. 
# The first match makes the card worth one point, and each additional match doubles the point value of that card.

# Example:

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

#     Card 1 has four winning numbers (48, 83, 17, and 86), so it is worth 8 points.
#     Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
#     Card 3 has two winning numbers (1 and 21), so it is worth 2 points.       <-- THIS IS ONLY SHOWING AS 1 POINT - WHY?
#     Card 4 has one winning number (84), so it is worth 1 point.
#     Card 5 has no winning numbers, so it is worth no points.
#     Card 6 has no winning numbers, so it is worth no points.

#   Total: 13 points

solution=0

inputfile = "input.txt"
f = open(inputfile, "r")

for line in f:
    winning_tally=0
    card_id=line.split(':')[0].split('Card ')[1]
    numbers=line.split(':')[1]
    # print('card_id:',card_id)
    winning_numbers=numbers.split('|')[0].split(' ')
    your_numbers=numbers.split('|')[1].split(' ')
    for winning_number in winning_numbers:
        if winning_number!='':
            # print('  checking winning_number',winning_number)
            for your_number in your_numbers:
                if your_number!='':
                    # print('    checking your_number',your_number)
                    if int(winning_number)==int(your_number):
                        # print('  ',your_number,'is a winner!')
                        if winning_tally==0:
                            winning_tally=1
                        else:
                            winning_tally=winning_tally*2
    # print('  card value:',winning_tally)
    solution+=winning_tally

f.close()

print(solution)