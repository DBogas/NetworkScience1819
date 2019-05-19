import networkx
import matplotlib.pyplot as plt
import numpy

import ex2
import ex3


n_nodes = 1000
s_prob = 0.0001
f_prob = 0.005
step_prob = 0.0001

res_x = list()
res_y = list()


# plotting code adapter from here:
#https://stackoverflow.com/questions/21519203/plotting-a-list-of-x-y-coordinates-in-python-matplotlib

#Show a plot of your results, with the X axis representing p
#and the Y axis representing the size of the giant component.
if __name__ == '__main__':

    steps = numpy.arange(s_prob, f_prob+step_prob, step_prob)
    print "Using %d steps." % len(steps)
    print "Working..."
    for step in steps:
        graph = ex2.generate_erdos_renyi_graph(n_nodes,step)
        giant_comp_size = ex3.calculate_giant_component_size(graph)
        res_x.append(step)
        res_y.append(giant_comp_size)
    print "Done, plotting."
    plt.scatter(res_x,res_y)
    #plt.plot(res_x,res_y)
    plt.show()
