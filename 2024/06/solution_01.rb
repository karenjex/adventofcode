# GOAL: 
# Find the number of distinct positions the guard will visit before leaving the mapped area.

# The map shows the current position of the guard with ^ 
# (to indicate the guard is currently facing up from the perspective of the map). 
# Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

# The guard repeatedly follows these steps:

#     If there is something directly in front of you, turn right 90 degrees.
#     Otherwise, take a step forward.

# Test input (in this example, the guard will visit 41 distinct positions on your map):

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...


class Guard

    attr_reader :pos, :dir, :num_points_visited, :out_of_bounds, :points_visited        
    # attr_writer :pos, :dir

    def initialize(guard_position, map_lines)
        @pos = guard_position
        @dir = 0   # guard is pointing upwards to start with (0 = up, 1 = right, 2 = down, 3 = left)
        @points_visited = []
        @points_visited.append(guard_position)
        @map_lines = map_lines
        @map_width = map_lines[0].length
        @out_of_bounds = false
        @num_points_visited = self.get_num_points_visited
    end

    def get_new_pos
        if @dir==0 # i.e. up
            new_pos = [pos[0]-1, pos[1]]    # subtract 1 from line number, character within line stays the same
        elsif @dir==1 # i.e. right
            new_pos = [pos[0], pos[1]+1]    # line number stays the same, add 1 to character within line
        elsif @dir==2 # i.e. down
            new_pos = [pos[0]+1, pos[1]]    # add 1 to line number, character within line stays the same
        else # @dir==3 i.e. left
            new_pos = [pos[0], pos[1]-1]    # line number stays the same, subtract 1 from character within line
        end
        # puts "new position to check: ("+new_pos[0].to_s+","+new_pos[1].to_s+")"
        return new_pos
    end

    def move
        # Check the position in front of the current position
        new_pos = self.get_new_pos()
        if new_pos[0]<0 or new_pos[0]>@map_lines.length-1 or new_pos[1]<0 or new_pos[1]>@map_width-1
            # The new position is outside the map, STOP HERE
            @out_of_bounds=true
        else
            if @map_lines[new_pos[0]][new_pos[1]] == "#"
            # There's an obstacle in front
            # Turn right 90 degrees - add 1 modulo 4 to dir
            @dir = (@dir+1)%4
            else     # There's no obstacle - move to new_pos
                @pos=new_pos
                points_visited.append(new_pos)
            end
        end
    end

    def get_num_points_visited
        while !@out_of_bounds
            self.move
        end
        # @num_points_visited = @points_visited.tally.length
        return @points_visited.tally.length
    end

end

# Process the input to get the map

map_lines=[]

# File.foreach("input_test.txt") do
File.foreach("input.txt") do
    |line|
    map_line=line.chomp
    map_lines.append(map_line)
end

# Find starting position (^)

for line, line_num in map_lines.map.with_index
    if line.include?("^")   
        start_pos=[line_num,line.index("^")]
        # puts "start position: ("+start_pos[0].to_s+","+start_pos[1].to_s+")"
    end
end

guard = Guard.new(start_pos, map_lines)
puts guard.num_points_visited
