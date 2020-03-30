# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:50:51 2019

@author: makigon
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.sparse.csgraph import connected_components

num = 1000
G= nx.barabasi_albert_graph(num, 3)

count=0
while sum([G.degree(i) for i in range(num)])/num < 6:
    d = [G.degree(i) for i in range(num)]
    G.add_edge(random.randint(0,999),np.argmax(d))
    count += 1
print(count)
print(len(list(G.edges)))

d.sort()
d.reverse()
    

adj_mat = nx.to_numpy_matrix(G)
n, labels = connected_components(adj_mat)
print(n)

g_average = sum([G.degree(i) for i in range(num)])/num
print(g_average)

degree_centers = nx.betweenness_centrality(G)
cent_list = []
for k in degree_centers.values():
    cent_list.append(k)
#plt.rcParams['ps.useafm'] = True
#plt.rcParams['pdf.use14corefonts'] = True
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = '\usepackage{sfmath}' 
plt.hist(cent_list, bins=50, range=(0,0.1))
plt.xlabel('Betweenness centrality', fontsize=14)
plt.ylabel('Number of oscillators',fontsize=14)
plt.show()
nx.draw_networkx(G)
plt.show()
    