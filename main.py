import networkx as nx
import matplotlib.pyplot as plt
"""
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_node(H) #as a node

G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e) #unpack edge tuple*

G.add_edges_from([(1, 2), (1, 3)])
"""
"""
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam") #adds node "spam"
G.add_nodes_from("spam") #add 4 nodes: 's' 'p' 'a' 'm'
G.add_edge(3, 'm')
print(G.number_of_nodes())
print(G.number_of_edges())

list(G.nodes)
list(G.edges)
list(G.adj[1])
G.degree[1]

G.edges([2, 'm'])
G.degree([2, 3])

#remove
G.remove_node(2)
G.remove_nodes_from("spam")
print(list(G.nodes))
G.remove_edge(1, 3)
print(list(G.edges))
"""
"""
DG = nx.DiGraph()
DG.add_edge(2, 1)
DG.add_edge(1, 3)
DG.add_edge(2, 4)
DG.add_edge(1, 2)
assert list(DG.successors(2)) == [1, 4]
assert list(DG.edges) == [(2, 1), (2, 4), (1, 3), (1, 2)]
"""
#Using the graph constructors
"""
G = nx.Graph()
G.add_edge(1, 2)
H = nx.DiGraph(G)  # crete a Digraph using the connections from G
print(list(H.edges))
edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist) # create a graph from an edge list
print(H.edges())
adjacency_dict = {0: (1, 2), 1:(0,2), 2:(0,1)}
H = nx.Graph(adjacency_dict) # create a Graph dict mapping nodes to nbrs
print(list(H.edges()))
"""
# accessing edges and neighbor
"""
G = nx.Graph([(1, 2, {"color": "yellow"})])
print(G[1]) # same as G.adj[1]
print(G[1][2])
print(G.edges[1, 2])
G.add_edge(1, 3)
G[1][3]['color'] = "bule"
G.edges[1, 2]['color'] = 'red'
print(G.edges[1, 2])
print(G[1])
"""
"""
FG = nx.Graph()
FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
for n, nbrs in FG.adj.items():
    for nbr, eattr in nbrs.items():
   #for (u, v, wt) in FG.edges.data('weight'):
        wt = eattr['weight']
        if wt < 0.5:
            print(f"({n}, {nbr}, {wt:.3})")

G = nx.Graph(day="Friday")
G.graph['day'] = "Monday"
print(G.graph)

G = nx.Graph()
G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')
print(G.nodes[1])
G.nodes[1]['room'] = 714
print(G.nodes.data())
"""
"""
G = nx.Graph()
G.add_edge(1, 2, weight=4.7)
G.add_edges_from([(3, 4), (4, 5)], color = 'red')
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
print(G.edges())
G[1][2]['weight'] = 4.2
G.edges[3, 4]['weight'] = 4.21
print(G.edges[1, 2])
"""
"""
G = nx.DiGraph()
G.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
print(G.out_degree(1, weight='weight'))
print(G.degree(1, weight='weight'))
print(list(G.successors(1)))
print(list(G.neighbors(1)))

MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])
print(dict(MG.degree(weight='weight')))
GG = nx.Graph()
for n, nbrs in MG.adjacency():
    for nbr, edict in nbrs.items():
        minvalue = min([d['weight'] for d in edict.value()])
        GG.add_edge(n, nbr, weight = minvalue)
nx.shortest_paths(GG, 1, 3)

G = nx.Graph()
G.add_edges_from([(1,2), (1,3)])
G.add_node("spam")
print(list(nx.connected_components(G)))
# sorted(d for n, d in G.degree())
print(sorted(d for n, d in G.degree()))
print(nx.clustering(G))
sp = dict(nx.all_pairs_shortest_path(G))
print(sp[3])
"""
G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

