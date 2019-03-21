import networkx as nx
import random
from ex2 import print_graph_to_file

def generate_barabasi_albert_graph(n,m0,m):
    graph = nx.Graph()

    #graph starts with m0 nodes (1 to m0 included)
    for n in range(1,m0+1):
        graph.add_node(n)

    # make graph fully connected
    for n1 in graph.nodes:
        for n2 in graph.nodes:
            if n1 != n2 and not graph.has_edge(n1,n2):
                graph.add_edge(n1,n2)

    #add nodes until graph has # NOTE:  nodes
    while len(graph.nodes) < n:
        curr = len(graph.nodes) + 1
        print "adding node %d " % curr
        # get m random nodes that already exist, and add an edge between them and curr
        nodes = list()
        while(len(nodes) < m):
            j = random.randint(0,len(graph.nodes))
            if not j in nodes:
                nodes.append(j)
        # add the m edges
        for node in nodes:
            graph.add_edge(node,curr)




    return graph

if __name__ == '__main__':

    #l = list(x for x in range(0,10))
    #print l

    g1 = generate_barabasi_albert_graph(1000,3,1)
    #print_graph_to_file("ba1.txt", g1)
    #g2 = generate_barabasi_albert_graph(1000,6,3)
    #print_graph_to_file("ba2.txt", g2)
