inputfile = "input.txt"
f = open(inputfile, "r")

calorie_total=0
elf_id=1
highest_cal=0

for line in f:
  if line == '\n':
    if calorie_total>highest_cal:
        highest_cal=calorie_total
        highest_elf=elf_id
    calorie_total=0
    elf_id+=1
  else:
    calories=int(line)
    calorie_total+=calories

print("Elf ", highest_elf, " is carrying the most calories: ", highest_cal, " calories")    
 
f.close()