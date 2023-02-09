import networkx as nx
import matplotlib.pyplot as plt
import heapq as hq

def prim(graph, start):
    mst = []                                                        #Liste vide pouvant contenir les aretes des sommets
    T = set()                                                       #Methode servant de prendre en parametre les sommet deja visiter
    heap = [(0, start)]                                             #Tuple prenant en parametre le poid et le sommet de depart
    hq.heapify(heap)                                                #Converti le tuple en priorite

    while heap:
        poid, sommet = hq.heappop(heap)
        if sommet not in T:
            T.add(sommet)
            mst.append((poid, sommet))

            for neighbor, w in graph[sommet].items():
                if neighbor not in T:
                    hq.heappush(heap, (w, neighbor))
    return mst


# Obtenir les informations sur le graphe à partir de l'utilisateur
num_nodes = int(input("Entrez le nombre de nœuds dans le graphe: "))
graph = {}
for i in range(num_nodes):
    node = input("Entrez le nom du nœud: ")
    neighbors = input("Entrez les nœuds voisins séparés par des virgules (ex. A,B,C): ").split(",")
    weights = input("Entrez les poids des arêtes vers les nœuds voisins séparés par des virgules (ex. 1,2,3): ").split(",")
    graph[node] = {}
    for j in range(len(neighbors)):
        graph[node][neighbors[j]] = int(weights[j])

# Obtenir le nœud de départ à partir de l'utilisateur
start = input("Entrez le nœud de départ: ")

# Utiliser l'algorithme de Prim pour obtenir le MST
mst = prim(graph, start)

# Création du graphe
G = nx.Graph(graph)

# Ajout des arêtes du MST au graphe initial
for poid, sommet in mst:
    for neighbor, w in graph[sommet].items():
        if (w, neighbor) in mst:
            G.add_edge(sommet, neighbor, weight=w)

# Dessin du graphe MST avec des lignes épaisses pour les arêtes de l'MST
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=[(sommet, neighbor) for poid, sommet in mst for neighbor, w in graph[sommet].items() if (w, neighbor) in mst], width=2, edge_color='r')
nx.draw_networkx_edges(G, pos, edgelist=[edge for edge in G.edges() if edge not in [(sommet, neighbor) for poid, sommet in mst for neighbor, w in graph[sommet].items() if (w, neighbor) in mst]], width=1, edge_color='k')
nx.draw_networkx_labels(G, pos)

plt.show()
