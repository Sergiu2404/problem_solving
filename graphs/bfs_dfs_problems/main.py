graph_undirected = {
    1: [2, 3],
    2: [1],
    3: [1, 4, 6],
    4: [3, 5],
    5: [4],
    6: [3]
}

graph_directed = {
    1: [2, 3],
    2: [4],
    3: [1, 4],
    4: [3, 5],
    5: []
}

visited = set()
def bfs(graph, start_node):
    queue = [start_node]

    while len(queue) > 0:

        current_node = queue.pop(0)

        if current_node not in visited:
            visited.add(current_node)

            print(f"{current_node} -> ", end="")

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    print("all nodes parsed comppletly")

#bfs(graph_undirected, 1)
#visited.clear()
#bfs(graph_directed, 1)
#visited.clear()


def bfs_find_target(graph, start_node, target_node):
    if start_node == target_node:
        print("start node is the target node")
        return
    queue = [start_node]

    while len(queue) > 0:

        current_node = queue.pop(0)

        if current_node not in visited:
            visited.add(current_node)

            print(f"{current_node} -> ", end="")

            if current_node == target_node:
                print("target node found")
                return

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    print("all nodes parsed comppletly")

#bfs_find_target(graph_undirected, 1, 4)
#visited.clear()

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

def bfs_hasPath(graph, src, dst):
    if src == dst:
        return True

    queue = [src]

    while len(queue) > 0:
        current = queue.pop(0)

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor == dst:
                return True
            if neighbor not in visited:
                queue.append(neighbor)

    return False

#print(bfs_hasPath(graph, 'f', 'k'))
visited.clear()

#CHECK IF THERE EXISTS ANY PATH BETWEEN SRC AND DST FOR AN UNDIRECTED GRAPH WITH GIVEN EDGES
edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
]

def checkUndirectedPath(edges_list, src, dst):
    graph = dict()

    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        graph[edge[0]].append(edge[1])
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[1]].append(edge[0])

    queue = [src]

    while len(queue) > 0:
        current = queue.pop(0)

        if current == dst:
            return True

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor == dst:
                return True
            if neighbor not in visited:
                queue.append(neighbor)


#print(checkUndirectedPath(edges, 'l', 'j'))
visited.clear()


# FIND THE NUMBER OF COMPONENTS IN A GRAPH
graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

def bfs(graph, start_node, visited):
    queue = [start_node]

    while len(queue) > 0:
        current = queue.pop(0)

        if current in visited:
            continue

        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)


def connectedComponentsCount(graph):
    visited = set()
    counter = 0
    for node in graph.keys():
        if node in visited:
            continue

        bfs(graph, node, visited)
        counter+=1

    return counter

#print(connectedComponentsCount(graph))


#SIZE OF LARGEST COMPONENT IN A GRAPH
graph = {
  0: ['8', '1', '5'],
  1: ['0'],
  5: ['0', '8'],
  8: ['0', '5'],
  2: ['3', '4'],
  3: ['2', '4'],
  4: ['3', '2']
}
def count_nodes(graph, start_node, visited):
    queue = [start_node]
    counter = 0

    while len(queue) > 0:
        current = queue.pop(0)

        if current not in visited:
            visited.add(current)
            counter+=1

            for neighbor in graph[current]:
                if int(neighbor) not in visited:
                    queue.append(int(neighbor))

    return counter

def largestComponent(graph):
    graph_node_visited = set()
    largest_component = 0

    for node in graph.keys():
        if node not in graph_node_visited:
            largest_component = max(largest_component, count_nodes(graph, node, graph_node_visited))

    return largest_component

#print(largestComponent(graph))


#PRINT ALL THE COMPONENTS' CONTENT
def content_of_component(graph, start_node, visited):
    queue = [start_node]
    content = []

    while len(queue) > 0:
        current = queue.pop(0)

        if current not in visited:
            visited.add(current)
            content.append(int(current))

            for neighbor in graph[current]:
                if int(neighbor) not in visited:
                    queue.append(int(neighbor))

    return content

def find_components(graph):
    components = []
    visited_nodes = set()

    for node in graph.keys():
        if node not in visited_nodes:
            component = content_of_component(graph, node, visited_nodes)

            if components is []:
                components = [component]
            else:
                components.append(component)

    return components

#print(find_components(graph))

#HARDER
#FIND SHORTEST PATH FORM SRC TO DIST (EACH EDGE COUNTS AS 1)
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

def bfs_shortestPath(edges, src, dst):
    graph = {}

    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = [edge[1]]
        else:
            graph[edge[0]].append(edge[1])
        if edge[1] not in graph:
            graph[edge[1]] = [edge[0]]
        else:
            graph[edge[1]].append(edge[0])

    visited = set()
    if src == dst:
        return 0
    queue = [(src, 0)]

    while len(queue) > 0:
        current_node, current_distance = queue.pop(0)

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor == dst:
                    return current_distance + 1
                if neighbor not in visited:
                    queue.append((neighbor, current_distance + 1))

#print(bfs_shortestPath(edges, 'w', 'z'))

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

def dfs_island(grid, row, col, visited):
    if not(row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])):
        return
    if grid[row][col] == 'W':
        return
    if (row, col) in visited:
        return
    visited.add((row, col))

    dfs_island(grid, row - 1, col, visited)
    dfs_island(grid, row + 1, col, visited)
    dfs_island(grid, row, col - 1, visited)
    dfs_island(grid, row, col + 1, visited)



def islandCount(grid):
    visited = set()
    count = 0

    for rowIdx in range(len(grid)):
        for colIdx in range(len(grid[0])):
            if grid[rowIdx][colIdx] == 'L' and (rowIdx,colIdx) not in visited:
                    count+=1
                    dfs_island(grid, rowIdx, colIdx, visited)
    return count

#print(islandCount(grid))



#FIND MINIMUM ISLAND
def dfs_island_size(grid, row, col, visited):
    if not(row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])) or grid[row][col] == 'W' or (row, col) in visited:
        return 0
    visited.add((row, col))
    counter = 1

    counter+= dfs_island_size(grid, row - 1, col, visited)
    counter+= dfs_island_size(grid, row + 1, col, visited)
    counter+= dfs_island_size(grid, row, col - 1, visited)
    counter+= dfs_island_size(grid, row, col + 1, visited)

    return counter


def minimumIsland(grid):
    visited = set()
    min_size = float('inf')

    for rowIdx in range(len(grid)):
        for colIdx in range(len(grid[0])):
            if (rowIdx, colIdx) not in visited and grid[rowIdx][colIdx] == 'L':
                min_size = min(min_size, dfs_island_size(grid, rowIdx, colIdx, visited))

    return min_size

#print(minimumIsland(grid))