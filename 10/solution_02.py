# Goal: Render the image given by your program. What eight capital letters appear on your CRT?

# X Value represents middle of a sprite - sprite is at x_val-1, x_val, x_val+1

# One pixel is drawn during each cycle

# If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, 
# the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).

line0=""    # line1[0] written during cycle 1, line1[39] written during cycle 40
line1=""    # line2[0] written during cycle 41, line2[39] written during cycle 80
line2=""    # line3[0] written during cycle 81, line3[39] written during cycle 120
line3=""    # line4[0] written during cycle 121, line4[39] written during cycle 160
line4=""    # line5[0] written during cycle 161, line5[39] written during cycle 200
line5=""    # line6[0] written during cycle 201, line6[39] written during cycle 240

screen=[line0,line1,line2,line3,line4,line5]

inputfile = "input.txt"

cycle=1         # keep track of current cycle number
x_val=1         # Value of X register starts at 1
current_line=0  # keep track of current line (increase after every 40 cycles)

change_lines=[40,80,120,160,200,240]

# check for each cycle: is sprite at current (horizontal) position?
#    if yes: draw '#'
#    if no: draw '.'

with open(inputfile) as f:
    for line in f:
        words=line.split()
        cursor_position=cycle-(current_line*40)-1
        # print("cycle:",cycle,"line:",current_line,"cursor position",cursor_position)
        sprite_position=(x_val-1,x_val,x_val+1)
        # print("    sprite position",sprite_position)
        if cursor_position in sprite_position:                    # sprite at current position
            current_line_contents=screen[current_line]
            screen[current_line]=current_line_contents+"#"
        else:
            current_line_contents=screen[current_line]
            screen[current_line]=current_line_contents+"."
        # print("    current screen row",screen[current_line])      
        if cycle in change_lines:
            current_line+=1
        cycle+=1        # will always add 1 to cycle, whether noop or addx
        if words[0]=="addx":                                           # if command is addx
            cursor_position=cycle-(current_line*40)-1
            # print("cycle:",cycle,"line:",current_line,"cursor position",cursor_position)
            sprite_position=(x_val-1,x_val,x_val+1)
            # print("    sprite position",sprite_position)
            if cursor_position in sprite_position:                    # sprite at current position
                current_line_contents=screen[current_line]
                screen[current_line]=current_line_contents+"#"
            else:
                current_line_contents=screen[current_line]
                screen[current_line]=current_line_contents+"."
            # print("    current screen row",screen[current_line])      
            if cycle in change_lines:
                current_line+=1
            cycle+=1                                                   # advance another cycle and add V to current value of X
            x_val+= int(words[1])


for line in screen:
    print(line)

# print("Sum of required signal strenghths: ",total_signal_strength)