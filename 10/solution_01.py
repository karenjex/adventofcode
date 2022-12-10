# Goal: Return sum of signal strengths during the 20th, 60th, 100th, 140th, 180th, and 220th cycles

# Value of X register starts at 1

# instructions:
#     addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
#     noop takes one cycle to complete. It has no other effect.

# NB: the cycle to be calculated might occur in the middle of an addx command


inputfile = "input.txt"

cycle=1         # keep track of current cycle number
x_val=1         # Value of X register starts at 1
total_signal_strength=0
cycles_to_count=[20,60,100,140,180,220]

with open(inputfile) as f:
    for line in f:
        words=line.split()
        print("Cycle",cycle,"signal_strength:",cycle*x_val)
        if cycle in cycles_to_count:                                   #     if we need to record the signal strength
            signal_strength=cycle*x_val
            total_signal_strength+=signal_strength                     #         add current signal strength to total
            print("Signal strength:",signal_strength,"New total_signal_strength",total_signal_strength)
        cycle+=1        # will always add 1 to cycle, whether noop or addx
        if words[0]=="addx":                                           # if command is addx
            if cycle in cycles_to_count:                               #     if we need to record the signal strength
                signal_strength=cycle*x_val
                total_signal_strength+=signal_strength                 #         add current signal strength to total
                print("Signal strength:",signal_strength,"New total_signal_strength",total_signal_strength)
            cycle+=1                                                   # advance another cycle and add V to current value of X
            x_val+= int(words[1])


print("Sum of required signal strenghths: ",total_signal_strength)