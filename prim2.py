import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def Prime(Graphe):
    T = []
    n = len(Graphe)
    plusProche = []
    distanceMin = []

    for i in range(0, n):
        plusProche.append(0)
        distanceMin.append(0)

    for i in range(1, n):
        plusProche[i] = 0
        distanceMin[i] = Graphe[i][0]

    for i in range(0, n - 1):
        min = None
        for j in range(1, n):
            if ((min and distanceMin[j] and 0 <= distanceMin[j] < min) or (not min and 0 <= distanceMin[j])):
                min = distanceMin[j]
                k = j

        T.append((k, plusProche[k]))
        print(T)

        distanceMin[k] = -1
        distanceMin[plusProche[k]] = -1

        for j in range(1, n):
            if ((distanceMin[j] and Graphe[k][j] and Graphe[k][j] < distanceMin[j]) or not distanceMin[j]):
                distanceMin[j] = Graphe[k][j]
                distanceMin[k] = Graphe[j][k]

                plusProche[j] = k
                plusProche[k] = j

    return T


matrix = [[0, 3, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0],
          [3, 0, 0, 0, 3, 6, 0, 0, 0, 0, 0, 0],
          [5, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 0],
          [4, 0, 2, 0, 1, 0, 0, 5, 0, 0, 0, 0],
          [0, 3, 0, 0, 0, 2, 0, 0, 4, 0, 0, 0],
          [0, 6, 0, 0, 2, 0, 0, 0, 0, 5, 0, 0],
          [0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 6, 0],
          [0, 0, 0, 5, 0, 0, 3, 0, 6, 0, 7, 0],
          [0, 0, 0, 0, 4, 0, 0, 6, 0, 3, 0, 5],
          [0, 0, 0, 0, 0, 5, 0, 0, 3, 0, 0, 9],
          [0, 0, 0, 0, 0, 0, 6, 7, 0, 0, 0, 8],
          [0, 0, 0, 0, 0, 0, 0, 0, 5, 9, 8, 0]]

Prime(matrix)

G = nx.Graph()

# Add edges to the graph
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        if matrix[i][j] != 0:
            G.add_edge(i, j, weight=matrix[i][j])

# Draw the graph
mst = Prime(matrix)
pos = nx.circular_layout(G)
for edge in mst:
    nx.draw_networkx_edges(G, pos, edgelist=[edge], width=2, edge_color='g')
    nx.draw_networkx_nodes(G, pos, node_size=100)
plt.show()