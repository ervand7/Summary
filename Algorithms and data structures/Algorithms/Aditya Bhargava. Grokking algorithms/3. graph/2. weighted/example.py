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

import heapq


def dijkstra(graph, start, finish):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    predecessors = {node: None for node in graph}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current = finish
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]

    return path, distances[finish]


# Example usage
graph = {
    'start': {'b': 5, 'c': 2},
    'b': {'d': 4, 'e': 2},
    'c': {'b': 8, 'e': 7},
    'd': {'finish': 3},
    'e': {'d': 6, 'finish': 1},
    'finish': {},
}

start_node = 'start'
finish_node = 'finish'
shortest_path, shortest_distance = dijkstra(graph, start_node, finish_node)
print(f"Shortest path from {start_node} to {finish_node}: {shortest_path}")
print(f"Shortest distance: {shortest_distance}")
