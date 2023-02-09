import networkx as nx
import matplotlib.pyplot as plt

def kruskal(matrix):
    mst = []
    edges = []
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                edges.append((i, j, matrix[i][j]))
                print()
    edges = sorted(edges, key=lambda x: x[2])
    parent = list(range(n))
    rank = [0] * n

    for edge in edges:
        node1, node2, weight = edge
        root1 = node1
        root2 = node2
        while root1 != parent[root1]:
            root1 = parent[root1]
        while root2 != parent[root2]:
            root2 = parent[root2]
        if root1 != root2:
            mst.append(edge)
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    return mst


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

print(kruskal(matrix))
G = nx.Graph()

# Add edges to the graph
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        if matrix[i][j] != 0:
            G.add_edge(i, j, weight=matrix[i][j])

# Draw the graph
mst = kruskal(matrix)
pos = pos = nx.circular_layout(G)
for edge in mst:
    nx.draw_networkx_edges(G, pos, edgelist=[edge], width=2, edge_color='r')
nx.draw_networkx_nodes(G, pos, node_size=100)
plt.show()