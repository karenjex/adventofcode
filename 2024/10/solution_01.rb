# GOAL: Calculate the sum of the scores of all trailheads on your topographic map

# A hiking trail is any path that starts at height 0, ends at height 9, and always increases by a height of exactly 1 at each step. 
# Hiking trails never include diagonal steps - only up, down, left, or right (from the perspective of the map).

# A trailhead is any position that starts one or more hiking trails - here, these positions will always have height 0. 
# A trailhead's score is the number of 9-height positions reachable from that trailhead via a hiking trail. 

# Example: This has 9 trailheads with scores of 5, 6, 5, 3, 1, 3, 5, 3, and 5. 

# [char,line] => score
# [2,0]       => 5
# [4,0]       => 6
# [4,2]       => 5
# [6,4]       => 3
# [2,5]       => 1
# [5,5]       => 3
# [0,6]       => 5
# [6,6]       => 3
# [1,7]       => 5

# Total:        36

# line
# | 01234567 <-- char
# v
# 0 89010123
# 1 78121874
# 2 87430965
# 3 96549874
# 4 45678903
# 5 32019012
# 6 01329801
# 7 10456732

class Topomap

  attr_reader :check_around, :get_trailhead_score, :test_trailhead_score, :total_trailhead_score

  def initialize(input_file)
    @topo_map = self.get_topo_map(input_file)
    @total_trailhead_score=0
    @high_points=[]
    @total_trailhead_score = self.get_trailhead_score
    @test_trailhead_score = self.check_around(0,4,0)
  end

  def check_around(line_num, char_pos, value)
    # Check a potential trailhead to find out how many 9 height points can be reached from it
    # puts "  Checking ABOVE line "+line_num.to_s+" position "+char_pos.to_s+" value "+value.to_s
    if line_num > 0  # no point checking above if we're already on the first line  
      if (@topo_map[line_num-1][char_pos]).to_i == value+1
        if value+1 == 9
          # puts "  found a trail ending at line "+(line_num-1).to_s+", char "+char_pos.to_s
          @high_points.append([char_pos,line_num-1])
        else  # we found the next number, but we're not yet at the end of a trail
          check_around(line_num-1, char_pos, value+1)
        end
      end
    else
      # puts "    at the top - don't bother checking above"
    end       
    # puts "  Checking RIGHT of line "+line_num.to_s+" position "+char_pos.to_s+" value "+value.to_s
    if char_pos < @topo_map[0].length - 1  # no point checking to the right if we're already on the last char
      if (@topo_map[line_num][char_pos+1]).to_i == value+1
        if value+1 == 9
          # puts "  found a trail ending at line "+line_num.to_s+", char "+(char_pos+1).to_s
          @high_points.append([char_pos+1,line_num])
        else  # we found the next number, but we're not yet at the end of a trail
          check_around(line_num, char_pos+1, value+1)
        end
      end
    else
      # puts "    at the r.h.s - don't bother checking to right"
    end            
    # puts "  Checking BELOW line "+line_num.to_s+" position "+char_pos.to_s+" value "+value.to_s
    if line_num < @topo_map.length - 1    # no point checking below if we're already on the last line
      if (@topo_map[line_num+1][char_pos]).to_i == value+1
        if value+1 == 9
          # puts "  found a trail ending at line "+(line_num+1).to_s+", char "+char_pos.to_s
          @high_points.append([char_pos,line_num+1])
        else  # we found the next number, but we're not yet at the end of a trail
          check_around(line_num+1, char_pos, value+1)
        end
      end
    else
      # puts "    at the bottom - don't bother checking below"
    end
    # puts "  Checking LEFT of line "+line_num.to_s+" position "+char_pos.to_s+" value "+value.to_s
    if char_pos > 0    # no point checking to the left if we're already on the first char
      if (@topo_map[line_num][char_pos-1]).to_i == value+1
        if value+1 == 9
          # puts "  found a trail ending at line "+line_num.to_s+", char "+(char_pos-1).to_s
          @high_points.append([char_pos-1,line_num])
        else  # we found the next number, but we're not yet at the end of a trail
          check_around(line_num, char_pos-1, value+1)
        end
      end
    else
      # puts "    at l.h.s - don't bother checking left"
    end       
    # puts "  num unique high points for this trailhead: "+@high_points.uniq.length.to_s
    return @high_points.uniq.length
  end

  def get_topo_map(input_file)
    topo_map=[]
    File.foreach(input_file) do
      |line|
      topo_map.append(line.chomp.chars)  # array of the characters in the input file
    end
    return topo_map
  end

  def get_trailhead_score
    # Find each trailhead along with the number of trails that lead from it
    total_trailhead_score=0
    for row, row_id in @topo_map.map.with_index
      for char, char_pos in row.map.with_index
        height=char.to_i
        if height==0 # this may be a trailhead - check it and get the number of 9 height points we can reach from it
          # puts "There may be a trailhead at line "+row_id.to_s+", char "+char_pos.to_s
          @high_points=[]
          this_trailhead_score=check_around(row_id, char_pos, height)
          total_trailhead_score+=this_trailhead_score
        end
      end
    end
    return total_trailhead_score
  end

end

# topomap = Topomap.new('input_test.txt')
topomap = Topomap.new('input.txt')
puts "Total trailhead score: "+topomap.total_trailhead_score.to_s
