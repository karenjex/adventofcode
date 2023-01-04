# Goal: Calculate the sum of the fuel requirements for all of the modules on your spacecraft

# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. 
# They haven't determined the amount of fuel required yet.

# Fuel required for a module:  mass / three (round down) - 2

# For example:

#     For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
#     For a mass of 1969, the fuel required is 654.
#     For a mass of 100756, the fuel required is 33583.

# inputfile = "input_test.txt"    # expected result  2 + 654 + 33583 = 34239
inputfile = "input.txt"

fuel_counter=0

with open(inputfile) as f:
    for line in f:
        mass=int(line)
        fuel_required=int(mass/3)-2
        fuel_counter+=fuel_required

print(fuel_counter)