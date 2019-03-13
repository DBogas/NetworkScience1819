import random

import networkx as nx

p1 = 0.0001
p2 = 0.005


def generate_erdos_renyi_graph(size, prob):
    graph = nx.Graph()
    nodes = (x for x in range(0,size))
    graph.add_nodes_from(nodes)

    # triangular superior matrix (undirected graph)
    for i in range(0, len(graph.nodes)):
        for j in range(i+1,len(graph.nodes)):
            # not sure if < or <= here
            if random.uniform(0, 1) < prob:
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



    print_graph_to_file("random1.txt", erdos_renyi_1)
    print_graph_to_file("random2.txt", erdos_renyi_2)