import ex3
import matplotlib.pyplot as plt

def degree_dist_cummulative_binning(graph):
    dgs = list()
    for node in graph.nodes:
        dgs.append((node,graph.degree(node,1)))

    cummulative_dgs = list()
    for i in range(1, len(graph.node) + 1):
        sum = 0
        for pair in dgs:
            if(pair[1] >= i):
                sum += 1
        cummulative_dgs.append((i,sum))

    # filter pairs (dg,v) where the number of nodes v with degree dg is 0
    return [x for x in cummulative_dgs if not x[1] == 0]


if __name__ == '__main__':

    #g1 = ex3.read_graph_from_file("ba1.txt")
    g2 = ex3.read_graph_from_file("ba2.txt")

    #dgs = degree_dist_cummulative_binning(g1)
    dgs = degree_dist_cummulative_binning(g2)

    dgs_x = list()
    dgs_y = list()
    for d in dgs:
        dgs_x.append(d[0])
        dgs_y.append(d[1])
    plt.scatter(dgs_x,dgs_y)
    plt.show()
