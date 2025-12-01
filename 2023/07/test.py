
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


card_groups={'K':1, 'T':2, 'J':2}

print(card_groups)

for group in card_groups:
    print(group)
