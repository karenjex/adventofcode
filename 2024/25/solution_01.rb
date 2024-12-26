# GOAL: Find number of unique lock/key pairs that fit together without overlapping in any column.

# Locks: top row filled (#) and bottom row empty (.)
# pins extend downward from top.

# Keys: top row empty and bottom row filled.
# pins extend upward from bottom.

# Example (3 unique lock/key combinations without overlapping):

# #####
# .####
# .####
# .####
# .#.#.
# .#...
# .....

# #####
# ##.##
# .#.##
# ...##
# ...#.
# ...#.
# .....

# .....
# #....
# #....
# #...#
# #.#.#
# #.###
# #####

# .....
# .....
# #.#..
# ###..
# ###.#
# ###.#
# #####

# .....
# .....
# .....
# #....
# #.#..
# #.#.#
# #####


class Lockkeys

  attr_reader :num_possible_combos

  def initialize(input)
    @locks, @keys =self.process_input(input)  
    @lock_width=5
    @lock_height=6   # lazy version - including the last line of each lock/key so I don't have to check for it
    @num_possible_combos=self.check_locks
  end

  def process_input(input)
    locks=[]      
    keys=[]       
    lock=[]
    key=[]
    start_collecting=true
    collecting_lock=false
    collecting_key=false
    File.foreach(input) do
      |line|        
      # puts
      # puts "processing line "+line.chomp
      if line.chomp==""    # collect next lock or key
        # puts "gap between lock/key"
        if collecting_key
          keys.append(key)
        elsif collecting_lock
          locks.append(lock)
        end
        start_collecting=true
        collecting_lock=false
        collecting_key=false
      elsif start_collecting and line.chomp=="#####" # this is a lock
        # puts "this is a lock - collecting lock info"
        start_collecting=false
        collecting_lock=true
        # puts "collecting_lock: "+collecting_lock.to_s
        lock=[0,0,0,0,0]
      elsif start_collecting and line.chomp=="....." # this is the start of a key
        # puts "this is a key - collecting key info"
        start_collecting=false
        collecting_key=true
        # puts "collecting_key: "+collecting_key.to_s
        key=[0,0,0,0,0]
      else
        if collecting_lock
          # puts "  this is a line of a lock"
          # get info about the lock. Store it in lock
          for pin, pin_position in line.chomp.chars.map.with_index
            if pin=="#"
              lock[pin_position]+=1
            end
          end      
        elsif collecting_key
          # puts "  this is a line of a key"
          for pin, pin_position in line.chomp.chars.map.with_index
            if pin=="#"
              key[pin_position]+=1
            end
          end
        end
      end
    end
    if collecting_key
      keys.append(key)
    elsif collecting_lock
      locks.append(lock)
    end
    # puts "locks"
    # puts locks
    # puts
    # puts "keys"
    # puts keys
    # puts
    return locks, keys
  end

  def check(lock,key)
    # check if given key may fit given lock - return true if so, false otherwise
    # key is OK for lock if there are no overlaps.
    # assume key and lock are same height (seems to be true - may need to change this)
    is_possible=true   # start by assuming there are no overlaps
    for i in 0..@lock_width-1
      if lock[i]+key[i]>@lock_height    # there's an overlap on this pin
        is_possible=false
      end
    end
    return is_possible
  end

  def check_locks
    num_possible_combos=0
    for lock in @locks
      for key in @keys
        if check(lock,key)
          num_possible_combos+=1
        end
      end
    end
    return num_possible_combos
  end

end

lockkeys=Lockkeys.new("input.txt")
puts lockkeys.num_possible_combos