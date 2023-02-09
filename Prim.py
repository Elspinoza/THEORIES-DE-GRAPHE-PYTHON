# import networkx as nx
# import matplotlib.pyplot as plt
# #La bibliotheque permet d'etablir un tat de priorite en pyhton
# import heapq as hq
#
# #Definition de la fonction qui prend en parametre un graphe et un sommet de depart
# def prim(graph, start):
#     mst = []                                                        #Liste vide pouvant contenir les aretes des sommets
#     T = set()                                                       #Methode servant de prendre en parametre les sommet deja visiter
#     heap = [(0, start)]                                             #Tuple prenant en parametre le poid et le sommet de depart
#     hq.heapify(heap)                                                #Converti le tuple en priorite
#
#
#     while heap:
#         poid, sommet = hq.heappop(heap)
#         if sommet not in T:
#             T.add(sommet)
#             mst.append((poid, sommet))
#
#             for neighbor, w in graph[sommet].items():
#                 if neighbor not in T:
#                     hq.heappush(heap, (w, neighbor))
#     return mst
#
# # Exemple de graphe:
# graph = {
#     'A': {'B': 1, 'C': 2},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 2, 'B': 2, 'E': 1, 'G': 3},
#     'D': {'B': 5, 'E': 3, 'F': 1},
#     'E': {'C': 1, 'D': 3, 'F': 3},
#     'F': {'E': 3, 'D': 1, 'G': 4, 'H': 3, 'I': 1},
#     'G': {'C': 3, 'F': 4, 'I': 5},
#     'H': {'F': 3, 'I': 2},
#     'I': {'G': 5, 'H': 2, 'F': 1}
# }
#
# print(prim(graph, 'A'))
#
#
# # Création du graphe
# G = nx.Graph(graph)
#
# # Dessin du graphe
# nx.draw(G, with_labels=True)
# plt.show()
#
#
# #Affichage du resultat en graphef
#
# # Utilisation de l'algorithme de Prim pour obtenir le MST
# mst = prim(graph, 'A')
#
# # Ajout des arêtes du MST au graphe initial
# for poid, sommet in mst:
#     for neighbor, w in graph[sommet].items():
#         if (w, neighbor) in mst:
#             G.add_edge(sommet, neighbor, weight=w)
#
# # Dessin du graphe MST avec des lignes épaisses pour les arêtes de l'MST
# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G, pos)
# nx.draw_networkx_edges(G, pos, edgelist=[(sommet, neighbor) for poid, sommet in mst for neighbor, w in graph[sommet].items() if (w, neighbor) in mst], width=2, edge_color='r')
# nx.draw_networkx_edges(G, pos, edgelist=[edge for edge in G.edges() if edge not in [(sommet, neighbor) for poid, sommet in mst for neighbor, w in graph[sommet].items() if (w, neighbor) in mst]], width=1, edge_color='k')
# nx.draw_networkx_labels(G, pos)
#
# plt.show()

import networkx as nx
import matplotlib.pyplot as plt

# Création du graphe
G = nx.Graph()

# Ajout des arêtes au graphe
edges = [('A','B',1), ('A','C',2), ('B','C',2), ('B','D',5), ('C','E',1), ('C','G',3), ('D','E',3),('D','F',1),
         ('E','F',3), ('F','G',2),('F','H',3),('F','I',1),('G','I',5),('H','I',2)]

for edge in edges:
    G.add_edge(edge[0], edge[1], poids = edge[2])

# Dessin du graphe
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()

# Utilisation de l'algorithme de Prim pour obtenir le MST
mst = nx.minimum_spanning_tree(G)

# Dessin du graphe
nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), width=2, edge_color='g')
nx.draw_networkx_nodes(G, pos, node_size=100)
plt.show()