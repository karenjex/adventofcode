inputfile = "input.txt"
f = open(inputfile, "r")

# GOAL: 

# Calculate total winnings for the set of hands
# The winnings for a hand are its rank multiplied by its bid

# A hand consists of five cards labeled one of 
#   A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2            (A highest, 2 lowest)

# Every hand is exactly one type. From strongest to weakest, they are:

#     Five of a kind, where all five cards have the same label: AAAAA
#     Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#     Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
#     Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
#     Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
#     One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
#     High card, where all cards' labels are distinct: 23456

# Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

# If two hands have the same type, a second ordering rule takes effect. 
# Start by comparing the first card in each hand. 
# If these cards are different, the hand with the stronger first card is considered stronger. 
# If the first card in each hand have the same label, however, then move on to considering the second card in each hand. 
# If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

# So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

# The input is a list of hands and their corresponding bid:

# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483

# Each hand wins an amount equal to its bid multiplied by its rank, 
# where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. 
# Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

# So, the first step is to put the hands in order of strength:

#     32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
#     KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
#     T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.

# The total winnings of this set of hands is calculated by adding the result of multiplying each hand's bid by its rank 
#   765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5 = 6440

set_of_hands=[]

def convert_card_val(card_val):
    if card_val=='A':
        new_val='14'
    elif card_val=='K':
        new_val='13'
    elif card_val=='Q':
        new_val='12'
    elif card_val=='J':
        new_val='11'
    elif card_val=='T':
        new_val='10'
    else: 
        new_val=''.join(['0',card_val])
    return new_val

def get_hand_type(cards):
    # determine hand type based on list of cards
    # 6 : Five of a kind
    # 5 : Four of a kind
    # 4 : Full house
    # 3 : Three of a kind
    # 2 : Two pair
    # 1 : One pair
    # 0 : High card
    card_groups=[]
    cards_found=''
    max_group_len=0
    for card in cards:
        card_found=cards_found.find(card)
        if card_found==-1:
            cards_found=''.join([cards_found,card])
            num_occurences=cards.count(card)
            if num_occurences>max_group_len:
                max_group_len=num_occurences
            card_groups.append((card,num_occurences))
    num_pairs=0
    for group in card_groups:
        if group[1]==2:
            num_pairs+=1
    if max_group_len==5:
        # print('Five of a kind')
        hand_type='6'
    elif max_group_len==4:
        # print('Four of a kind')
        hand_type='5'
    elif max_group_len==3:
        if num_pairs==1:
            # print('Full house')
            hand_type='4'
        else:
            # print('Three of a kind')
            hand_type='3'
    elif max_group_len==2:
        if num_pairs==2:
            # print('Two Pair')
            hand_type='2'
        else:
            # print('One pair')
            hand_type='1'
    else:
        # print('High card')
        hand_type='0'
    return hand_type

for line in f:
    cards=line.split(' ')[0]
    bid=int(line.split(' ')[1])
    hand_type=get_hand_type(cards)
    # combine the hand_type and cards to get a combined value that can be used for ranking:
    combined_val=hand_type
    for c in cards:
        c1=convert_card_val(c)      # convert card val to 2-digit nunber
        combined_val=''.join([combined_val,c1]) 
    hand={'cards':cards,'bid':bid,'hand_type':hand_type, 'combined_val': int(combined_val)}
    set_of_hands.append(hand)

winnings=0

sorted_hands = sorted(set_of_hands, key=lambda x:x['combined_val'])

for index, hand in enumerate(sorted_hands):
    bid=hand['bid']
    hand_rank=index+1
    print('bid:',bid,'rank:',hand_rank, 'combined_val:', combined_val)
    hand_winnings=hand_rank*bid
    winnings+=hand_winnings

f.close()

print('winnings:',winnings)