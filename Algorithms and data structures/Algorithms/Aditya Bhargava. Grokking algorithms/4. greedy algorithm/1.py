# Классическая задача о покрытии множества.
# Она NP-полная, решенная за O(n2)

stations = {
    '1': {'id', 'nv', 'ut'},
    '2': {'wa', 'id', 'mt'},
    '3': {'or', 'nv', 'sa'},
    '4': {'nv', 'ut'},
    '5': {'ca', 'az'}
}


def find_best_stations(stations):
    needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'sa', 'az'}
    result = set()
    while needed:
        best_station = None
        covered = set()
        for k, v in stations.items():
            intersection = needed & v
            if len(intersection) > len(covered):
                best_station = k
                covered = intersection

        needed -= covered
        result.add(best_station)

    return result


print(find_best_stations(stations))
