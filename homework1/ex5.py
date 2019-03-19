import networkx as nx
from ex2 import print_graph_to_file

def generate_barabasi_albert_graph(n,m0,m):
    graph = nx.Graph()
    #graph starts with m0 nodes
    for n in range(0,m0):
        graph.add_node(m0)
    # make graph fully connected
    for n1 in graph.nodes:
        for n2 in graph.nodes:
            if n1 != n2 and not graph.has_edge(n1.n2):
                graph.add_edge(n1,n2)
    return graph

if __name__ == '__main__':

    g1 = generate_barabasi_albert_graph(1000,3,1)
    print_graph_to_file("ba1.txt", g1)
    g2 = generate_barabasi_albert_graph(1000,6,3)
    print_graph_to_file("ba2.txt", g2)
