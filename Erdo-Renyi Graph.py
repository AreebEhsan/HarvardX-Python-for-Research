import networkx as nx
from scipy.stats import bernoulli
N = 20
p = 0.2



# create empty grapgh
# add all N nodes in the graph
# loop over all pairs of nodes
# add an edge with probabilty p

def er_graph(N,p):
    """Generate an er graph"""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)

    return G


