# Goal: Calculate score of the board that will win last

inputfile = "input.txt"

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

print("input has been processed:")
print("Numbers to call:", numbers_to_call)
print("Boards")
for board in boards:
  for row in board:
      print(row)
  print()

board_count=len(boards)
print(board_count)
boards_won=[]

# call the numbers one at a time and check them off against the boards
# after each number is called, check for full rows or columns to see if there's a winning board
for called_num in numbers_to_call:
    if len(boards_won)<board_count:
        print()
        print("    Number",called_num,"has been called")
        latest_number=called_num    # record the latest number called (will be used to calculate score)
        # Check each of the boards. If called_num is in one of the boards, set value to 'x' to mark it as "called"
        for board_idx, (board) in enumerate(boards):
            # print("            Checking called number against board",board_idx)
            for (row) in board:
                for idx, (val) in enumerate(row):                 # for each value in each row of each board...
                    if val==called_num:
                        # print("                        Called number",called_num,"matches",val)
                        row[idx]='x'                              # if value matches called number, mark with 'x'
        # check each of the boards for a full row or column
        for board_idx, (board) in enumerate(boards):
            if board_idx not in boards_won:
                # print("            Checking board",board_idx," for full rows or columns")
                # first look for full columns by checking each item in the first row in turn
                for idx, element in enumerate(board[0]):        # for each element in the first row of the current board
                    if element=='x':        # we have a called number. Need to check the value in the same position in all of the other rows
                        full_col=True       # until proved otherwise
                        for row in board:   # don't actually need to check the first one - we already know that matches
                            if row[idx]!='x':     # this element hasn't been called, we don't have a full col (don't actually need to check remaining rows)
                                full_col=False
                        if full_col:              # this is a full column, ie a winning board; stop processing and calculate the score
                            print("                        Board ",board_idx," has won (full column)")
                            winning_board=boards[board_idx] 
                            boards_won.append(board_idx)
                # now look for full rows by checking the first value in each row in turn
                for row in board:
                    if board_idx not in boards_won:
                        # print("                Checking row",row)
                        if row[0]=='x':        # we have a called number. Need to check the remaining values in the row
                            full_row=True      # until proved otherwise
                            for element in row:
                                if element!='x':     # this element hasn't been called, we don't have a full row and can stop checking
                                    full_row=False
                            if full_row:              # this is a full row, ie a winning board; stop processing and calculate the score
                                print("                        Board ",board_idx," has won (full row)")
                                winning_board=boards[board_idx] 
                                boards_won.append(board_idx)

print("The boards won in the following order:",boards_won)
print("last board to win:")
print(winning_board)

#     calculate score of winning board
remaining_nums=0
for row in winning_board:
    for element in row:
        if element!='x':
            remaining_nums+=int(element)

score=int(latest_number)*remaining_nums

print("latest number called:",latest_number)
print("sum of remaining numbers:",remaining_nums)
print("Score of winning board:",score)