

import ex2


if __name__ == '__main__':
    graph = ex2.generate_erdos_renyi_graph(1000, 0.005)
    for node in graph.nodes:
        print graph.degree(node, 1)
