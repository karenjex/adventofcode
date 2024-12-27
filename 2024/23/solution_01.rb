# GOAL: Count the sets of three inter-connected computers where at least one computer name starts with t

# Example (with 7 possibles):

# kh-tc
# qp-kh
# de-cg
# ka-co
# yn-aq
# qp-ub
# cg-tb
# vc-aq
# tb-ka
# wh-tc
# yn-cg
# kh-ub
# ta-co
# de-co
# tc-td
# tb-wq
# wh-td
# ta-ka
# td-qp
# aq-cg
# wq-ub
# ub-vc
# de-ta
# wq-aq
# wq-vc
# wh-yn
# ka-de
# kh-ta
# co-tc
# wh-qp
# tb-vc
# td-yn

class Network

  attr_reader :num_possible_clusters

  def initialize(input)
    @connections, @computers =self.process_input(input)   # connections = edges, computers = vertices
    @num_possible_clusters=self.find_clusters
  end

  def process_input(input)
    connections=[]         # edges
    computers=[]           # vertices
    File.foreach(input) do
      |line|        
      computer1=line.chomp.split("-")[0]
      computer2=line.chomp.split("-")[1]
      connection=[computer1,computer2]
      connections.append(connection)
      computers.append(computer1,computer2)
    end
    for connection in connections
      # puts connection[0]+"=>"+connection[1]
    end
    return connections, computers.uniq
  end

  def find_clusters
    num_clusters=0
    num_connections=@connections.length
    for i in 0..num_connections-3
      for j in i+1..num_connections-2
        computer1=@connections[i][0]
        computer2=@connections[i][1]
        computer3=@connections[j][0]
        computer4=@connections[j][1]
        if computer1.chars.first=='t' or computer2.chars.first=='t' or computer3.chars.first=='t' or computer4.chars.first=='t'
          if computer1==computer3
            for k in j+1..num_connections-1
              # if there's a connection between computer2 and computer4 this is a cluster
              if (computer2 == @connections[k][0] and computer4 == @connections[k][1]) or (computer2 == @connections[k][1] and computer4 == @connections[k][0])
                num_clusters+=1
              end
            end
          elsif computer2==computer3
            for k in j+1..num_connections-1
              # if there's a connection between computer1 and computer4 this is a cluster
              if (computer1 == @connections[k][0] and computer4 == @connections[k][1]) or (computer1 == @connections[k][1] and computer4 == @connections[k][0])
                num_clusters+=1
              end
            end
          elsif computer1==computer4
            for k in j+1..num_connections-1
              # if there's a connection between computer2 and computer3 this is a cluster
              if (computer2 == @connections[k][0] and computer3 == @connections[k][1]) or (computer2 == @connections[k][1] and computer3 == @connections[k][0])
                num_clusters+=1
              end
            end
          elsif computer2==computer4
            for k in j+1..num_connections-1
              # if there's a connection between computer1 and computer3 this is a cluster
              if (computer1 == @connections[k][0] and computer3 == @connections[k][1]) or (computer1 == @connections[k][1] and computer3 == @connections[k][0])
                num_clusters+=1
              end
            end
          end
        end
      end
    end
    return num_clusters
  end

end

network=Network.new("input.txt")
puts network.num_possible_clusters