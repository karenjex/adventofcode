# Goal:  Find number of positions that cannot contain a beacon in the row where y=2000000

# Each sensor knows its own position and can determine the position of a beacon precisely; 
# Sensors can only lock on to the one beacon closest to the sensor (as measured by Manhattan distance)

# inputfile="input_test.txt"
inputfile="input.txt"


# process input to get list of sensors 
# For each sensor, store its x,y coords and the distance from its closest beacon)
# do we need to store the coords of the beacon? Store a separate list of beacons?

sensors = []

# y_val=10
y_val=2000000
beacons_row_y = []

with open(inputfile) as f:
    for line in f:
        sensor_x = line.strip().split()[2]
        sensor_x = sensor_x.split("=")[1] 
        sensor_x = int(sensor_x.strip(","))

        sensor_y = line.strip().split()[3]
        sensor_y = sensor_y.split("=")[1] 
        sensor_y = int(sensor_y.strip(":"))

        beacon_x = line.strip().split()[8]
        beacon_x = beacon_x.split("=")[1] 
        beacon_x = int(beacon_x.strip(","))

        beacon_y = line.strip().split()[9]
        beacon_y = int(beacon_y.split("=")[1])

        beacon_dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        sensor=(sensor_x,sensor_y,beacon_dist)
        # sensor=(sensor_x,sensor_y,beacon_x,beacon_y)
        sensors.append(sensor)
        # beacon=(beacon_x,beacon_y)
        if beacon_y==y_val:
            beacons_row_y.append(beacon_x)

# find x_vals where y_val==10 and there is no beacon

no_beacon=[]

# if y_val = s_y, no beacon between points s_x - beacon_dist and s_x + beacon_dist
# if abs(y_val - s_y) = 1, no beacon between pointsd s_x - (beacon_dist-abs(y_val - s_y)) and s_x + (beacon_dist-abs(y_val - s_y))

for sensor in sensors:
    s_x=sensor[0]
    s_y=sensor[1]
    beacon_dist=sensor[2]
    # print("sensor at",s_x,",",s_y,"dist from closest beacon",beacon_dist)

    no_beacons_from=s_x - (beacon_dist-abs(y_val - s_y))
    no_beacons_to=s_x + (beacon_dist-abs(y_val - s_y))

    for x in range(no_beacons_from,no_beacons_to+1):
        if (x) not in beacons_row_y: 
            # print("add",x,"to list")
            no_beacon.append((x))

# print("beacons on row y:",beacons_row_y)
# print("points with no beacon on row y:",no_beacon)
no_beacon_dedup = list(set(no_beacon))

print("There are",len(no_beacon_dedup),"points with no beacon on line",y_val)