# Алгоритм Дейкстры для нахождения кратчайших путей во взвешенном графе имеет
# следующие шаги:
#
# 1. Найти узел с наименьшей стоимостью. Это узел, до которого можно добраться
# за минимальное время
#
# 2. Проверить, существует ли более дешевый путь к соседям этого узла. И если
# существует, обновить их стоимости.
#
# 3. Проверять, пока это не будет сделано для всех узлов графа.
#
# 4. Вычислить итоговый путь.
#
# Эти шаги помогают пошагово находить кратчайший путь от начального узла ко всем
# остальным узлам в графе.


class Dijkstra:
    def __init__(self, graph: dict, costs: dict, parents: dict):
        self.graph = graph
        self.costs = costs
        self.parents = parents
        self.result = []

    def get_list(self) -> list:
        while True:
            node = self._find_lowest_cost_node(self.costs)
            if node is None:
                return self.result

            cost = self.costs[node]
            neighbors = self.graph[node]
            for neighbor in neighbors.keys():
                new_cost = cost + neighbors[neighbor]
                if self.costs[neighbor] > new_cost:
                    self.costs[neighbor] = new_cost
                    self.parents[neighbor] = node
            self.result.append(node)

    def _find_lowest_cost_node(self, costs: dict) -> str:
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in self.result:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node


graph = {
    'start': {
        'a': 6,
        'b': 2
    },
    'a': {
        'finish': 1
    },
    'b': {
        'a': 3,
        'finish': 5
    },
    'finish': {
    },
}

costs = {  # таблица стоимостей, которая будет обновляться
    'a': 6,
    'b': 2,
    'finish': float('inf')
}

parents = {  # таблица родителей, которая будет обновляться
    'a': 'start',
    'b': 'start',
}

d = Dijkstra(graph, costs, parents)
print(d.get_list())  # ['b', 'a', 'finish']
