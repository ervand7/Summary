from collections import defaultdict


class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1][vertex2] = weight
            self.graph[vertex2][vertex1] = weight

    def get_neighbors(self, vertex):
        return list(self.graph.get(vertex, {}).keys())

    def get_weight(self, vertex1, vertex2):
        return self.graph.get(vertex1, {}).get(vertex2, None)

    def __str__(self):
        return str(dict(self.graph))


# Example usage:
weighted_graph = WeightedGraph()
weighted_graph.add_vertex('A')
weighted_graph.add_vertex('B')
weighted_graph.add_vertex('C')
weighted_graph.add_vertex('D')

weighted_graph.add_edge('A', 'B', 3)
weighted_graph.add_edge('B', 'C', 5)
weighted_graph.add_edge('C', 'D', 2)
weighted_graph.add_edge('D', 'A', 1)

print("Weighted Graph:")
print(weighted_graph)

print("\nNeighbors of 'B':", weighted_graph.get_neighbors('B'))
print("Weight between 'A' and 'B':", weighted_graph.get_weight('A', 'B'))
