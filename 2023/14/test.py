
list = [1,2,3]

print(list)

list.reverse()
print(list)

# rows=[{3: '.', 2: '#', 1: '.', 0: '.'},
#       {3: '.', 2: '.', 1: '#', 0: 'O'},
#       {3: 'O', 2: 'O', 1: 'O', 0: '.'}]



# these rows converted to columns should look like this:

# .#..
# O#..
# .OOO

# col 1: .O.
# col 2: ##O
# col 3: ..O
# col 4: ..O

# vals={0:'.',1:'.',2:'O',3:'O'}

# for val in vals:
#     print(vals[val])

# convert a list of rows to a list of columns
# rock_columns=[]
# for y,line in enumerate(rows):        # process each row in rows
#     print('converting row',y,':',line,'into columns')
#     for x in line:   # process each position (col index) in the row
#         print('the value of this entry is',line[x])
#         if y==0:        # we're processing the first row
#             column={y:line[x]}  # create a dictionary to contain the values this column and add it to the list of rock_columns
#             rock_columns.append(column)
#         else:
#             rock_columns[x][y]=line[x]        # add the value to the current column
# print('rows_to_columns:',rock_columns)
