import networkx as nx
from networkx.algorithms import bipartite
import csv
import os

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


def write_unicode_nodes_to_csv(rows):
    with open('unicode_nodes.csv', mode='w') as nodes_file:
        writer = csv.writer(nodes_file, delimiter=';')
        row1 = ["Country","Country_ID","Population","bipartite_group"]
        writer.writerow(row1)
        for row in rows:
            writer.writerow(row)
    return


def generate_country_nodes_rows(nodes):
    """
    Nodes that are countries have bipartite attr = 0
    Nodes that are languages have bipartite attr = 1
    """
    rows = list()
    for node in nodes:
        if node[1]['bipartite'] == 0:
            row = [node[0], node[1]['id'], node[1]['pop_total'], node[1]['bipartite']]
        elif node[1]['bipartite'] == 1:
            row = [node[0], node[1]['id'], "-", node[1]['bipartite']]
        rows.append(row)
    return rows


def write_unicode_edges_to_csv(rows):
    with open('unicode_edges.csv', mode='w') as edges_file:
        writer = csv.writer(edges_file, delimiter=';')
        row1 = ['Source','Target','Weight']
        writer.writerow(row1)
        for row in rows:
            writer.writerow(row)
    return


def generate_edges_rows(edges):
    result = list()
    for edge in edges:
        row = [edge[0], edge[1], edge[2]['weight']]
        result.append(row)
    return result


def graph_gen(lines):
    """
    Nodes that are countries have bipartite attr = 0
    Nodes that are languages have bipartite attr = 1
    """
    g = nx.Graph()

    for line in lines:
        g.add_node(line[0], bipartite=0, id=line[1], pop_total=line[4])
        g.add_node(line[2], bipartite=1, id=line[3])
        g.add_edge(line[0], line[2], weight=line[5])

    return g


def write_to_files():
    lines = read_csv('raw_unicode.csv')
    graph = graph_gen(lines)
    write_unicode_edges_to_csv(generate_edges_rows(graph.edges(data=True)))
    write_unicode_nodes_to_csv(generate_country_nodes_rows(graph.nodes(data=True)))

if __name__ == '__main__':
    # lines = read_csv("raw_unicode.csv")
    # g = graph_gen(lines)
    # print "nodes: {}".format(len(g.nodes))
    # print "edges: {}".format(len(g.edges))
    write_to_files()
