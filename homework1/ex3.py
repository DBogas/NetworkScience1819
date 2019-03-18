# compute the size of the random networks we generated

import networkx as nx
import time

def read_graph_from_file(filename):

    #read from file
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    size = int(lines[0])
    nodes = (x for x in range(0, size))
    graph = nx.Graph()

    #add nodes
    for node in nodes:
        graph.add_node(node,visited=False)


    # read and add edges
    for i in range(1, len(lines)):
        x,y = lines[i].split()
        graph.add_edge(int(x),int(y))

    return graph


# implementing BFS here
# sauces:
#   https://en.wikipedia.org/wiki/Breadth-first_search
#   https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
def calculate_giant_component_size(graph):

    time_start = int(round(time.time() * 1000))

    components = list()
    node_queue = list()
    visitedNodes = set()
    nodes_to_visit = list(graph.nodes)
    root = nodes_to_visit.pop(0)
    currNode = root
    currComp = list()
    sizes = list()
    node_queue.append(currNode)

    while len(visitedNodes) < len(list(graph.nodes)):

        currNode = node_queue.pop(0)
        currComp.append(currNode)
        visitedNodes.add(currNode)
        neighbours = nx.all_neighbors(graph,currNode)

        for n in neighbours:
            if n not in visitedNodes and n not in node_queue and n in nodes_to_visit:
                node_queue.append(n)
                nodes_to_visit.remove(n)

        # component end
        if len(node_queue) == 0:
            if len(nodes_to_visit) > 0:
                node_queue.append(nodes_to_visit.pop(0))
            components.append(currComp)
            sizes.append(len(currComp))
            currComp = list()

    time_end = int(round(time.time() * 1000))
    #print "\t%d nodes \n\tin %d ms\n\twith giant component having size %d" % (len(visitedNodes),time_end-time_start,max(sizes))
    return max(sizes)

if __name__ == '__main__':
    graph1 = read_graph_from_file("random1.txt")
    print "Graph 1 has giant component size: %d " % calculate_giant_component_size(graph1)

    graph2 = read_graph_from_file("random2.txt")
    print "Graph 2 has giant component size: %d " % calculate_giant_component_size(graph2)
