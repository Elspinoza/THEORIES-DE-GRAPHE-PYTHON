from collections import defaultdict
import heapq

def dijkstra(graph, start, end):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    heap = [(0, start)]
    previous = defaultdict(lambda: None)
    while heap:
        (dist, current) = heapq.heappop(heap)
        if current == end:
            break
        for neighbor in graph[current]:
            new_distance = dist + graph[current][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current
                heapq.heappush(heap, (new_distance, neighbor))
    return (distances, previous)

def shortest_path(graph, start, end):
    (distances, previous) = dijkstra(graph, start, end)
    path = []
    current = end
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()
    return path

graph = defaultdict(dict)
edges = [("A", "B", 5), ("A", "C", 9), ("A", "F", 14), ("B", "C", 10),
         ("B", "D", 1), ("C", "D", 12), ("C", "F", 2), ("D", "E", 16),
         ("E", "F", 9)]
for (start, end, cost) in edges:
    graph[start][end] = cost
    graph[end][start] = cost

print(f"le plus court chemin du point A au point E est{shortest_path(graph, 'A', 'E')}")
