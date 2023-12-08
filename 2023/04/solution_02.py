# GOAL:

# Calculate the total number of scratchcards you end up with, including the originals

# scratchcards cause you to win copies of the scratchcards below the winning card, equal to the number of winning numbers you have.
# Cards will never make you copy a card past the end of the table

# Example:

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

#     Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
#     Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
#     Your copy of card 2 also wins one copy each of cards 3 and 4.
#     Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
#     Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
#     Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
#     Your one instance of card 6 (one original) has no matching numbers and wins no more cards.

# Once all of the originals and copies have been processed, you end up with:
#   1 instance of card 1
#   2 instances of card 2
#   4 instances of card 3
#   8 instances of card 4
#   14 instances of card 5
#   1 instance of card 6

#   Total: 30 scratchcards

num_scratchcards=0

inputfile = "input_test.txt"
f = open(inputfile, "r")

cards=[]        # set of cards - card ID, number of copies, winning_numbers, your_numbers for each card

# example for card 1:
# card={'card_id':1,'copies':1,'winning_numbers':[41,48,83,86,17],'your_numbers':[83,86,6,31,17,9,48,53]}

# Process input to generate list of cards

for line in f:
    card_id=line.split(':')[0].split('Card ')[1]
    numbers=line.split(':')[1]
    winning_numbers=numbers.split('|')[0].split(' ')
    your_numbers=numbers.split('|')[1].split(' ')
    card={'card_id':card_id,'copies':1,'winning_numbers':winning_numbers,'your_numbers':your_numbers}
    cards.append(card)

f.close()


for index, card in enumerate(cards):
    winning_tally=0                     # track count of winning numbers for this card 
    num_copies=card['copies']
    for winning_number in card['winning_numbers']:
        if winning_number!='':
            # print('  checking winning_number',winning_number)
            for your_number in card['your_numbers']:
                if your_number!='':
                    # print('    checking your_number',your_number)
                    if int(winning_number)==int(your_number):
                        # print('  ',your_number,'is a winner!')
                        # increment the winning_tally
                        winning_tally+=1
                        # increment 'copies' of appropriate card (if this is the nth winning number, the card n places below)
                        new_copies=cards[index+winning_tally]['copies']+num_copies
                        cards[index+winning_tally]['copies']=new_copies
    # print('  card value:',winning_tally)

for card in cards:
    num_scratchcards+=card['copies']

print(num_scratchcards)