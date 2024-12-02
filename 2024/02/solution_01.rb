# Test input:
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9

# Each line is a report containing a number of levels, separated by spaces 
# A report is safe if:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

# Goal: Find the number of safe reports

num_safe=0

File.foreach("input.txt") do
  |report|   # process the report contained in this line
  puts "report contains "+report.split.length.to_s+" levels"
  is_safe=true  # assume the report is safe until we find otherwise
  difference=report.split[1].to_i - report.split[0].to_i  # compare first two levels in the report (convert text to integer)
  puts "difference: "+difference.to_s+" absolute difference: "+difference.abs.to_s
  if difference > 0 
    is_increasing=true
    puts "report is increasing"
  else 
    is_increasing=false    # is_increasing must stay the same value from this point for report to be safe
    puts "report is decreasing"
  end
  if difference.abs < 1 or difference.abs > 3 # increase is grater than allowed so report is not safe
    is_safe=false
    puts "report not safe because first gap too big"
  else    # report is safe so far, check through remainder of line
    puts "first gap OK so continuing"
    for i in 2..report.split.length-1
      puts "checking level "+i.to_s+" against level "+(i-1).to_s
      difference=report.split[i].to_i - report.split[i-1].to_i    # compare this level against the previous one
      puts "difference: "+difference.to_s+" absolute difference: "+difference.abs.to_s
      if difference > 0
        new_is_increasing=true
      else 
        new_is_increasing=false
      end
      if new_is_increasing!=is_increasing or difference.abs < 1 or difference.abs > 3  
        # we are not following the current trend or increase is grater than allowed so report is not safe
        is_safe=false
        puts "report not safe because first gap too big or increasing doesn't match"
      end
    end
  end
  if is_safe
    puts "report "+report+" is safe"
    num_safe+=1
  else
    puts "report "+report+" is NOT safe"
  end
end

puts num_safe