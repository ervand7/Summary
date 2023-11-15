# Below is a simple implementation of a directed graph in Python using an
# adjacency list representation. In this implementation, we use a dictionary
# to represent the graph, where each vertex is a key, and the corresponding
# value is a list of vertices to which the key vertex has outgoing edges.

class DirectedGraph:
    def __init__(self):
        # Using a dictionary to represent the adjacency list
        self.graph = {}

    def add_vertex(self, vertex):
        # Add a new vertex to the graph
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start, end):
        # Add a directed edge from start to end
        if start in self.graph and end in self.graph:
            self.graph[start].append(end)

    def get_neighbors(self, vertex):
        # Get the neighbors (vertices with incoming edges) of a given vertex
        return self.graph.get(vertex, [])

    def __str__(self):
        # String representation of the graph
        return str(self.graph)


# Example usage:
graph = DirectedGraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")

print("Graph:")
print(graph)

print("\nNeighbors of B:", graph.get_neighbors("B"))

# {'A': ['B'], 'B': ['C'], 'C': ['D'], 'D': ['A']}

# Neighbors of B: ['C']