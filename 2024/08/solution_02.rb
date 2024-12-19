# GOAL: 
# Find the number of unique locations within the bounds of the map that contain an antinode

# As part 1, but this time an antinode occurs at any grid position 
# exactly in line with at least two antennas of the same frequency, regardless of distance. 

# Antenna frequency is indicated by a single lowercase letter, uppercase letter, or digit.

# Example (now has 34 total unique antinode locations):

# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............

class AntennaMap

    attr_reader :antinode_count       
    # attr_writer :pos, :dir

    def initialize(input_file)
        @map_lines = self.get_map_lines(input_file)
        @map_width = @map_lines[0].length
        @antennas = self.get_antennas       # hash of antennas of form: frequency=> [[char_pos,line_num],...]
        @antinode_count = self.get_antinode_count
        @antinodes = []
    end

    def get_map_lines(input_file)
        map_lines = []
        File.foreach(input_file) do
            |line|
            map_line=line.chomp.chars  # array of the characters in the map line
            map_lines.append(map_line)
        end
        return map_lines
    end

    def get_antennas
        antennas={}  # store antennas as a hash where key is the frequency, val is array of positions
        for map_line, line_num in @map_lines.map.with_index
            for char, char_pos in map_line.map.with_index
                if /[[:alnum:]]/.match(char)
                    puts "Antenna found at ("+char_pos.to_s+","+line_num.to_s+") with frequency "+char
                    if antennas.has_key?(char)      # this frequency is already in the list of antenas
                        antennas[char].append([char_pos,line_num])
                    else  # add this frequency to list of antennas
                      antennas[char] = [[char_pos,line_num]]
                    end
                end
            end
        end
        puts antennas
        return antennas
    end

    def get_antinode_count
        antinodes=[]
        antinode_count=0
        @antennas.each do |frequency|
            freq_val=frequency[0]
            positions=frequency[1]
            puts "freq_val: "+freq_val
            # for each pair of antennas of this frequency, calculate their antinodes
            for i in 0..positions.length-2
                # puts "i: "+i.to_s
                for j in (i+1)..positions.length-1
                    # puts "j: "+j.to_s
                    antenna_1=positions[i]
                    puts "antenna 1: "+antenna_1[0].to_s+","+antenna_1[1].to_s
                    antenna_2=positions[j]
                    puts "antenna 2: "+antenna_2[0].to_s+","+antenna_2[1].to_s
                    distance_x = antenna_2[0] - antenna_1[0]
                    distance_y = antenna_2[1] - antenna_1[1]

                    # This time, distance doesn't matter. 
                    # We need to get ALL points that fall in the straight line between the 2 antennas

                    # Take the distance vector and simplify the ratio as far as possible
                    # e.g. distance [3,6] would simplify to [1,2]

                    # from point 1:
                    #   repeatedly subtract the simplified vector and add the new position to the list
                    #   repeatedly add the simplified vector and add the new position to the list

                    # simplified distance: 
                    gcd = distance_x.gcd(distance_y)
                    new_dist_x=distance_x/gcd
                    new_dist_y=distance_y/gcd
                    puts "distance: "+distance_x.to_s+","+distance_y.to_s
                    puts "simplified distance: "+new_dist_x.to_s+","+new_dist_y.to_s

                    point_1=antenna_1

                    in_map=true
                    while in_map
                      antinode=[point_1[0]-new_dist_x]
                      antinode.append(point_1[1]-new_dist_y)
                      if antinode[0] >= 0 and antinode[0] < @map_width and antinode[1] >= 0 and antinode[1] < @map_lines.length
                        antinodes.append(antinode)
                      else
                        in_map=false
                      end
                      point_1=antinode
                    end

                    in_map=true
                    while in_map
                        antinode=[point_1[0]+new_dist_x]
                        antinode.append(point_1[1]+new_dist_y)
                        if antinode[0] >= 0 and antinode[0] < @map_width and antinode[1] >= 0 and antinode[1] < @map_lines.length
                          antinodes.append(antinode)
                        else
                          in_map=false
                        end
                        point_1=antinode
                    end
                end
            end
        end
        return antinodes.uniq.length
    end
end

# Process the input to get the map
antenna_map = AntennaMap.new("input.txt")
puts antenna_map.antinode_count