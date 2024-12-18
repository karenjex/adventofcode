# GOAL: 
# Find the number of unique locations within the bounds of the map that contain an antinode

# An antinode occurs at any point that is perfectly in line with two antennas of the same frequency
# but only when one of the antennas is twice as far away as the other. 
# For any pair of antennas with the same frequency, there are two antinodes, one on either side of them.
# Antinodes can occur at locations that contain antennas.

# Antenna frequency is indicated by a single lowercase letter, uppercase letter, or digit.

# Example (has 14 total unique antinode locations):

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
                    puts "distance: "+distance_x.to_s+","+distance_y.to_s
                    antinode_1=[antenna_1[0]-distance_x]
                    antinode_1.append(antenna_1[1]-distance_y)
                    if antinode_1[0] >= 0 and antinode_1[0] < @map_width and antinode_1[1] >= 0 and antinode_1[1] < @map_lines.length
                        antinodes.append(antinode_1)
                    end
                    antinode_2=[antenna_2[0]+distance_x]
                    antinode_2.append(antenna_2[1]+distance_y)
                    if antinode_2[0] >= 0 and antinode_2[0] < @map_width and antinode_2[1] >= 0 and antinode_2[1] < @map_lines.length
                        antinodes.append(antinode_2)
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