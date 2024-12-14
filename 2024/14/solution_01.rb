# GOAL: 

# Predict the motion of the robots in a 101 wide x 103 tall space.
# Calculate the safety factor after exactly 100 seconds.

# Safety factor: count num robots in each quadrant (ignore if exactly in the middle) and multiply together.

# In example: 1 * 3 * 4 * 1 = 12

# EXAMPLE: robots' current positions (p) and velocities (v), one robot per line:
#          in a space which 11 tiles wide and 7 tiles tall

# p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3

# robot position: p=x,y where x is num tiles from left wall, y is num tiles from top wall
# p=0,0 means robot is in top-left corner.

# robot velocity: v=x,y where x and y are in tiles per second. 
# Positive x: moving to the right, Positive y: moving down. 

# When a robot would run into an edge of the space, they wrap around to the other side

class Bathroom_map

  attr_reader :safety_factor

  def initialize(input, grid_width, grid_height, elapsed_seconds)
    @robots=self.get_robots(input)
    @grid_width=grid_width.to_i
    @grid_height=grid_height.to_i
    @new_robot_positions=self.move_robots(elapsed_seconds)
    @safety_factor=self.get_safety_factor
  end

  def get_robots(input)
    robots=[]  # create array to store robots. For each robot, store position and velocity
    File.foreach(input) do
      |line|
      pos=line.split(" v=")[0].split("p=")[1]    # position is to the left of " v=" and to right of "p="
      x_pos=pos.split(",")[0]
      y_pos=pos.split(",")[1]
      # puts "position= "+pos
      vel=line.split(" v=")[1]    # velocity is to the right of " v="
      x_vel=vel.split(",")[0]
      y_vel=vel.split(",")[1]
      # puts "velocity= "+vel
      robots.append([[x_pos,y_pos],[x_vel,y_vel]])
    end
    return robots
  end

  def move_robots(elapsed_seconds)
    robot_positions=[]
    for robot, robot_id in @robots.map.with_index
      start_x = robot[0][0] # first part of robot position
      start_y = robot[0][1] # second part of robot position
      vel_x = robot[1][0] # first part of robot velocity
      vel_y = robot[1][1] # second part of robot velocity
      puts "start position ="+start_x+","+start_y 
      puts "velocity ="+vel_x+","+vel_y 
      # find position of robot after x second. Use %grid_width for x movement and %grid_height for y movement
      final_x = (start_x.to_i + (elapsed_seconds * vel_x.to_i))%@grid_width
      final_y = (start_y.to_i + (elapsed_seconds * vel_y.to_i))%@grid_height
      puts "final position: ("+final_x.to_s+","+final_y.to_s+")"
      robot_positions.append([final_x,final_y])  # actually want to calculate the number of robots in this position, but just adding the position for now will be fine.
    end
    puts robot_positions
    return robot_positions
  end

  def get_safety_factor
    # find number of robots in each quadrant and multiply together to get safety_factor
    q1_robots = 0
    q2_robots = 0
    q3_robots = 0
    q4_robots = 0
    for robot_position in @new_robot_positions      
      if (robot_position[0] < @grid_width/2) and (robot_position[1] < @grid_height/2)
        # quadrant_1: top left
        q1_robots+=1
      elsif  (robot_position[0] > @grid_width/2) and (robot_position[1] < @grid_height/2)
        # quadrant_2: top right
        q2_robots+=1
      elsif  (robot_position[0] < @grid_width/2) and (robot_position[1] > @grid_height/2)
        # quadrant_3: bottom left 
        q3_robots+=1      
      elsif (robot_position[0] > @grid_width/2) and (robot_position[1] > @grid_height/2)
        # quadrant_4: bottom right
        q4_robots+=1      
      end
    end  
    puts "safety factor = "+q1_robots.to_s+" * "+q2_robots.to_s+" * "+q3_robots.to_s+" * "+q4_robots.to_s
    safety_factor = q1_robots * q2_robots * q3_robots * q4_robots
    puts safety_factor
  end

end

# bathroom_map=Bathroom_map.new("input_test.txt", 11, 7, 100)
bathroom_map=Bathroom_map.new("input.txt", 101, 103, 100)
puts bathroom_map.safety_factor