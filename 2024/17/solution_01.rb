# GOAL: Initialize the registers to the given values, then run the program. 
#       Once it halts, what do you get if you use commas to join the values it output into a single string?

# Example:

# Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0

# After the above program halts, its final output will be 4,6,3,5,6,3,5,2,1,0.

class Computer

  attr_reader :final_output

  def initialize(input)
    # get initial values of registers A, B & C plus program instructions
    @reg_a, @reg_b, @reg_c, @program=self.process_input(input)
    # execute program to get final output
    @final_output=self.run_program
  end

  def process_input(input)
    # get initial values of registers A, B & C plus program instructions from the input
    reg_a=0
    reg_b=0
    reg_c=0
    program=[]
    i=0
    File.foreach(input) do
      |line|        
      if i==0
        reg_a=line.chomp.split("Register A: ")[1].to_i
      elsif i==1
        reg_b=line.chomp.split("Register B: ")[1].to_i
      elsif i==2
        reg_c=line.chomp.split("Register C: ")[1].to_i
      elsif i==4
        program=line.chomp.split("Program: ")[1].split(",")
      end
      i+=1
    end
    # return the lines of the map, plus the moves as an array
    puts "Register A: "+reg_a.to_s+" Register B: "+reg_b.to_s+" Register C: "+reg_c.to_s
    puts "Program: "
    puts program
    return reg_a, reg_b, reg_c, program
  end

  def combo_operand(operand)
    if operand in (0..3)
      combo_operand=operand
    elsif operand==4
      combo_operand=@reg_a
    elsif operand==5
      combo_operand=@reg_b
    elsif operand==6
      combo_operand=@reg_c
    elsif operand==7    # does not appear in valid programs
      combo_operand=7
    end
    return combo_operand
  end

  def run_program
    # Run through the program, executing each of the instructions in turn
    final_output=""  # collect the output a a comma separated string
    pointer=0        # starting position is 0 - increase as defined in the instructions
    result=""
    while pointer < @program.length  # keep going until we get to the end of the instructions
      opcode=@program[pointer].to_i
      lit_operand=@program[pointer+1].to_i
      increase_pointer=true
      puts
      puts "pointer: "+pointer.to_s
      puts "opcode: "+opcode.to_s
      puts "operand: "+lit_operand.to_s
      puts
      if opcode==0  
        puts "adv - perform division to update A register value" 
        # value in A register divided by 2 to the power of the combo operand => A register
        @reg_a=(@reg_a/2**combo_operand(lit_operand)).to_i
      elsif opcode==1      # bxl 
        puts "bxl - perform bitwise XOR to update B register value" 
        # bitwise XOR of register B and literal operand => register B
        @reg_b=@reg_b^lit_operand
      elsif opcode==2      # bst  
        puts "bst - update B register value with combo operand modulo 8" 
        # combo operand modulo 8 => B register
        @reg_b=combo_operand(lit_operand)%8
      elsif opcode==3      # jnz 
        if @reg_a==0
          puts "jnz - A register value is 0 - do nothing" 
          # does nothing if the A register is 0. 
        else
          puts "jnz - A register value is not 0 - jump to operand value" 
          # jump by setting the instruction pointer to the value of its literal operand
          pointer=lit_operand
          increase_pointer=false
        end
      elsif opcode==4      # bxc 
        puts "bxc - perform bitwise XOR to update B register value" 
          # bitwise XOR of register B and register C => register B (ignores the operand)
        @reg_b=@reg_b^@reg_c
      elsif opcode==5      # out 
        puts "OUT - output the combo operand modulo 8"
        result=(combo_operand(lit_operand)%8).to_s+","
        final_output+=result
      elsif opcode==6      # bdv  (like adv but result stored in B reg)
        puts "bdv - perform division to update B register value" 
        # perform division, truncate result to an integer and write it to B register
        #    numerator: value in the A register. 
        #    denominator: raise 2 to the power of the combo operand.
        @reg_b=(@reg_a/2**combo_operand(lit_operand)).to_i
      elsif opcode==7      # cdv  (like adv but result stored in C reg)
        puts "bdv - perform division to update C register value" 
        # perform division, truncate result to an integer and write it to B register
        #    numerator: value in the A register. 
        #    denominator: raise 2 to the power of the combo operand.
        @reg_c=(@reg_a/2**combo_operand(lit_operand)).to_i
      end
      if increase_pointer
        pointer+=2
      end
    end
    return final_output.chomp(",")
  end

end

computer=Computer.new("input.txt")
puts "Final Output: "+computer.final_output