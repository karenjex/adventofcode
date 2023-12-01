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

valve=graph['AA']
neighbour_ids=valve['tunnels']

for tunnel in neighbour_ids:
    neighbours.append(graph[tunnel])

for sortedValue in sorted(neighbours.values()):
    print sortedValue # gives the values sorted by value

