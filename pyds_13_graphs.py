class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store adjacency list

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = [] # create a key in the dictionary for the 

    def add_edge(self, u, v, bidirectional=True):
        self.graph[u].append(v)
        if bidirectional:
            self.graph[v].append(u)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# Example Usage
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.display()

#############################################
class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, bidirectional=True):
        self.matrix[u][v] = 1
        if bidirectional:
            self.matrix[v][u] = 1

    def display(self):
        for row in self.matrix:
            print(row)

# Example Usage
g = GraphMatrix(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.display()


##################################################################
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, graph[node],end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example Graph (Adjacency List)
graph = {
    1: [2, 3, 6],
    2: [1, 4, 5],
    3: [1,5,6],
    4: [2,5],
    5: [2,3,4],
    6: [1,3]
}

print("BFS Traversal:")
bfs(graph, 1)

############################################
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

print("\nDFS Traversal:")
dfs(graph, 1)

###############################################
import heapq

def dijkstra(graph, start):
    """ 
    find the shortest path from a start node
    to all other nodes in a weighted graph 
    """
    min_heap = [(0, start)]  
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while min_heap:
        current_distance, node = heapq.heappop(min_heap)

        for neighbor, weight in graph[node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# Example Graph (Weighted Adjacency List)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print("Shortest distances from A:", dijkstra(graph, 'A'))
############################################
def has_cycle(graph, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited and has_cycle(graph, neighbor, visited, rec_stack):
            return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(node)
    return False

def detect_cycle(graph):
    visited = set()
    rec_stack = set()
    for node in graph:
        if node not in visited:
            if has_cycle(graph, node, visited, rec_stack):
                return True
    return False

# Example Graph (Directed)
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

print("Cycle Detected:", detect_cycle(graph))
