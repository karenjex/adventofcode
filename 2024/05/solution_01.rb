# GOAL: 
# Determine which updates are in the correct order. 
# Return the sum of the middle page number from the correctly-ordered updates.

# First section of input: page ordering rules, one per line. 
#   e.g. rule 47|53 means that if an update includes both page number 47 and page number 53, 
#   then page number 47 must be printed at some point before page number 53.

# Second section of input:
#   One line per input, containing a list of page numbers

# Test input (sum of middle page numbers of the 3 correctly-ordered updates = 143):

# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47

total=0

rules=[]
input=[]

gathering_rules=true

# Process input
# File.foreach("input_test.txt") do
File.foreach("input.txt") do
  |line|
  if gathering_rules      # if we've not yet reached the empty line, keep gathering rules
    if line.strip.empty?  # we've reached the empty line between the rules and the input lines
      gathering_rules=false 
    else  # if the line isn't empty
      rule=line.chomp.split("|")
      rules.append(rule)
    end
  else
    input_line=line.chomp.split(",")
    input.append(input_line)
  end
end

# For each input line: check that each rule is satisfied
#                      if so, find the middle number and add it to the running total

for line in input    # check each input line
  is_valid=true   # start by assuming the line is valid - i.e. no rules have yet been broken
  # puts "Checking line"
  # puts line
  # puts
  for rule in rules
    # puts "  checking rule "+rule[0]+" | "+rule[1]
    first_page=rule[0]
    last_page=rule[1]
    if is_valid # no point continuing to check if we already found a rule that's not followed
      rule_obeyed=true  # start by assuming the rule has been obeyed
      if line.include? first_page and line.include? last_page # i.e. both first_page and last_page exist in line
        # puts "    found both pages"
        if line.index(first_page)>line.index(last_page)  # the pages both exist but are not in the correct order
          rule_obeyed=false
          # puts "    RULE BROKEN"
        end
      end
      if !rule_obeyed   # if the rule was not obeyed, we know that this line is not valid
        is_valid=false
      end
    end
  end
  if is_valid
    # puts "LINE OK"
    # find middle number
    middle_number = line[(line.length - 1) / 2].to_i
    # add middle number to running total
    total+=middle_number
  end
end

puts "Total of the middle numbers"
puts total
