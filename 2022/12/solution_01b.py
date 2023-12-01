# Goal: Find the fewest steps required to move from your current position to the location that should get the best signal

# Input represents heightmap of surrounding area.
# Elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, z is the highest
# Your current position is marked S (has elevation a)
# Location that gets best signal is marked E (has elevation z) 

# During each step, you can move exactly one square up, down, left, or right. 
# The elevation of the destination square can be at most one higher than the elevation of your current square (can be one higher, same or lower)

# for each square, consider where we can go and where we want to go
# eg, for grid[0,0] in the following example,
#    move_l = False     (can not move left)
#    move_r = True      (can move right)
#    move_u = False     (can not move up)
#    move_d = True      ( can move down)
#    desired_h = r       (desired horizontal movement to get to E is "right" - could alternatively be l "left" or n "none")
#    desired_v = d       (desired vertical movement to get to E is "down" - could alternatively be u "up" or n "none")

# example:
# ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm']
# ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l']
# ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k']
# ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j']
# ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']

# graph={
#     (0,0): {'height':'a','neighbours':[(1,0),(0,1)]},
#     (1,0): {'height':'a','neighbours':[(0,0),(2,0),(1,1)]},
#     (2,0): {'height':'b','neighbours':[]},
#     (3,0): {'height':'q','neighbours':[]},
#     (4,0): {'height':'p','neighbours':[]},
#     (5,0): {'height':'o','neighbours':[]},
#     (6,0): {'height':'n','neighbours':[]},
#     (7,0): {'height':'m','neighbours':[]},
#     ...
#     (5,4): {'height':'g','neighbours':[]},
#     (6,4): {'height':'h','neighbours':[]},
#     (7,4): {'height':'i','neighbours':[]},
# }

inputfile="input_test.txt"

graph={}

max_x=0
max_y=0

y_coord=0

with open(inputfile) as f:
    for line in f:
        x_coord=0
        for char in line.strip():
            point={}
            if char=='S':
                start_coords=(x_coord,y_coord)
                point["height"]=ord('a')
            elif char=='E':
                end_coords=(x_coord,y_coord)
                point["height"]=ord('z')
            else:
                point["height"]=ord(char)
            point["neighbours"]=[]
            coords=(x_coord,y_coord)
            graph[coords]=point
            max_x=max(max_x,x_coord)
            x_coord+=1
        max_y=max(max_y,y_coord)
        y_coord+=1

# find neighbours (possible moves from each point):
for point in graph:
    x = point[0]
    y = point[1]
    neighbours=[]
    # check left, right, up and down to get neighbours
    # left:
    if x!=0:
        if (graph[(x-1,y)]['height']<=graph[(x,y)]['height']+1):
            neighbours.append((x-1,y))
    # right:
    if x!=max_x:
        if (graph[(x+1,y)]['height']<=graph[(x,y)]['height']+1):
            neighbours.append((x+1,y))
    # up:
    if y!=0:
        if (graph[(x,y-1)]['height']<=graph[(x,y)]['height']+1):
            neighbours.append((x,y-1))
    # down:
    if y!=max_y:
        if (graph[(x,y+1)]['height']<=graph[(x,y)]['height']+1):
            neighbours.append((x,y+1))
    # neighbour_heights={}                   # generate list of neighbours, sorted (in reverse order) by height
    # for neighbour in neighbours:
    #     neighbour_heights[neighbour]=graph[neighbour]['height']     # create dict of heights of neighbours
    # # sorted_neighbours=sorted(neighbour_heights.items(), key=lambda x:x[1], reverse=True)
    # sorted_neighbours=sorted(neighbour_heights, key=lambda x:x[1], reverse=True)
    # # print(sorted_neighbours)
    # graph[(x,y)]['neighbours']=sorted_neighbours
    graph[(x,y)]['neighbours']=neighbours


# print(graph)

# print(start_coords)
# print(end_coords)

# visited = set() # Set to keep track of visited nodes of graph.

# print(ord('z'))

# def search_graph(visited, graph, node):  #function for dfs 
#     # if node not in visited and node!=end_coords:
#     if node!=end_coords:
#         print (node, graph[node]['height'])
#         visited.add(node)
#         # find highest neighbour that we have not yet visited
#         found_next_step=False
#         for point in graph[node]['neighbours']:
#             if point not in visited and not found_next_step:
#                 neighbour=graph[node]['neighbours'][0]
#                 found_next_step=True
#                 search_graph(visited, graph, neighbour)

# # Driver Code
# search_graph(visited, graph, start_coords)

# https://towardsdatascience.com/a-self-learners-guide-to-shortest-path-algorithms-with-implementations-in-python-a084f60f43dc

def dfs(graph, v, parent, order):
    if not parent:
        parent[v] = None
    # checking neighbours of v
    for n in graph[v]['neighbours']:
        if n not in parent:
            parent[n] = v
            dfs(graph, n, parent, order)

    # we're done visiting a node only when we're done visiting
    # all of its descendents first
    order.append(v)


def topological_sort(V):
    parent = {}
    order = []
    for v in V.keys():
        print("v:",v)
        if v not in parent:
            parent[v] = None
            dfs(graph, v, parent, order)

    return list(reversed(order))


def dag_shortest_path(graph, source, dest):
    order = topological_sort(graph)
    parent = {source: None}
    d = {source: 0}

    for u in order:
        if u not in d: continue  # get to the source node
        if u == dest: break
        for v, weight in graph[u]['neighbours']:
            if v not in d or d[v] > d[u] + weight:
                d[v] = d[u] + weight
                parent[v] = u
    print(len(order))
    return parent, d


dag_shortest_path(graph,start_coords,end_coords)



# print("steps moved:",len(visited))