
# combine the hand_type and cards to get a combined value that can be used for ranking:

# A: '14'
# K: '13'
# Q: '12'
# J: '11'
# T: '10'
# 9: '09'
# 8: '08'
# 7: '07'
# 6: '06'
# 5: '05'
# 4: '04'
# 3: '03'
# 2: '02'

# cards: '32T3K' hand_type: 1     combined_val: 10302100313 
# cards: 'T55J5' hand_type: 3     combined_val: 31005051105
# cards: 'KK677' hand_type: 2     combined_val: 21313060707 
# cards: 'KTJJT' hand_type: 2     combined_val: 21310111110 
# cards: 'QQQJA' hand_type: 3     combined_val: 3 


# set_of_hands=[
#     {'cards': '32T3K', 'bid': 765, 'hand_type': 1}, 
#     {'cards': 'T55J5', 'bid': 684, 'hand_type': 3}, 
#     {'cards': 'KK677', 'bid': 28, 'hand_type': 2}, 
#     {'cards': 'KTJJT', 'bid': 220, 'hand_type': 2}, 
#     {'cards': 'QQQJA', 'bid': 483, 'hand_type': 3}]

# sorted_hands = sorted(set_of_hands, key=lambda x:x['hand_type'])

# current_rank=1
# for hand in sorted_hands:
#     hand_type=hand['hand_type']
#     cards=hand['cards']
#     bid=hand['bid']
#     hand_with_same_type=next(hand for hand in sorted_hands if hand['hand_type'] == hand_type)
#     print(hand_with_same_type)
#     hand_rank = current_rank
#     print('rank: ',hand_rank)
#     current_rank+=1


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

for x in '32T3K':
    print(convert_card_val(x))