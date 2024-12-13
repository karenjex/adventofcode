# GOAL: 

# As for part 1, but this time:

# Determine which updates are NOT in the correct order and put them in the correct order
# Return the sum of the middle page number from these newly correctly-ordered updates.

# Plan:
# 1. Use the same method to find which updates are not in the correct order
# 2. For the updates that aren't in the correct order:
       # find all of the rules that apply
       # put the numbers in the rules into the correct order
           # need a topological sort for this.
       # find the middle number

# CREDIT:
# The code for the topological sort is taken from the example found here:
# https://medium.com/cracking-the-coding-interview-in-ruby-python-and/topological-sort-in-javascript-ruby-and-python-mastering-algorithms-c04c20f88bd5

# The resulting code is not very elegant (my fault) but I haven't got the time or energy to go back and make it better!

total=0

rules=[]
input=[]

gathering_rules=true
# Process input
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

# The topological_sort method performs a Topological Sort on the given graph.
def topological_sort(graph)
  order = []  # This array will store the sorted vertices.
  visited = {}  # This hash will keep track of visited vertices.

  # Iterate over each vertex in the graph.
  graph.keys.each do |vertex|
    # If the vertex has not been visited, perform Depth First Search (DFS) from this vertex.
    dfs(vertex, graph, visited, order) unless visited[vertex]
  end
  # The order array is filled in reverse, so we need to reverse it before returning.
  order.reverse
end

# The dfs method performs a Depth First Search from the given vertex.
def dfs(vertex, graph, visited, order)
  # Mark the current vertex as visited.
  visited[vertex] = true
  
  # Retrieve the neighbors of the current vertex from the graph.
  # If the vertex has no neighbors, default to an empty array.
  neighbors = graph[vertex] || []
  
  # Iterate over each neighbor of the current vertex.
  neighbors.each do |neighbor|
    # If the neighbor has not been visited, perform DFS from this neighbor.
    dfs(neighbor, graph, visited, order) unless visited[neighbor]
  end
  
  # After visiting all neighbors of the current vertex, add the vertex to the order array.
  order << vertex
end

# For each input line: check whether or not all rules are satisfied

for line in input    # check each input line
  is_valid=true   # start by assuming the line is valid - i.e. no rules have yet been broken
  rules_in_play=[]
  for rule in rules
    # puts "  checking rule "+rule[0]+" | "+rule[1]
    first_page=rule[0]
    last_page=rule[1]
      rule_obeyed=true  # start by assuming the rule has been obeyed
      if line.include? first_page and line.include? last_page # i.e. both first_page and last_page exist in line
        # puts "    found both pages"
        rules_in_play.append(rule)
        if line.index(first_page)>line.index(last_page)  # the pages both exist but are not in the correct order
          rule_obeyed=false
          # puts "    RULE BROKEN"
        end
      end
      if !rule_obeyed   # if the rule was not obeyed, we know that this line is not valid
        is_valid=false
      end
  end
  if !is_valid
    # put line in correct order
    # gather rules for this line into a graph
    # stored as a hash where each key is a vertex and the associated value is an array of neighbors.
    graph={}
    for rule in rules_in_play
      if graph[rule[0]]
        graph[rule[0]] = graph[rule[0]].append(rule[1])
      else
        graph[rule[0]] = [rule[1]]
      end
    end
    # Perform Topological Sort on the graph and print the sorted order.
    sorted_list=topological_sort(graph)
    # find middle number
    middle_number = sorted_list[(sorted_list.length - 1) / 2].to_i
    # add middle number to running total
    total+=middle_number
  end
end

puts "Total of the middle numbers"
puts total
