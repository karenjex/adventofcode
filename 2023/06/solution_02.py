inputfile = "input.txt"
f = open(inputfile, "r")

# GOAL: 

# Determine the number of ways you could beat the record
# Holding down the button (only at the start of the race) charges the boat, the boat moves once the button is released
# Boats move faster if their button was held longer, but time spent holding the button counts against the total race time. 
# For each ms you hold down the button, the boat's speed increases by one mm/ms (starting speed is 0 mm/ms).

# Example input:

# Time:      7  15   30
# Distance:  9  40  200

# Race Time:         71530
# Record Distance:  940200

# You could hold the button anywhere from 14 to 71516 milliseconds and beat the record - a total of 71503 ways

for line in f:
    line_text=line.split('\n')[0]         # get rid of the newline character
    if line_text.find('Time:')==0:                # i.e. line begins "Time:"
        times=line_text.split('Time:')[1].strip().split(' ')     # get the digits that appear after "Time:"
        time = int(''.join(times))                               # concatenate them to get the total time
    elif line_text.find('Distance:')==0:               # i.e. line begins "Distance:"
        dists=line_text.split('Distance:')[1].strip().split(' ')  # get the digits that appear after "Distance:"
        dist = int(''.join(dists))                                # concatenate them to get the total distance
num_ways=0

print('race lasts',time,'ms','and distance to beat is',dist,'mm')
# Find how many ways we can beat record_dist
for charging_time in range(1,time):     # hold the button for between 1 ms and time-1 ms inclusive
    # speed = charging_time ms
    moving_time = time - charging_time
    dist_moved = charging_time * moving_time
    if dist_moved>dist:
        num_ways+=1

f.close()

print(num_ways)