antennas={"0"=>[[4, 4]], "A"=>[[9, 9]]}

antennas["0"].append([1,2])

if antennas.has_key?("0")
    puts "entry with value O"
else
    puts "NO entry with value O"
end

for antenna in antennas
    puts antenna
end