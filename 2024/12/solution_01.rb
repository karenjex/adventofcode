# GOAL: Calculate total price of fencing all regions on your map of garden plots (puzzle input).

# Each plot grows a type of plant indicated by a single letter on your map.
# When multiple plots grow the same type of plant and are touching (horizontally or vertically), they form a region. 

# Plants of the same type can appear in multiple separate regions and regions can appear within other regions.

# The area of a region is the number of garden plots the region contains.
# The perimeter of a region is the number of sides of garden plots in the region that do not touch another garden plot in the same region. 

# The price of fence required for a region is found by multiplying that region's area by its perimeter. 


###                                                                                                ###
#                                                                                                    # 
# TO FIX:                                                                                            #
# If we have more than one region growing the same crop, the entry in the hash gets overwritten      #
# Change the structure to an array where the first element of each region is the crop                #
# and the second is the list of plots                                                                #
#                                                                                                    #
###                                                                                                ###


class Garden

  attr_reader :num_regions, :total_fence_price

  def initialize(input_file)
    @garden_map = self.get_garden_map(input_file)
    @regions=self.get_regions  # Return an array of regions.
                               # first element [0] = plant type, second element [1] = array of plot coordinates.
    @num_regions = @regions.length
    @total_fence_price=self.get_fence_price   # Calculate area and perimeter of each region to calculate total fence price.
  end

  def get_garden_map(input_file)
    # Return the garden map as an array of lines, each comprising an array of characters.
    garden_map=[]
    File.foreach(input_file) do
      |line|
      garden_map.append(line.chomp.chars)  # array of the characters in the input line
    end
    return garden_map
  end


  # def get_region(region_id, char_pos, line_num, plot_val)
  def get_region(region_id, char_pos, line_num, plot_val)
    # Check around given plot to find adjoining plots with the same value.
    # Add the adjoining plots to the current region and look around each of those plots in turn.

    # puts "  Checking ABOVE line "+line_num.to_s+" position "+char_pos.to_s
    if line_num > 0  # no point checking above if we're already on the first line  
      next_plot=[char_pos,line_num-1]
      next_plot_val=@garden_map[line_num-1][char_pos]
      # puts "    plot above contains '"+next_plot_val+"'"
      if next_plot_val == plot_val
        if !@regions[region_id][1].include?(next_plot) # this plot hasn't already been recorded as part of this region
          @regions[region_id][1].append(next_plot)
          get_region(region_id, char_pos, line_num-1, plot_val)
        end
      end
    end       
    # puts "  Checking RIGHT of line "+line_num.to_s+" position "+char_pos.to_s
    if char_pos < @garden_map[0].length - 1  # no point checking to the right if we're already on the last char
      next_plot=[char_pos+1,line_num]
      next_plot_val=@garden_map[line_num][char_pos+1]
      # puts "    plot to right contains '"+next_plot_val+"'"
      if next_plot_val == plot_val
        if !@regions[region_id][1].include?(next_plot) # this plot hasn't already been recorded as part of this region
          @regions[region_id][1].append(next_plot)
          get_region(region_id, char_pos+1, line_num, plot_val)
        end
      end
    end            
    # puts "  Checking BELOW line "+line_num.to_s+" position "+char_pos.to_s
    if line_num < @garden_map.length - 1    # no point checking below if we're already on the last line
      next_plot=[char_pos,line_num+1]
      next_plot_val=@garden_map[line_num+1][char_pos]
      # puts "    plot below contains '"+next_plot_val+"'"
      if next_plot_val == plot_val
        if !@regions[region_id][1].include?(next_plot) # this plot hasn't already been recorded as part of this region
          @regions[region_id][1].append(next_plot)
          get_region(region_id, char_pos, line_num+1, plot_val)
        end
      end
    end
    # puts "  Checking LEFT of line "+line_num.to_s+" position "+char_pos.to_s
    if char_pos > 0    # no point checking to the left if we're already on the first char
      next_plot=[char_pos-1,line_num]
      next_plot_val=@garden_map[line_num][char_pos-1]
      # puts "    plot to left contains '"+next_plot_val+"'"
      if next_plot_val == plot_val
        if !@regions[region_id][1].include?(next_plot) # this plot hasn't already been recorded as part of this region
          @regions[region_id][1].append(next_plot)
          get_region(region_id, char_pos-1, line_num, plot_val)
        end
      end
    end       
    return @regions[region_id]
  end

  def plot_in_region(char_pos, line_num)
    # return true if plot is already part of any region that we've identified. Otherwise, return false
    is_in_region=false
    # puts "Checking if plot ("+char_pos.to_s+","+line_num.to_s+") is already in a region."
    # puts "These are the regions we have so far: "
    # puts @regions
    for region in @regions
        if region[1].include?([char_pos, line_num])
          is_in_region=true
        end
    end
    return is_in_region
  end

  def get_regions
    @regions=[]
    region_id=0
    for line, line_num in @garden_map.map.with_index
      for plot_val, char_pos in line.map.with_index
        if !plot_in_region(char_pos, line_num) # this plot is not part of a region that we've already identified
          # identify the region containing this plot, i.e. joined plots containing the same value
          # puts "Finding region starting with plot ("+char_pos.to_s+","+line_num.to_s+") containing '"+plot_val+"'"
          @regions[region_id]=[plot_val,[[char_pos,line_num]]]
          @regions[region_id]=get_region(region_id, char_pos, line_num, plot_val)
          # puts "Region: "
          # puts @regions[region_id]
          region_id+=1   
        end
      end
    end
    return @regions
  end


  def check_around(plot, crop)
    # puts "checking around plot with crop " + crop
    # puts "coordinates "
    # puts plot
    sides_to_fence=4  # start by assuming all 4 sides must be fenced
    # check above: if plot above contains same value
    if plot[1] > 0 and @garden_map[plot[1]-1][plot[0]]==crop      # plot[0] is the x-val, ie the character pos, plot[1] is the y-val, ie the line number
      sides_to_fence-=1
    end
    # check right: if plot to right contains same value
    if plot[0] < @garden_map[0].length - 1 and @garden_map[plot[1]][plot[0]+1]==crop
      sides_to_fence-=1
    end
    # check below: if plot below contains same value
    if plot[1] < @garden_map.length - 1 and @garden_map[plot[1]+1][plot[0]]==crop
      sides_to_fence-=1
    end
    # check left: if plot to left contains same value
    if plot[0] > 0 and @garden_map[plot[1]][plot[0]-1]==crop
      sides_to_fence-=1
    end
    return sides_to_fence
  end

  def get_perimeter(region, crop)
    perimeter=0
    for plot in region[1]       # for each element in the array of plots for this region
      sides_to_fence=check_around(plot, crop)
      perimeter+=sides_to_fence
    end
  return perimeter
  end

  def get_fence_price()
    fence_price=0
    for region in @regions
      first_plot=region[1][0]
      region_crop=region[0]
      puts "Get fence price for region containing "+region_crop
      puts "with first plot "
      puts first_plot
      r_area=region[1].length
      r_perimeter=get_perimeter(region, region_crop)
      r_fence_price=r_area*r_perimeter
      fence_price+=r_fence_price
    end
    return fence_price
  end

end

# garden = Garden.new('input_test_1.txt') # A: 4 * 10 = 40, B: 4 * 8 = 32, C: 4 * 10 = 40, D: 1 * 4 = 4, E: 3 * 8 = 24. Total 140.
# garden = Garden.new('input_test_2.txt') # O: 21 * 36 = 756, each X region: 1 * 4 = 4. Total 772.
# garden = Garden.new('input_test_3.txt') # Total 1930.
garden = Garden.new('input.txt') # Total 1930.

# puts garden.garden_map
puts
puts "Garden has "+garden.num_regions.to_s+" regions."
puts "Total cost of fencing garden is "+garden.total_fence_price.to_s+"."