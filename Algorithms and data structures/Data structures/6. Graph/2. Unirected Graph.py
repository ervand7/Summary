class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

    def __str__(self):
        return str(self.graph)


# Example usage:
undirected_graph = UndirectedGraph()
undirected_graph.add_vertex('A')
undirected_graph.add_vertex('B')
undirected_graph.add_vertex('C')
undirected_graph.add_vertex('D')

undirected_graph.add_edge('A', 'B')
undirected_graph.add_edge('B', 'C')
undirected_graph.add_edge('C', 'D')
undirected_graph.add_edge('D', 'A')

print("Undirected Graph:")
print(undirected_graph)

print("\nNeighbors of 'B':", undirected_graph.get_neighbors('B'))

# {'A': ['B', 'D'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'A']}

# Neighbors of 'B': ['A', 'C']
