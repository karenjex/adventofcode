
# need to add flow rate for eaech valve to the graph
graph = {
  'AA' : {'opened': False, 'flowrate' : 0 , 'tunnels': ['DD', 'II', 'BB']},
  'BB' : {'opened': False, 'flowrate' : 13 , 'tunnels': ['CC', 'AA']},
  'CC' : {'opened': False, 'flowrate' : 2 , 'tunnels': ['DD', 'BB']},
  'DD' : {'opened': False, 'flowrate' : 20 , 'tunnels': ['CC', 'AA', 'EE']},
  'EE' : {'opened': False, 'flowrate' : 3 , 'tunnels': ['FF', 'DD']},
  'FF' : {'opened': False, 'flowrate' : 0 , 'tunnels': ['EE', 'GG']},
  'GG' : {'opened': False, 'flowrate' : 0 , 'tunnels': ['FF', 'HH']},
  'HH' : {'opened': False, 'flowrate' : 22 , 'tunnels': ['GG']},
  'II' : {'opened': False, 'flowrate' : 0 , 'tunnels': ['AA', 'JJ']},
  'JJ' : {'opened': False, 'flowrate' : 21 , 'tunnels': ['II']}
}

print(graph['BB']['flowrate'])

# Breadth first search - this will traverse the tree to visit the nodes

# visited = []     # List for visited nodes.
queue = []       # Initialize a queue


# def bfs(visited, graph, valve): #function for breadth first search. Would depth first work best, or do I need to check each time which to do?
def bfs(graph, valve): #function for breadth first search. Would depth first work best, or do I need to check each time which to do?

  # visited.append(valve)               # add valve ID to list of valves we have visited (do we need this?)
  queue.append(valve)                 # add valve ID to queue (valves to visit)

  total_flow = 0
  flow_per_min = 0
  minute=1

# sorted_neighbours_by_flowrate = sorted(neighbour_flowrates.items(), key=lambda x:x[1])

  while minute < 31: # and queue:                             # each minute for 30 minutes: open current valve or move to new valve
    if graph[valve]['flowrate']>0 and graph[valve]['opened']==False:
      graph[valve]['opened']=True                          # open the valve (if the valve isn't already opened and this will increase the flow)
      print("opened valve",valve)
      flow_per_min+=graph[valve]['flowrate']               # add this valve's flow rate to flow per minute
          # minute+=1
      # print("minute:",minute,"flow rate:",flow_per_min)
    else:                                                  # either valve is already open, or opening it would not increase flow
      # current_valve = queue.pop(0)                         # Choose next tunnel
      neighbours=graph[valve]['tunnels']        # list of valves that we can get to from current valve
      neighbour_flowrates={}
      for neighbour in neighbours:
        neighbour_flowrates[neighbour]=graph[neighbour]['flowrate']     # create dict of flowrates of neighbours
        # print(neighbour_flowrates[neighbour])
      sorted_neighbour_list=sorted(neighbour_flowrates.items(), key=lambda x:x[1], reverse=True)
      print(sorted_neighbour_list)
      # sorted_neighbours = dict(sorted_neighbour_list)
      best_neighbour_id = sorted_neighbour_list[0][0]
      # print(sorted_neighbours)
      # for neighbour in sorted_neighbours:
      # if minute < 31:
        #   print("moving to valve:",graph[neighbour])
        #   visited.append(neighbour)
          # queue.append(best_neighbour)
      print("moved to",neighbour)
      valve=best_neighbour_id
    total_flow+=flow_per_min                             # add this minute's flow to total flow
    minute+=1
    print("minute:",minute,"flow rate:",flow_per_min)
          # if minute < 31 and graph[neighbour]['flowrate']>0 and graph[neighbour]['opened']==False:
          #   graph[neighbour]['opened']=True
          #   print("opened valve",neighbour)
          #   flow_per_min+=graph[neighbour]['flowrate']
          #   total_flow+=flow_per_min
          #   minute+=1
          #   print("minute:",minute,"flow rate:",flow_per_min)
  return total_flow


print("Following is the Breadth-First Search")
# total_flow=bfs(visited, graph, 'AA')
total_flow=bfs(graph, 'AA')
print(total_flow)