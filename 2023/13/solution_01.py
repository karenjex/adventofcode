# GOAL: 

# Find the line of reflection in each pattern
# Sum the number of columns to the left of each vertical line of reflection 
# Add to that, 100 x number of rows above each horizontal line of reflection

# ash   . 
# rock  # 

# In the test input:

# In the first pattern, the line of reflection is the vertical line between cols 5 & 6:

# 123456789
#     ><   
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
#     ><   
# 123456789

# In the second pattern, the line of reflection is the horizontal line between rows 4 & 5:

# 1 #...##..# 1
# 2 #....#..# 2
# 3 ..##..### 3
# 4v#####.##.v4
# 5^#####.##.^5
# 6 ..##..### 6
# 7 #....#..# 7

# The first pattern's vertical line has 5 columns to its left  = 5
# The second pattern's horizontal line has 4 rows above it = 400
# Total: 405

inputfile = "input.txt"
f = open(inputfile, "r")


# given pattern with r rows    (i.e. len(pattern_grid) = r)
# and                c columns (i.e. len(pattern_grid[0]) = c)

# we have a grid that looks like this:

#       0    1    2    3   ...  c-1
# 0     x    x    x    x   ...   x
# 1     x    x    x    x   ...   x
# 2     x    x    x    x   ...   x
# 3     x    x    x    x   ...   x
# ...  ...  ...  ...  ...  ...  ...
# r-1   x    x    x    x   ...   x

class Pattern:

    def __init__(self, pattern_grid):
        self.pattern_grid = pattern_grid    # instance variable unique to each instance
        self.num_rows=len(pattern_grid)
        self.num_cols=len(pattern_grid[0])

    def get_col(self, col_id):
        # return the values in the given column as a list
        col=[]
        for x in range(0,self.num_rows):
            col.append(self.pattern_grid[x][col_id])
        return col

    def get_horizontal_line(self):
        num_rows_before=0       # if we find a horizontal line of symmetry, return the number of rows before the line (else return 0)
        for n in range(0,self.num_rows-1):      # want to 
            # compare each row (except the last row) with the next row to see if they're identical
            # if we find identical rows n and n+1:
            if num_rows_before==0:           # we haven't yet found a line of symmetry (no point checking once we've found one)
                if self.pattern_grid[n]==self.pattern_grid[n+1]:
                    print ('there may be a horizontal line of symmetry between lines',n,'and',n+1)
                    horizontal_line=True      # assume this is a horizontal line of symmetry unless we find otherwise
                    max_y=min(n+1,self.num_rows - (n+1)) # need  n-y >=0 and n+1+y < num_rows (can only compare rows that exist!)
                    for y in range(0,max_y):
                        if horizontal_line:
                            if self.pattern_grid[n-y] != self.pattern_grid[n+1+y]:
                                horizontal_line=False
                    if horizontal_line:
                        print ('we found a line of symmetry with',n+1,'rows before it')
                        num_rows_before=n+1
        if num_rows_before==0:
            print('there is no horizontal line of symmetry')

        return num_rows_before


    def get_vertical_line(self):

        num_cols_before=0       # if we find a vertical line of symmetry, return the number of cols before the line (else return 0)
        for n in range(0,self.num_cols-1): 
            # compare each col (except the last col) with the next col to see if they're identical
            # if we find identical cols n and n+1:

            if num_cols_before==0:           # we haven't yet found a line of symmetry (no point checking once we've found one)
                col = self.get_col(n)        # get the values in the current and next column as a list
                next_col = self.get_col(n+1)
                if self.get_col(n) == self.get_col(n+1):
                    print ('there may be a vertical line of symmetry between columns',n,'and',n+1)
                    vertical_line=True      # assume this is a vertical line of symmetry unless we find otherwise
                    max_x=min(n+1,self.num_cols - (n+1)) # need  n-x >=0 and n+1+x < num_cols (can only compare cols that exist!)
                    for x in range(0,max_x):
                        if vertical_line:
                            if self.get_col(n-x) != self.get_col(n+1+x):
                                vertical_line=False
                    if vertical_line:
                        print ('we found a line of symmetry with',n+1,'columns before it')
                        num_cols_before=n+1
        if num_cols_before==0:
            print('there is no vertical line of symmetry')

        return num_cols_before


pattern_grid=[]
solution=0

for line in f:
    line=line.split('\n')[0]        # remove the newline character
    if line=='':
        # ths is the line between two patterns. Process the previous pattern

        print('')
        print('Processing a grid:')
        print('')
        pattern=Pattern(pattern_grid)

        rows_before=pattern.get_horizontal_line()
        solution += rows_before*100
        if rows_before==0:      # only look for vertical line if we didn't find a horizontal line
            cols_before=pattern.get_vertical_line()
            solution += cols_before

        pattern_grid=[]
        # print(line)
    else:
        row=[]
        for x in line:
            row.append(x)
        pattern_grid.append(row)

# process the final pattern

print('')
print('Processing final grid:')
print('')

pattern=Pattern(pattern_grid)

rows_before=pattern.get_horizontal_line()
solution += rows_before*100
if rows_before==0:      # only look for vertical line if we didn't find a horizontal line
    cols_before=pattern.get_vertical_line()
    solution += cols_before

f.close()


print('Solution:',solution)