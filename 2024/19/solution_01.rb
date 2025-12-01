# GOAL:  Find how many of the desired designs are possible with the list of towel patterns.

# Each towel has a pattern of colored stripes. 
# You can use as many towels of a given pattern as you need. 

# Stripes: white (w), blue (u), black (b), red (r), or green (g).

# Options to display the design rgrgr:
#   two rg towels and then an r towel 
#   an rgr towel and then a gr towel
#   a single massive rgrgr towel

# The first line indicates the available towel patterns
# After the blank line, the remaining lines each describe a desired design

# Example (6 of the eight designs are possible):

# r, wr, b, g, bwu, rb, gb, br
# 
# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb


# desired design (dd): brwrr or [b,r,w,r,r]
# available patterns: r, wr, b, g, bwu, rb, gb, br
# whilst dd != []
  # for pattern in available patterns, check if the pattern matches the remaining desired design
  #   [b,r,w,r,r]
  #   r: NO
  #   wr: NO
  #   b: YES
  #     [r,w,r,r]
  #     r: YES
  #       [w,r,r]
  #       r: NO
  #       wr: YES
  #         [r]
  #         r: YES
  #           [] => DONE!

# BUT: This could give a false negative. How do we go back and "try again" if needed?

class Towels

  attr_reader :num_possible_designs

  def initialize(input)
    @towel_designs, @desired_designs=self.process_input(input)
    @num_possible_designs=self.get_num_possible_designs
  end

  def process_input(input)
    # get the map and the list of moves from the input
    desired_designs=[]
    towels=[]         
    sorted_towels=[]
    get_designs=false   # we'll collect the towel designs first, before collecting the desired designs
    File.foreach(input) do
      |line|        
      if line.strip.empty?       # we've reached the empty line between towels and desired designs
        get_designs=true
      end
      if get_designs    # gather the desired designs
        if !line.strip.empty?
          desired_designs.append(line.chomp)
        end
      else
        towels=line.chomp.split(", ")
        # towels=["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
        sorted_towels = towels.sort_by {|x| -x.length}  # sort the towel designs by longest first
      end
    end
    # return the lines of the map, plus the moves as an array
    # desired_designs=["brwrr","bggr","gbbr","rrbgbr","ubwu","bwurrg","brgr","bbrgwb"]
    return sorted_towels, desired_designs
  end

  def check_design(desired_design, towel_designs)
    still_looking=true
    while still_looking
      initial_length=desired_design.length
      for towel_pattern in towel_designs
        # find the longest towel pattern that matches the beginning of the design
        desired_design=desired_design.delete_prefix(towel_pattern)  # if towel pattern exists at beginning of design, remove it
        # puts desired_design        
      end
      if desired_design.length==0    # we managed to make the pattern
        design_possible=true
        still_looking=false
      elsif desired_design.length == initial_length  # we haven't managed to make any progress
        # ** NEED TO FIND ANOTHER WAY TO LOOK FOR THE PATTERN IF THIS DIDN'T WORK #
        still_looking=false
      end
    end
    if desired_design.length==0
      return true
    end
  end

  def get_num_possible_designs
    num_possible_designs=0
    for design in @desired_designs
      if check_design(design, @towel_designs)
        num_possible_designs+=1
      end
    end
    return num_possible_designs
  end

end

towels=Towels.new("input_test.txt")    
puts towels.num_possible_designs

# 214 is too low