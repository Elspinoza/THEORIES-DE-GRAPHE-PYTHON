# import matplotlib.pyplot as plt
# import numpy as np
#
# def color_graph_welsh_powell(graph, colors):
#     nodes = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)
#     node_color = {}
#     for node in nodes:
#         available_colors = [True] * len(colors)
#         for neighbor in graph[node]:
#             if neighbor in node_color:
#                 color = node_color[neighbor]
#                 available_colors[color] = False
#         for color, available in enumerate(available_colors):
#             if available:
#                 node_color[node] = color
#                 break
#     return node_color
#
# graph = {
#     'A': ['B', 'C', 'E'],
#     'B': ['A', 'C', 'D', 'F'],
#     'C': ['A', 'B', 'D', 'E'],
#     'D': ['B', 'C', 'F', 'E'],
#     'E': ['A', 'C', 'D', 'F'],
#     'F': ['B', 'D', 'E']
# }
#
# colors = ['red', 'green', 'blue', 'yellow', 'black']
# node_color = color_graph_welsh_powell(graph, colors)
#
# def plot_graph(graph, node_color):
#     colors = ['red', 'green', 'blue', 'yellow', 'black']
#     nodes = list(graph.keys())
#     x = [i for i, _ in enumerate(nodes)]
#     y = np.random.uniform(low=-3, high=3, size=(len(nodes),))
#     for i, node in enumerate(nodes):
#         plt.scatter(x[i], y[i], color=colors[node_color[node]])
#         for neighbor in graph[node]:
#             j = nodes.index(neighbor)
#             plt.plot([x[i], x[j]], [y[i], y[j]], color='gray')
#     plt.xticks(x, nodes)
#     plt.show()
#
# node_color = color_graph_welsh_powell(graph, colors)
# plot_graph(graph, node_color)

import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

edges = [('B', 'P', 800), ('B', 'N', 400), ('B', 'St', 2000), ('N', 'T', 1000), ('N', 'P', 700), ('N', 'St', 1800),
         ('T', 'P', 1600), ('T', 'L', 1100),
         ('T', 'M', 1300), ('M', 'P', 1300), ('M', 'S', 2300), ('L', 'D', 300), ('L', 'St', 600), ('D', 'P', 500),
         ('D', 'St', 300), ('P', 'S', 900), ('P', 'St', 700), ('S', 'St', 200)]

# Fonction pour colorier les sommets du graphe en utilisant le nombre de couleurs spécifié
def color_graph(edges, num_colors):
    # Créer un dictionnaire par défaut qui contient une liste vide pour chaque sommet
    graph = defaultdict(list)
    for edge in edges:
        # Remplir le dictionnaire avec les voisins de chaque sommet
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Dictionnaire pour stocker la couleur attribuée à chaque sommet
    colors = {}

    for node in graph:
        # Ensemble de couleurs disponibles
        available_colors = set(range(num_colors))
        # Pour chaque voisin du sommet actuel
        for neighbor in graph[node]:
            # Si le voisin a déjà une couleur attribuée, la supprimer de la liste des couleurs disponibles
            if neighbor in colors:
                available_colors.discard(colors[neighbor])
        # Attribuer la couleur minimale disponible au sommet actuel
        colors[node] = min(available_colors)

    # Renvoyer les couleurs attribuées à chaque sommet
    return colors

# Afficher les couleurs attribuées à chaque sommet en utilisant 5 couleurs
print(color_graph(edges, 5))
colors = color_graph(edges, 5)

G = nx.Graph()
for edge in edges:
    G.add_edge(edge[0], edge[1], poids=edge[2])

pos = nx.circular_layout(G)
node_colors = [colors[node] for node in G.nodes()]
nx.draw(G, pos, node_color=node_colors, with_labels=True)

# Dessin du graphe avec les coûts des arêtes
edge_labels = nx.get_edge_attributes(G, 'poids')

plt.show()