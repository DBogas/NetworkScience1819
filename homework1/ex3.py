# compute the size of the random networks we generated

import networkx as nx

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
def find_connected_components(graph):

    node_queue = list() # node list so BFS progresses
    visited_nodes = list() # set of visited nodes
    nodes_to_visit = list(graph.nodes) # list of nodes to visit (guarantees order since we append)
    components = list() # list of connected components' sizes
    comp = list()
    node_queue.append(nodes_to_visit.pop(0))

    while len(nodes_to_visit) > 0:
        currnode = node_queue.pop(0)
        comp.append(currnode)

        graph.nodes[currnode]['visited'] = True
        visited_nodes.append(currnode)

        # add neighbours to queue if not visited or already in queue to get visited
        neighbours = nx.all_neighbors(graph, currnode)
        for neighbour in neighbours:
            if not neighbour in node_queue and graph.nodes[neighbour]['visited'] == False:
                print currnode," knows ", neighbour, " is not visited or in queue"
                node_queue.append(neighbour)
                nodes_to_visit.remove(neighbour)

        # end of component
        if len(node_queue) == 0 and len(nodes_to_visit) > 0:
            node_queue.append(nodes_to_visit.pop(0))
            components.append(comp)


    print len(visited_nodes)

    return False



def calculate_giant_component_size(graph):

    connected_components = find_connected_components(graph)
    return 1

if __name__ == '__main__':
    #graph1 = read_graph_from_file("random1.txt")
    #components1  = find_connected_components(graph1)

    graph2 = read_graph_from_file("random2.txt")
    calculate_giant_component_size(graph2)



