import networkx as nx
import matplotlib.pyplot as plt

# Création du graphe
G = nx.Graph()

# Ajout des arêtes au graphe
#edges = [('A','B',1), ('A','C',2), ('B','C',2), ('B','D',5), ('C','E',1), ('C','G',3), ('D','E',3),('D','F',1),
#         ('E','F',3), ('F','G',2),('F','H',3),('F','I',1),('G','I',5),('H','I',2)]
edges = [('A','B',800), ('A','E',2000), ('A','D',400),
         ('B','C',900), ('B','D',700), ('B','G',1600), ('B','F',500),  ('B','E',700), ('B','I',1300),
         ('C','E',200), ('C','I',2300),
         ('D','E',800),('D','G',1000),
         ('E','F',300), ('E','H',600),
         ('F','H',300),
         ('G','H',1100), ('G','I',1300)]

for edge in edges:
    G.add_edge(edge[0], edge[1], poids = edge[2])

# Dessin du graphe
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
#plt.show()

# Utilisation de l'algorithme de Prim pour obtenir le MST
mst = nx.minimum_spanning_tree(G)

# Dessin du graphe avec les coûts des arêtes
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'poids')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Dessin du graphe
nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), width=2, edge_color='r')
nx.draw_networkx_nodes(G, pos, node_size=100)
plt.show()