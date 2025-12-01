# GOAL: 

# **-- TO DO: THIS IS A COPY OF DAY 15 --** #

class Warehouse

  attr_reader :total_gps_coords

  def initialize(input)
    # Initialize a Warehouse by extracting the initial position of the robot, the map and the list of moves from the input.
    # Calculate the sum of the GPS coordinates for the boxes after the robot has followed the moves.

    @map_lines, @moves=self.process_input(input)
    @robot_start_pos=self.get_start_pos
    @total_gps_coords=self.get_gps_coords      # calculate the total GPS coordinates of the boxes
  end

  def process_input(input)
    # get the map and the list of moves from the input

    map_lines=[]
    moves=""   # string to collect up the lines of moves
    get_moves=false   # we'll collect the map lines first, before collecting the robot moves
    File.foreach(input) do
      |line|        
      if line.strip.empty?       # we've reached the empty line between map and moves
        get_moves=true
      end
      if get_moves==false
        # gather the map details
        map_lines.append(line.chomp.split(""))
        puts "map line: "+line.chomp
      else
        moves+=line.chomp   # add this line of moves (minus the newline char) to the string of moves
      end
    end
    # return the lines of the map, plus the moves as an array
    return map_lines, moves.split("")
  end

  def get_start_pos
    # Find the robot's start position (the place in the map marked with "@")

    robot_start_pos=[]
    for line, line_idx in @map_lines.map.with_index
      for char, char_pos in line.map.with_index
        if char=="@"
          robot_start_pos=[char_pos,line_idx]
        end
      end
    end
    return robot_start_pos
  end 

  def new_pos(dir,start_pos)
    # for a given start position and direction character, 
    # return the coordinates of the position that we are attempting to move to

    if dir == "^" # go up
      new_pos = [start_pos[0],start_pos[1]-1]
    elsif dir == "v" # go down
      new_pos = [start_pos[0],start_pos[1]+1]
    elsif dir == "<" # go left
      new_pos = [start_pos[0]-1,start_pos[1]]
    elsif dir == ">" # go right
      new_pos = [start_pos[0]+1,start_pos[1]]
    end
    return new_pos
  end


  def move_robot
    # process each of the robot moves and update the position of the robot and the boxes (@boxes)

    robot_pos = @robot_start_pos

    puts "processing the robot's moves: "
    for move_dir in @moves

      new_pos=new_pos(move_dir,robot_pos)   # Find the position the robot is trying to move to
      robot_new_pos=new_pos
      num_boxes=0                           # keep track of how many boxes we've found (NOTE: may not need this)

      # Look ahead from current robot position in direction move_dir until we encounter a wall ("#") or a space (".")

      puts "Trying to move robot "+move_dir+" from "+robot_pos[0].to_s+","+robot_pos[1].to_s+"to "+new_pos[0].to_s+","+new_pos[1].to_s

      while @map_lines[new_pos[1]][new_pos[0]] == "O"
        new_pos=new_pos(move_dir,new_pos)
        num_boxes+=1
      end
      puts "We found "+num_boxes.to_s+" boxes."
      if @map_lines[new_pos[1]][new_pos[0]] == "."
        # We encountered a space: the robot and all of the boxes between the robot and the space can move one place in that direction.
        # Practically that just means updating the robot's position and swapping the following (no need to swap the intermediate boxes):
        #   robot "@" => space "."
        @map_lines[robot_pos[1]][robot_pos[0]] = "."
        #   first box "O" => robot
        @map_lines[robot_new_pos[1]][robot_new_pos[0]] = "@"
        robot_pos=robot_new_pos
        #   space at end "." => box "0"
        if num_boxes>0
          @map_lines[new_pos[1]][new_pos[0]]="O"
        end
      elsif @map_lines[new_pos[1]][new_pos[0]] == "#"
          # If we encounter a wall: nothing moves.
      end
    end
    return @map_lines
  end

  def get_gps_coords

    # Calculate the GPS coordinates for each box 
    # and add them together to get the total GPS coordinates (our solution).

    total_gps_coords=0
    map_lines=self.move_robot

    for line, y_coord in @map_lines.map.with_index
      for char, x_coord in line.map.with_index
        if char=="O"
          # puts "Box found at "+x_coord.to_s+","+y_coord.to_s
          # GPS coordinates: 100 * y_coord (distance from top) + x_coord (distance from left)
          total_gps_coords+=((100*y_coord)+x_coord)
        end
      end
    end
    return total_gps_coords
  end

end

# warehouse=Warehouse.new("input_test_1.txt") 
# warehouse=Warehouse.new("input_test_2.txt") 

warehouse=Warehouse.new("input.txt")    
puts "Total GPS coordinates: "+warehouse.total_gps_coords.to_s