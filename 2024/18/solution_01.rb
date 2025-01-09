# GOAL: Find the minimum number of steps needed to reach the exit (70,70) from the start (0,0) after 1024 bytes fall.

# 1 byte falls every nanosecond into your memory space (grid with coords 0-70 horizontally & vertically)
# Input: positions the bytes will land in (from top left). The position is then corrupted and can't be entered.
# Example is on a 0 to 6 grid.

# Start: (0,0)
# End: (70,70) or (6,6) in test

# Using A* algorithm. 
# Code adapted from https://github.com/MatteoRagni/ruby-astar because I didn't know where to start!

########################### GRAPH CLASS ###############################

# Create connected graph to represent the paths between the different points in the graph

class Graph

    attr_reader :start, :stop  #  start (start point) and stop (exit point) are Node objects
    
    # def initialize(d)        
    def initialize(f,map_size,num_bytes)    

        @map_size = map_size
        @exit_pos = map_size-1

        corrupted_bytes=[]
        num_fallen_bytes=0

        for byte in f
            if num_fallen_bytes<num_bytes # only collect the required number of bytes
                x_coord=byte.chomp.split(",")[0].to_i       # integer to left of comma as x coordinate (char)
                y_coord=byte.chomp.split(",")[1].to_i       # integer to right of comma as y coordinate (line)
                corrupted_bytes.append([x_coord,y_coord])
                num_fallen_bytes+=1
            end
        end

        # Build the @memorymap matrix, that will be used to create the nodes
        @memorymap = Array.new(@map_size) { Array.new(@map_size) { nil } }
      
        # Create the @start and @stop nodes (start is always at 0,0 and exit is always in the bottom right corner)
        @start = Node.new(0, 0)
        @stop  = Node.new(@exit_pos, @exit_pos)
      
        # Assign a value for each position of the map
        map do |r, c|
            if r == 0 and c == 0 # it's the start node
                @start
            elsif r == @exit_pos and c == @exit_pos # it's the exit node
                @stop
            elsif corrupted_bytes.include?([c,r])  # it's a corrupted block
                nil
            else # create a new node for it
                Node.new(r, c)
            end
        end
      
        # Build the connectivity. Add nodes to the near attribute of the current node.
        each do |v, r, c|
            next unless v
            [[r + 1, c], 
            [r, c + 1], 
            [r - 1, c], 
            [r, c - 1]].each do |p|
                next unless inside?(p[0], p[1])
                if @memorymap[p[0]][p[1]] 
                    # puts "adding ("+p[1].to_s+","+p[1].to_s+") to near nodes"
                    v.insert(@memorymap[p[0]][p[1]]) 
                end
            end
        end
    end # initialize
        
    private 
    
    # Set row and column as the value of each element of the @memorymap array
    def map
      for r in 0...@map_size
        for c in 0...@map_size
          @memorymap[r][c] = yield(r, c)
        end
      end
      return @memorymap
    end # map
    
    # return the value, row number, and column number for each element of the @memorymap array.
    def each
      for r in 0...@map_size
        for c in 0...@map_size
          yield(@memorymap[r][c], r, c)
        end
      end
      return @memorymap
    end # map
        
    def inside?(r, c)    # Check if we're inside or outside of the matrix
        return ((0...@map_size).include?(r) and (0...@map_size).include?(c))
    end # inside?
    
end # Graph

####################### END OF GRAPH CLASS ############################


############################ NODE CLASS ################################

# Used within the graph class to represent each node/point of our map

class Node
    attr_accessor :g, :h, :prev 
    attr_reader :r, :c, :near   
  
    # Initialize an empty new Node with its coordinates (r, c).
    def initialize(r, c)

      @r = r     # row position
      @c = c     # col position
      @g = 0.0   # distance from start node
      @h = 0.0   # distance to exit node
      
      @prev = nil  # edge to previous position
      @near = []   # edges to next positions

    end # initialize
    
    def f  # Total heuristic distance from start to exit via this node
      self.g + self.h   
    end
    
    
    def distance(n)  # Distance between the current node and node n.
      return (
        (@r - n.r) ** 2 +
        (@c - n.c) ** 2
      ) ** (0.5)
    end
  
    def insert(e)
      @near << e    # Add new edge (n) to the Node's @near list.
    end

end # Node

######################## END OF NODE CLASS #############################



############################# ASTAR CLASS ##############################

# Contains the A* algorithm.
# The search method explores the graph and creates the shortest path

class ASTAR

    def initialize(start, stop)
          
      @start = start # starting node
      @stop  = stop # exit node
      
      @openset = [@start]        # Will contain the nodes that we have not explored yet.
      @closedset = []            # Will contain the nodes that have already been explored and are in our path or failing strategy.

      @start.g = 0                         # Initialize the starting point. Distance from start is zero
      @start.h = @start.distance(@stop)    # Calculate distance from start to exit
    end
    
    def search
        while @openset.size > 0       # Continue until there are no nodes in the openset
            x = openset_min_f()         # find node with minimum distance from both start and exit.        
            if x == @stop # we're at the exit - were done
            return reconstruct_path(x) # reconstruct the path and return it
            end

            @openset -= [x]     # remove node x from the openset
            @closedset += [x]   # and add it to the closedset.
            
            x.near.each do |y|  # Inspect all the nodes near x          

                next if @closedset.include?(y)  # Don't analyze the node if it's already in the closed set.

                g_score = x.g + x.distance(y)   # calculate the distance from the start point - we'll check this against the existing g_score.

                if not @openset.include?(y)  # Case 1: y is not in the openset. This is always an improvement
                    @openset += [y]
                    improving = true
                elsif g_score < y.g # Case 2: y is already in the openset, but the new g_score is lower so we've found a better strategy.
                    improving = true
                else                #  Case 3: y is in the openset but already has a better g_score.
                    improving = false
                end
            
                if improving    # this is an improved strategy, so we reach y from x
                    y.prev = x                        
                    y.g = g_score    # update the gscore value
                    y.h = y.distance(@stop)   # and update the heuristic distance from the exit
                end
            end # for
        end # while
        return []   # return an empty path if we haven't yet encountered a return - this means we didn't reach the exit.
    end # search
    
    private

    def openset_min_f # Search the openset to find the node with the minimum f
      ret = @openset[0]
      for i in 1...@openset.size
        ret = @openset[i] if ret.f > @openset[i].f
      end
      return ret
    end # openset_min_f
    
    def reconstruct_path(curr) # Recursively reconstruct the path from last node backwards.
      return ( curr.prev ? reconstruct_path(curr.prev) + [curr] : [] ) 
    end # reconstruct_path
  
  end # ASTAR

######################### END OF ASTAR CLASS ###########################

# main:

# map_size=7      # exit is at (6,6)  (or (70,70) in the full test), map size is 7x7 (71x71 in the full test)
# num_bytes=12    # calculate after 12 bytes have fallen
# fallingbytes = File.open("input_test.txt", "r").read.split

map_size=71      # exit is at (70,70), map size is 71x71
num_bytes=1024   # calculate after 1024 bytes have fallen
fallingbytes = File.open("input.txt", "r").read.split

# Create the graph based on the map size and the required number of falling bytes
graph = Graph.new(fallingbytes,map_size,num_bytes)

# Create the astar object
astar = ASTAR.new(graph.start, graph.stop)

# Perform the search
path  = astar.search
puts "shortest path length: "+path.length.to_s

# Check the path
# for node in path
#     puts "("+node.c.to_s+","+node.r.to_s+")"
# end