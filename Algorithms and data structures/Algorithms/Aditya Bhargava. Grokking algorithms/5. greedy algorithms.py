_stations = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'sa'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}


def find_best_stations(stations):
    states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'sa', 'az'}
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_station)

    return final_stations


print(find_best_stations(_stations))
