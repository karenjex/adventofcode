# Goal: Calculate score of the winning board (first board to get a complete row or column)
#           Score = last number called * sum of uncalled numbers on the boards

inputfile = "input_test.txt"


numbers_to_call=[]
board=[]               # 5x5 array
boards=[]              # list of boards

processing_boards=False

with open(inputfile) as f:
    for line in f:
        if processing_boards==False:            # first get the numbers to call
            numbers_to_call=line.strip().split(',')
            processing_boards=True
        elif line == '\n':                      # prepare to process next board
            if board!=[]:
                boards.append(board)            # add the board that has just been processed to the set of boards
                board=[]                        # reset the board ready to process the next one
        else:
            board.append(line.strip().split())  # split into list of numbers without newline/space
    boards.append(board)       # add final board to list of boards

keep_going=True

# call the numbers one at a time and check them off against the boards
# after each number is called, check for full rows or columns to see if there's a winning board
for called_num in numbers_to_call:
    if keep_going:                  # ie we haven't yet found a winner
        latest_number=called_num    # record the latest number called (will be used to calculate score)
        # Check each of the boards. If called_num is in one of the boards, set to 'x' to mark it as "called"
        for (board) in boards:
            for (row) in board:
                for idx, (val) in enumerate(row):                 # for each value in each row of each board...
                    if val==called_num:
                        row[idx]='x'                              # if value matches called number, mark with 'x'
        # check each of the boards for a full row or column
        for board in boards:
            # first look for full columns by checking each item in the first row in turn
            for idx, element in enumerate(board[0]):        # for each element in the first row of the current board
                if element=='x':        # we have a called number. Need to check the value in the same position in all of the other rows
                    full_col=True       # until proved otherwise
                    for row in board:   # don't actually need to check the first one - we already know that matches
                        if row[idx]!='x':     # this element hasn't been called, we don't have a full col (don't actually need to check remaining rows)
                            full_col=False
                    if full_col:              # this is a full column, ie a winning board; stop processing and calculate the score
                        winning_board=board
                        keep_going=False
            # now look for full rows by checking the first value in each row in turn
            for row in board:
                if row[0]=='x':        # we have a called number. Need to check the remaining values in the row
                    full_row=True      # until proved otherwise
                    for element in row:
                        if element!='x':     # this element hasn't been called, we don't have a full row and can stop checking
                            full_row=False
                    if full_row:              # this is a full row, ie a winning board; stop processing and calculate the score
                        winning_board=board
                        keep_going=False

#     calculate score of winning board
remaining_nums=0
for row in winning_board:
    for element in row:
        if element!='x':
            remaining_nums+=int(element)

score=int(latest_number)*remaining_nums

#print("latest number called:",latest_number)
#print("sum of remaining numbers:",remaining_nums)
print("Score of winning board:",score)