# GOAL: Find many stones will you have after blinking 25 times

# Every time you blink, the stones change according to the first applicable rule in this list:

#     If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
#     If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
#     If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

# No matter how the stones change, their order is preserved, and they stay on their perfectly straight line.

# Example: Puzzle input gives the initial arrangement of stones:
# 125 17
# After blinking 25 times, you would have 55312 stones!

class Stones

  attr_reader :num_stones, :stone_layout, :blink, :new_num_stones

  def initialize(input_file, num_blinks)
    @stone_layout = self.get_stone_layout(input_file)
    @num_stones = @stone_layout.length
    @new_num_stones = self.blink(num_blinks)
  end

  def get_stone_layout(input_file)
    f=File.open(input_file).readline
    stone_layout=f.chomp.split(" ")  # array of the numbers in the input file (separated by space)
    return stone_layout
  end

  def blink(num_blinks)
    for i in 1..num_blinks
      new_stone_layout=[]
      for stone in @stone_layout
        if stone.to_i == 0     # If the stone is engraved with the number 0
          new_stone_layout.append('1')  #  replace it with a stone engraved with the number 1.
        elsif stone.chars.length%2==0    # If the stone is engraved with a number that has an even number of digits
          # replace it with two stones. left half of the digits on the new left stone, right half on nre right stone.
          half_length = stone.chars.length/2
          left_half = stone[0,half_length]   # get half of the length, starting at 0 (conv)
          right_half = stone[half_length,half_length].to_i.to_s   # get half of the length, starting at length-1. Convert to integer then back to string to remove trailing zeros
          new_stone_layout.append(left_half)
          new_stone_layout.append(right_half)
        else  # replace with a new stone that has the old stone's number multiplied by 2024.
          new_stone_layout.append((stone.to_i*2024).to_s)
        end     
      end
      @stone_layout = new_stone_layout
    end
    return @stone_layout.length
  end

end

stones = Stones.new('input.txt', 25)

# puts stones.stone_layout
# puts
puts stones.new_num_stones
