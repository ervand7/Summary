graph = {
    'a': {
        'fin': 1
    },
    'b': {
        'a': 3,
        'fin': 5
    },
    'fin': {

    },
    'start': {
        'a': 6,
        'b': 2
    }
}

costs = {
    'a': 6,
    'b': 2,
    'fin': float('inf')
}

parents = {
    'a': 'start',
    'b': 'start',
    'in': None
}


def dijkstra():
    result = []

    def find_lowest_cost_node(costs):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in result:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        result.append(node)
        node = find_lowest_cost_node(costs)

    return result


print(dijkstra())  # ['b', 'a', 'fin']
