graph = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
}

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    visited = {vertex: False for vertex in graph}

    for i in range(len(graph)):
        min_distance = float('inf')
        current = None

        for vertex in graph:
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current = vertex

        # no more vertex reachable
        if current is None:
            break

        visited[current] = True
        for neighbor, weight in graph[current].items():
            if not visited[neighbor]:
                newDistance = distances[current] + weight
                if newDistance < distances[neighbor]:
                    distances[neighbor] = newDistance

    return distances

if __name__ == '__main__':
    print(dijkstra(graph, "A"))


    