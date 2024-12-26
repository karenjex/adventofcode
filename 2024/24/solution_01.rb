# GOAL: Find the decimal number output on the wires starting with z?

# The first section of the input specifies the wires' starting values. 
# The second section of the input lists the gates and the wires connected to them.

# Example: (input_test_small: the three output bits form the binary number 100 which is equal to the decimal number 4)

# x00: 1
# x01: 1
# x02: 1
# y00: 0
# y01: 1
# y02: 0

# x00 AND y00 -> z00
# x01 XOR y01 -> z01
# x02 OR y02 -> z02

# process gate 0: z00 = (x00 AND y00) = (1 AND 0) = 0 
# process gate 1: z01 = (x01 XOR y01) = (1 XOR 1) = 0
# process gate 2: z02 = (x02 OR y02) = (1 OR 0) = 1

# output: z02   z01   z00
# binary:   1     0     0
# i.e.:   1*4 + 0*2 + 0*1
# decimal: 4 

class Gates

  attr_reader :gate_output

  def initialize(input)
    @gates,@wires=self.process_input(input)  
    @gate_output=self.find_gate_output
  end

  def process_input(input)
    gates=[]
    wires={}    # each wire has a name and a value 1, 0 or null
    collect_gates=false
    File.foreach(input) do
      |line|        
      if line.chomp==""    # start processing the gates
        # puts "gap between start vals and gates"
        collect_gates=true
      elsif collect_gates        # this is a gate
        gates.append(line.chomp)
      else    # this is a start_val
        wire_name=line.chomp.split(": ")[0]
        wire_val=line.chomp.split(": ")[1].to_i
        wires[wire_name]=wire_val
      end
    end
    return gates, wires
  end

  def decimal(z_vals)
    # for array of [position,value] calculate the decimal equivalent
    # e.g. binary_array=[[0,1],[2,1],[1,0]]=101
    decimal_num=0
    for i in z_vals
      position=i[0]
      val=i[1]
      decimal_num += (2**position)*val 
      # puts "decimal so far = "+decimal_num.to_s
    end
    return decimal_num
  end

  def find_gate_output
    while @gates.length>0     
      # As we process the gates, we're going to remove them from the array.
      # Keep going until we've processed them all, i.e. the gates array is empty
      for gate in @gates
        wire_in_1 = gate.split(" -> ")[0].split(" ")[0] 
        wire_in_2 = gate.split(" -> ")[0].split(" ")[2]
        gate_op = gate.split(" -> ")[0].split(" ")[1]
        wire_out =  gate.split(" -> ")[1]
        # if gate_in_1 and gate_in_2 exist in wires
        if @wires.has_key?(wire_in_1) and @wires.has_key?(wire_in_2)
          # calculate the gate output
          if gate_op == "AND"
            if @wires[wire_in_1]==1 && @wires[wire_in_2]==1
              wire_out_val=1
            else
              wire_out_val=0
            end
          elsif gate_op == "OR"
            if @wires[wire_in_1]==1 || @wires[wire_in_2]==1
              wire_out_val=1
            else
              wire_out_val=0
            end 
          elsif gate_op == "XOR"
            if @wires[wire_in_1] != @wires[wire_in_2]
              wire_out_val=1
            else
              wire_out_val=0
            end
          end
          @wires[wire_out]=wire_out_val
          @gates.delete(gate)
        end
      end
    end
    z_wire_vals={}
    for wire in @wires
      if wire[0].start_with?("z")
        position=wire[0].split("z")[1].to_i
        val=wire[1]
        z_wire_vals[position]=val      
      end
    end
    gate_output=decimal(z_wire_vals)
    return gate_output
  end

end

gates=Gates.new("input.txt")
puts "Gate output: "+gates.gate_output.to_s