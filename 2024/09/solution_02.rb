# GOAL: Calculate the checksum of the compacted files (checksum for example would be 2858)

# New compaction method:
#   Attempt to move *whole files* to the leftmost span of free space blocks that could fit the file. 
#   Attempt to move each file *exactly once* 
#   in order of decreasing file ID number starting with the file with the highest file ID number. 
#   If there is no span of free space to the left of a file that is large enough to fit the file, 
#   the file does not move.

# The process of updating the filesystem checksum is the same

class Filesystem

  attr_reader :checksum, :disk_map

  def initialize(input_file)
    @disk_map = self.get_disk_map(input_file)
    @files, @spaces, @max_file_id = self.get_block_layout
    @checksum = self.get_checksum
  end

  def get_disk_map(input_file)
    f=File.open(input_file).readline
    disk_map=f.chomp.chars  # array of the characters in the input file
    return disk_map
  end

  def get_block_layout
    # Store the file_id, file_start_pos, and length of each file
    # Store the file_id ("."), empty_block_start_pos, and length of the empty blocks
    files=[]
    spaces=[]
    start_pos=0     # keep track of the start position of the current file or empty blocks
    for char, char_pos in @disk_map.map.with_index do
      file_length=char.to_i
      if char_pos%2 == 0  # this is an even character position i.e. a file length
        files.append([start_pos,file_length])   # [file_id, file_start_pos, file_length]
      else # odd character position = empty space length
        spaces.append([start_pos,file_length])    # [empty_block_start_pos, file_length]
      end
      start_pos+=file_length   # increment start_pos so the next file/space starts at the end of this one
    end
    return files, spaces
  end

  def get_checksum
    checksum=0
    # start from the r.h. file, i.e. the file with the highest file_id
    (@files.length-1).downto(0) do |i|
      file=@files[i]
      file_start=file[0]
      file_length=file[1]
      # puts "this is file "+i.to_s+" which is "+file[1].to_s+" blocks long"
      file_moved=false
      for space, space_idx in @spaces.map.with_index
        if !file_moved
          space_start=space[0]
          space_length=space[1]
          if space_start < file_start  # only check gaps with start position before the file's start position
            if space_length >= file_length # if the gap is at least as big as the file
              # puts "moving file "+i.to_s+" to start at "+space_start.to_s
              file_moved=true
              # change the start position of the file to the start position of the space
              @files[i][0] = space_start
              # change the start position of the space to just after the (new) end of the file
              @spaces[space_idx][0] = space_start+file_length
              # subtract the length of the file from the length of the space
              @spaces[space_idx][1] = space_length-file_length
            end
          end
        end
      end
    end
  for file, file_id in @files.map.with_index
    file_checksum=0
    file_start_pos=file[0]
    file_length=file[1]
    for i in file_start_pos..file_start_pos+file_length-1
      file_checksum+=i*file_id
    end
    checksum+=file_checksum
  end
  return checksum
  end

end

# filesystem = Filesystem.new('input_test.txt')
filesystem = Filesystem.new('input.txt')
puts filesystem.checksum