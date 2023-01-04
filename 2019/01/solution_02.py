# Goal: Calculate the sum of the fuel requirements for all of the modules on your spacecraft taking into account mass of fuel

# A module of mass 14 requires 2 fuel. 
# This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.

# At first, a module of mass 1969 requires 654 fuel. 
# Then, this fuel requires 216 more fuel (654 / 3 - 2). 
# 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. 
# So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.

# The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

# inputfile = "input_test.txt"    # expected result  2 + 966 + 50346 = 51314
inputfile = "input.txt"


# fuel_required = int(module_mass/3)-2
#               + int(  fuel_required  /3)-2
#               + int(    int(fuel_required/3)-2    /3 ) - 2

def calculate_additional_fuel(fuel,total_fuel):
    while int(fuel/3)-2>0:
        fuel=int(fuel/3)-2
        total_fuel+=fuel
        # print('adding',fuel,'to total to get',total_fuel)
        calculate_additional_fuel(fuel,total_fuel)
    return(total_fuel)

fuel_counter=0

with open(inputfile) as f:
    for line in f:
        mass=int(line)
        initial_fuel=int(mass/3)-2
        additional_fuel=calculate_additional_fuel(initial_fuel,0)
        # print('fuel required for',mass,'=',initial_fuel,'+',additional_fuel)
        fuel_counter+=(initial_fuel+additional_fuel)

print(fuel_counter)