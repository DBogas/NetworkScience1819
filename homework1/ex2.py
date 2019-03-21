import random

import networkx as nx

p1 = 0.0001
p2 = 0.005


def generate_erdos_renyi_graph(size, prob):
    graph = nx.Graph()
    nodes = list(x for x in range(1,size+1))
    graph.add_nodes_from(nodes)
    # triangular superior matrix (undirected graph)
    for i in graph.nodes:
        for j in graph.nodes:
            # not sure if < or <= here
            if i != j and random.uniform(0, 1) < prob:
                graph.add_edge(i,j)

    return graph


def print_graph_to_file(filename,graph):

    file = open(filename, "w+")

    file.write("%d\n" % len(graph.nodes))

    for edge in graph.edges:
        file.write("%d %d\n" % (edge[0], edge[1]))

    file.close()

    return


if __name__ == '__main__':

    size = 1000
    erdos_renyi_1 = generate_erdos_renyi_graph(size, p1)
    erdos_renyi_2 = generate_erdos_renyi_graph(size, p2)

    print 0 in erdos_renyi_1.nodes
    print 0 in erdos_renyi_2.nodes


    print_graph_to_file("random1.txt", erdos_renyi_1)
    print_graph_to_file("random2.txt", erdos_renyi_2)
