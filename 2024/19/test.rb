towel_designs=["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]

# order towel_designs alphabetically by first letter then by length descending.
# towel_designs=["bwu", "br", "b", "gb","g", "rb", "r", "wr"]

# sorted_towels=towel_designs.sort
sorted_towels = towel_designs.sort_by {|x| -x.length}

puts "sorted_towels"
puts sorted_towels

desired_designs=["brwrr","bggr","gbbr","rrbgbr","ubwu","bwurrg","brgr","bbrgwb"]


def check_design(desired_design, sorted_towels)
    design_possible=false  # start by assuming we can't make the design.
    still_looking=true
    while still_looking
      initial_length=desired_design.length
      for towel_pattern in sorted_towels
        # find the longest towel pattern that matches the beginning of the design
        desired_design=desired_design.delete_prefix(towel_pattern)  # if towel pattern exists at beginning of design, remove it
        # puts desired_design        
      end
      if desired_design.length==0    # we managed to make the pattern
        design_possible=true
        still_looking=false
      elsif desired_design.length == initial_length  # we haven't managed to make any progress - no point trying the towel designs again
        still_looking=false
      end 
    end
    # puts design_possible
    return design_possible
end

num_possible_designs=0
for design in desired_designs
  if check_design(design, sorted_towels)
    num_possible_designs+=1
  end
end
puts num_possible_designs