# GOAL: What is the fewest tokens you would have to spend on the claw machines to win all possible prizes?

# The machines have two buttons A and B. 
# It costs 3 tokens to push the A button and 1 token to push the B button.

# Each machine's buttons move the claw a specific amount to the right (along the X axis) and a specific amount forward (along the Y axis).

# To win the prize, the claw must be positioned exactly above the prize on both the X and Y axes.

# Note: it is not always possible to win a prize
# Note: no button needs to be pressed more than 100 times

# This time add 10000000000000 to the prize positions

class Claw_machine

  attr_reader :prize_cost, :a_moves, :b_moves, :prize_coords

  def initialize(claw_machine_input)
    @a_moves=claw_machine_input["A"]
    @b_moves=claw_machine_input["B"]
    @prize_coords=claw_machine_input["Prize"]
    @prize_cost=self.get_prize_cost
  end

  def get_prize_cost
    prize_possible=false
    prize_cost=0
    goal = [@prize_coords[0].to_i*10000000000000,@prize_coords[1].to_i*10000000000000]
    for a_presses in 1..10000
      # puts "number of 'A' presses: "+a_presses.to_s
      for b_presses in 1..10000
        # puts "    number of 'B' presses: "+b_presses.to_s
        x_pos = a_presses*@a_moves[0].to_i+b_presses*@b_moves[0].to_i
        y_pos = a_presses*@a_moves[1].to_i+b_presses*@b_moves[1].to_i
        # puts "("+x_pos.to_s + "," + y_pos.to_s+")"
        if x_pos == @prize_coords[0].to_i and y_pos == @prize_coords[1].to_i
          prize_possible=true
          # puts "PRIZE!"
          new_prize_cost=(3*a_presses)+b_presses
          if prize_cost==0 or new_prize_cost < prize_cost
            prize_cost=new_prize_cost
          end
        end
      end
    end
    # puts "prize_cost: "+prize_cost.to_s
    return prize_cost
  end

end

total_cost = 0

claw_machine_input={}
machine_line=0
File.foreach("input.txt") do
  |line|
    if line.strip.empty?  # we've reached the empty line between machines, reset the counters
      claw_machine_input={}
      machine_line=0
    else  # if the line isn't empty
      input=line.chomp.split(":")[1]     # get info from right hand side of the colon
      input_x=input.split(",")[0]        # get info from left hand side of the comma
      input_y=input.split(",")[1]        # get info from right hand side of the comma
      if machine_line==0           # get info about machine A
        x_moves = input_x.split("+")[1]   # get number from rhs of "+"
        y_moves = input_y.split("+")[1]   # get number from rhs of "+"
        claw_machine_input["A"]=[x_moves,y_moves]
      elsif machine_line==1               # get info about machine B
        x_moves = input_x.split("+")[1]   # get number from rhs of "+"
        y_moves = input_y.split("+")[1]   # get number from rhs of "+"
        claw_machine_input["B"]=[x_moves,y_moves]
      else                               # get info prize
        x_pos = input_x.split("=")[1]   # get number from rhs of "="
        y_pos = input_y.split("=")[1]   # get number from rhs of "="
        claw_machine_input["Prize"]=[x_pos,y_pos]
        claw_machine = Claw_machine.new(claw_machine_input)
        # puts "prize cost: "+claw_machine.prize_cost.to_s
        total_cost += claw_machine.prize_cost
      end
      machine_line+=1
    end
end

puts "Minimum cost for most possible prizes: "+total_cost.to_s