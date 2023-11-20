# O(V + E)

# Поиск в ширину отвечает на 2 вопроса:
#  - существует ли путь от узла A к узлу B
#  - как выглядит кратчайший путь от узла A к узлу B

# The provided algorithm performs a breadth-first search (BFS) on a graph to
# find a person with a name ending in 'm' (a mango seller). Let's analyze the
# time complexity (Big O) of this algorithm:
#
# - **Vertices (V):** The number of vertices in the graph.
# - **Edges (E):** The number of edges in the graph.
#
# The BFS algorithm visits each vertex and each edge once, making the time
# complexity of BFS O(V + E).
#
# In the given algorithm:
# - The `while` loop runs until the `queue` is empty, which takes O(V) time
# in the worst case.
# - Within the loop, each vertex is processed once, and each edge is examined
# once, taking O(E) time.
#
# Therefore, the overall time complexity is O(V + E), where V is the number of
# vertices and E is the number of edges in the graph.

from collections import deque

# create a graph
graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}


def is_seller(name: str):
    if name[-1] == 'm':
        return True
    return False


def search(name):
    queue = deque()
    queue += graph[name]
    searched = []
    while queue:
        person = queue.popleft()
        if person not in searched:
            if is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                queue += graph[person]
                searched.append(person)
    return False


search('you')
