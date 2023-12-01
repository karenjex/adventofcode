# Goal: Calculate the most pressure it is possible to release in 30 minutes 

inputfile='input_test.txt'
# inputfile='input.txt'

# get graph of valves and tunnels

valves=[]          # list of valves = list of nodes
tunnels=[]         # list of tunnels = list of edges (directional)

# process input file
with open(inputfile) as f:
    for line in f:
        valve_id = line.strip().split()[1]
        flowrate = line.strip().split()[4].split("=")[1].strip(';')    # get number from between "=" and ";"
        # print(flowrate)
        valve=(valve_id,flowrate,False)
        valves.append(valve)
        to_valves=line.strip().split('to valve')[1].strip('s').strip(' ')    # get list after "to valve" or "to valves"
        for v in to_valves.split(','):
            to_valve=v.strip(' ')
            # print(to_valve)
            tunnel=(valve_id, to_valve)
            tunnels.append(tunnel)

print("Valves",valves)
print("Tunnels",tunnels)

total_released=0
released_per_min=0
current_position='AA'

# need to find/work out algorithm for traversing the graph in the best way

for minute in range(1,31):
    # current_valve = valve in valves where valve[0] (valve_id) ==current_position
    valve_id=current_position
    flowrate=current_valve[1]
    valve_open=current_valve[2]
    if flowrate>0 and not valve_open:
        # set valve[2] to True
        released_per_min += flowrate
        total_released +=released_per_min
    else:
        # choose tunnel and move to valve with highest flowrate that is not yet open

print("total released in 30 mins:",total_released)
