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

# NEW: The Problem Dampener: can tolerate a single bad level in what would otherwise be a safe report. 
#      If removing a single level from an unsafe report would make it safe, the report instead counts as safe.

# Goal: Find the number of safe reports

# For any report marked unsafe, check if removing a given level will make it safe.

num_safe=0

def check_is_safe(report)
  puts "report contains "+report.length.to_s+" levels"
  is_safe=true  # assume the report is safe until we find otherwise
  difference=report[1].to_i - report[0].to_i  # compare first two levels in the report (convert text to integer)
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
    for i in 2..report.length-1
      puts "checking level "+i.to_s+" against level "+(i-1).to_s
      difference=report[i].to_i - report[i-1].to_i    # compare this level against the previous one
      puts "difference: "+difference.to_s+" absolute difference: "+difference.abs.to_s
      if difference > 0
        new_is_increasing=true
      else 
        new_is_increasing=false
      end
      if new_is_increasing!=is_increasing or difference.abs < 1 or difference.abs > 3  
        # we are not following the current trend or increase is grater than allowed so report is not safe
        # may be able to make the report safe by removing this or the previous level from the list
        is_safe=false
        puts "report not safe because first gap too big or increasing doesn't match"
      end
    end
  end
  return is_safe
end

File.foreach("input.txt") do
  |line|   # process the report contained in this line
  report=line.split
  if check_is_safe(report)    # This report is safe. Increment the safe count.
    num_safe+=1
  else    # This report is not safe. Try dampening.
    # Note this does the job but is not very efficient as we're repeating a lot of work.
    is_safe_when_dampened=false
    # Loop through the levels. For each level, see if report is safe with that level removed.
    for i in 0..report.length-1   
      if !is_safe_when_dampened # Stop if we've already found a level that can be removed to make the report safe.
        dampened_report=report.reject.with_index{|v, j| j == i } # Create a dampened report with this level removed
        if check_is_safe(dampened_report) # The report is safe with this level removed.
          is_safe_when_dampened=true
          num_safe+=1
        end
      end
    end
  end
end

puts num_safe