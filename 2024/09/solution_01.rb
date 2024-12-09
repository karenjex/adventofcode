# GOAL: Calculate the checksum of the compacted files

# Example Input (disk map). Checksum of the compacted files is 1928:
# 2333133121414131402

# The digits alternate between indicating the length of a file and the length of free space.

# Example input represents these blocks, where n indicates block of file with id n and . indicates free space:
# 00...111...2...333.44.5555.6666.777.888899

# Move file blocks one at a time from the end of the disk to the leftmost free space block until there are no gaps remaining between file blocks:

# 00...111...2...333.44.5555.6666.777.888899
# 009..111...2...333.44.5555.6666.777.88889.
# 0099.111...2...333.44.5555.6666.777.8888..
# 00998111...2...333.44.5555.6666.777.888...
# 009981118..2...333.44.5555.6666.777.88....
# 0099811188.2...333.44.5555.6666.777.8.....
# 009981118882...333.44.5555.6666.777.......
# 0099811188827..333.44.5555.6666.77........
# 00998111888277.333.44.5555.6666.7.........
# 009981118882777333.44.5555.6666...........
# 009981118882777333644.5555.666............
# 00998111888277733364465555.66.............
# 0099811188827773336446555566..............

# Then calculate the updated filesystem checksum:
# Add up the result of multiplying each of these blocks' position with the file ID number it contains. 
# The leftmost block is in position 0. If a block contains free space, skip it instead.

# Example checksum: 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32, and so on. 

class Filesystem

  attr_reader :checksum, :disk_map

  def initialize(input_file)
    @disk_map = self.get_disk_map(input_file)
    @block_layout = self.get_block_layout
    @checksum = self.get_checksum
  end

  def get_disk_map(input_file)
    f=File.open(input_file).readline
    disk_map=f.chomp.chars  # array of the characters in the input file
    # puts disk_map
    return disk_map
  end

  def get_block_layout
    block_layout=[]
    for char, char_pos in @disk_map.map.with_index do
      if char_pos%2 == 0  # even character position = file length
        for i in 1..char.to_i
          block_layout.append(char_pos/2)
        end
      else # odd character position = empty space length
        for i in 1..char.to_i
          block_layout.append(".")
        end
      end
    end
    # puts block_layout
    return block_layout
  end

  def get_checksum
    checksum=0
    new_block_layout=@block_layout
    for block, block_position in @block_layout.map.with_index
      # puts "block "+block.to_s+" is in position "+block_position.to_s
      # if block_position<new_block_layout.length-1
        if block=='.'   # we have a gap - fill it with the last non-empty block
          empty_blocks=true   # assume there's an empty block at the end of the string
          while empty_blocks
            last_block = new_block_layout.pop   # identify last block
            # puts "last block: "+last_block.to_s
            if last_block != '.'    # the last block not empty
              empty_blocks=false
              new_block_layout[block_position]=last_block  # replace the '.' with the last_block's file_id
            end          
            # puts "new block layout "+new_block_layout
          end
        end
      # end
    end
    for block, block_position in new_block_layout.map.with_index
      checksum+=(block.to_i*block_position)
    end
    return checksum
  end

end

filesystem = Filesystem.new('input.txt')
puts filesystem.checksum