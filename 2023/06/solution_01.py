inputfile = "input.txt"
f = open(inputfile, "r")

# GOAL: 

# Determine the number of ways you could beat the record in each race and multiply these numbers together to get the answer

# Holding down the button (only at the start of the race) charges the boat, the boat moves once the button is released
# Boats move faster if their button was held longer, but time spent holding the button counts against the total race time. 
# For each ms you hold down the button, the boat's speed increases by one mm/ms (starting speed is 0 mm/ms).

# Example input:

# Time:      7  15   30
# Distance:  9  40  200

#     1st race: lasts  7 ms, record dist   9 mm.
#     2nd race: lasts 15 ms, record dist  40 mm.
#     3rd race: lasts 30 ms, record dist 200 mm.

# Options for 1st race:

#     Hold the button for 1 millisecond, giving the boat will travel at a speed of 1 millimeter per millisecond for 6 milliseconds, reaching a total distance traveled of 6 millimeters.
#     Hold the button for 2 milliseconds, giving the boat a speed of 2 millimeters per millisecond. It will then get 5 milliseconds to move, reaching a total distance of 10 millimeters.
#     Hold the button for 3 milliseconds. After its remaining 4 milliseconds of travel time, the boat will have gone 12 millimeters.
#     Hold the button for 4 milliseconds. After its remaining 3 milliseconds of travel time, the boat will have gone 12 millimeters.
#     Hold the button for 5 milliseconds, causing the boat to travel a total of 10 millimeters.
#     Hold the button for 6 milliseconds, causing the boat to travel a total of 6 millimeters.

# Since the current record for this race is 9 millimeters, there are actually 4 different ways you could win: you could hold the button for 2, 3, 4, or 5 milliseconds at the start of the race.

# In the second race, you could hold the button for at least 4 milliseconds and at most 11 milliseconds and beat the record, a total of 8 different ways to win.
# In the third race, you could hold the button for at least 11 milliseconds and no more than 19 milliseconds and still beat the record, a total of 9 ways you could win.

# In this example, if you multiply these values together, you get 288 (4 * 8 * 9).

response=1

times=[]
distances=[]

for line in f:
    line_text=line.split('\n')[0]                             # get rid of the newline character
    if line_text.find('Time:')==0:                            # i.e. line begins "Time:"
        time_list=line_text.split('Time:')[1].split(' ')      # list of times is the space-separated list that appears after "Times:"
        for time in time_list:
            try:
                ms=int(time)
                times.append(ms)
            except:
                pass
    elif line_text.find('Distance:')==0:                      # i.e. line begins "Distance:"
        distance_list=line_text.split('Distance:')[1].split(' ')  # list of distances is the space-separated list that appears after "Distances:"
        for distance in distance_list:
            try:
                mm=int(distance)
                distances.append(mm)
            except:
                pass

for index, time in enumerate(times):
    num_ways=0
    record_dist = distances[index]
    print('race',index+1,'lasts',time,'ms','and distance to beat is',record_dist,'mm')
    # Find how many ways we can beat record_dist
    for charging_time in range(1,time):     # hold the button for between 1 ms and time-1 ms inclusive
        # speed = charging_time ms
        moving_time = time - charging_time
        dist = charging_time * moving_time
        if dist>record_dist:
            num_ways+=1
    response=response*num_ways

f.close()

print(response)