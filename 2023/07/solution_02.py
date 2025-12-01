inputfile = "input_test.txt"
f = open(inputfile, "r")

# GOAL: 

# Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.
# To balance this, J cards are now the weakest individual cards for the purpose of breaking ties.
# For example JKKK2 is weaker than QQQQ2 because J is weaker than Q.

# For example, QJJQ2 is now considered four of a kind. 

# Now, the above example goes very differently:

# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483

#     32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
#     KK677 is now the only two pair, making it the second-weakest hand.
#     T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.

# With the new joker rule, the total winnings in this example are 5905.

set_of_hands=[]

def convert_card_val(card_val):
    if card_val=='A':
        new_val='13'
    elif card_val=='K':
        new_val='12'
    elif card_val=='Q':
        new_val='11'
    elif card_val=='J':
        new_val='01'
    elif card_val=='T':
        new_val='10'
    else: 
        new_val=''.join(['0',card_val])
    return new_val

def get_hand_type(cards):
    # determine hand type based on list of cards
    # J is wildcard - can be whatever makes the hand strongest

    # 6 : Five of a kind
    # 5 : Four of a kind
    # 4 : Full house
    # 3 : Three of a kind
    # 2 : Two pair
    # 1 : One pair
    # 0 : High card

    card_groups={}      # dictionary containing each type of card found in the hand and the number of times it appears
    # cards_found=''      # keep track of which types of card have been found
    # max_group_len=0     # keep track of the type of card with the most occurences
    for card in cards: 
        try:
            card_groups[card] = card_groups[card]+1
        except:
            card_groups
            num_occurences=cards.count(card)            # find how many times it appears in the hand
            if num_occurences>max_group_len:            # if there are more occurences of this card than the previous ones
                max_group_len=num_occurences            # re-set max_group_len
                card_groups.append'card_type': card,'num_occurences':num_occurences}        # create dictionary containing type of card and number of occurences

            # card_groups.append((card,num_occurences))
    print('card groups:',card_groups)
    num_jokers=
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