from __future__ import division
import networkx as nx
import random
from ex2 import print_graph_to_file

def get_sum_all_degrees(graph):
    sum = 0;
    for node in graph.nodes:
        sum += graph.degree(node,1)

    return sum

def generate_barabasi_albert_graph(n,m0,m):
    graph = nx.Graph()

    #graph starts with m0 nodes (1 to m0 included)
    for i in range(1,m0+1):
        graph.add_node(i)

    # make graph fully connected
    for n1 in graph.nodes:
        for n2 in graph.nodes:
            if n1 != n2 and not graph.has_edge(n1,n2):
                graph.add_edge(n1,n2)

    #add nodes until graph has # nodes
    while len(graph.nodes) < n:

        curr = len(graph.nodes) + 1
        # get m random nodes that already exist, and add an edge between them and curr
        nodes = list()
        sum_all_degrees =  get_sum_all_degrees(graph)
        while len(nodes) < m:
            j = random.randint(1,len(graph.nodes))
            p_i = graph.degree(j,1) / sum_all_degrees
            target = random.uniform(0,1)
            if not j in nodes and p_i > target:
                nodes.append(j)
        for node in nodes:
            graph.add_edge(node,curr)

    return graph

if __name__ == '__main__':

    g1 = generate_barabasi_albert_graph(1000,3,1)
    print_graph_to_file("ba1.txt", g1)
    g2 = generate_barabasi_albert_graph(1000,6,3)
    print_graph_to_file("ba2.txt", g2)
