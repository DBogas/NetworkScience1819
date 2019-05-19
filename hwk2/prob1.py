import networkx as nx
from networkx.algorithms import bipartite
import csv

def read_csv(filepath):
    res = list()
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            res.append(row)
            line_count += 1
        print "Read {} lines".format(line_count)
        return res

def interpretation():
    lines = read_csv('raw_unicode.csv')
    for line in lines:
        print "In {}, {} is spoken by {} people, which is {}% of the population".format(line[0],line[2],line[4],line[5])
    print "\n"

def read_countries_from_lines(lines):
    res = list()
    for line in lines:
        if line[0] not in res:
            res.append(line[0])
    return res

def read_languages_from_lines(lines):
    res = list()
    for line in lines:
        if line[2] not in res:
            res.append(line[2])
        return res



def graph_gen(lines, countries, languages):
    """
    Nodes that are countries have bipartite attr = 0
    Nodes that are languages have bipartite attr = 1
    """
    graph = nx.Graph()

    graph.add_nodes_from(countries, bipartite=0)

    graph.add_nodes_from(languages, bipartite=1)

    for line in lines:
        graph.add_edge(line[0], line[2], weight=line[5])

    for node in graph.nodes(data=True):
        print node
    #top_nodes = {n for n, d in graph.nodes(data=True) if d['bipartite'] == 0}
    #bottom_nodes = set(graph) - top_nodes

    #print(round(bipartite.density(graph, bottom_nodes), 2))


    return graph



if __name__ == '__main__':
    lines = read_csv('raw_unicode.csv')
    countries = read_countries_from_lines(lines)
    languages = read_languages_from_lines(lines)

    graph = graph_gen(lines, countries, languages)
