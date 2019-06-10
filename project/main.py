import os
import csv
import networkx as nx

PATH = "gameofthrones/data/"
seasons = [1,2,3,4,5,6,7]
types = ["edges","nodes"]

def get_season_graph(season):
    """
    Generates a graph for a specific season
    """
    fc_edges = get_file_contents("edges",season)
    fc_nodes = get_file_contents("nodes",season)

    graph = nx.Graph()

    # id (caps), label (normal)
    for c_node in fc_nodes:
        print c_node
        graph.add_node(c_node[0], name=c_node[1])
    # source, target, weight, season
    for c_edge in fc_edges:
        print c_edge
        graph.add_edge(c_edge[0], c_edge[1], weight=c_edge[2])

    return graph

def get_file_contents(type, season):

    if type == "edges":
        str = "got-s{}-edges.csv".format(season)
    elif type == "nodes":
        str = "got-s{}-nodes.csv".format(season)
    contents = list()
    for root, dirs, files in os.walk(PATH, topdown=False):
        for file in files:
            if file == str:
                with open(file) as csv_target:
                    csv_reader = csv.reader(csv_target, delimiter=',')
                    line_counter=0
                    for row in csv_reader:
                        contents.append(row)
                        line_counter += 1
    return contents


if __name__ == '__main__':
    get_season_graph(1)
