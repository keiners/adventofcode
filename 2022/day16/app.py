import re, itertools

def run():
    fileName = "2022/day16/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    valves = {}
    for line in lines:
        valve_ids = re.findall(r'([A-Z][A-Z])', line)
        name = valve_ids[0]
        tunnels = valve_ids[1:]
        flow = int(re.findall(r'\d+', line)[0])
        valves[name] = Valve(name, flow, tunnels)
    dist = find_distance(valves)
    key_valves = {v for v in valves if valves[v].flow > 0}
    a1 = find_best_flow(valves, dist, targets=key_valves)
    print("Answer part 1: " + str(a1))    
    a2 = part2(valves, dist, key_valves)
    print("Answer part 2: " + str(a2))
    
def find_best_flow(valves, dist, current="AA", time=30, visited=set(), targets=set()):
    """DFS"""
    visited = visited | {current}
    targets = targets - visited
    best_flow = 0
    for target in targets:
        time_left = time - dist[current][target] -1
        if time_left > 0:
            flow = valves[target].flow * (time_left)
            flow += find_best_flow(valves, dist, current=target, time=time_left, visited=visited, targets=targets)
            if flow > best_flow: best_flow = flow
    return best_flow

def find_distance(valves):
    """Floyd-Warshall"""
    dist = {a: {b: 999 for b in valves} for a in valves}
    for v in valves.values():
        dist[v.name][v.name] = 0
        for u in v.tunnels:
            dist[v.name][u] = 1
    for k in valves:
        for i in valves:
            for j in valves:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def part2(valves, dist, key_valves):
    # find the best flow rate for every combination of using only half the valves
    # add matching halves to find the best combined flow rate
    combinations = itertools.combinations(key_valves, len(key_valves)//2)
    even_number_of_rooms = len(key_valves) % 2 == 0
    best_flows = {}
    for c in combinations:
        best_flow = find_best_flow(valves, dist, current='AA', time=26, targets=set(c))
        best_flows[frozenset(c)] = best_flow
    if not even_number_of_rooms:
        combinations = itertools.combinations(key_valves, 1 + len(key_valves)//2)
        for c in combinations:
            best_flow = find_best_flow(valves, dist, current='AA', time=26, targets=set(c))
            best_flows[frozenset(c)] = best_flow
    best_combined_flow = 0
    for valves_1,my_flow in best_flows.items():
        valves_2 = frozenset(key_valves - valves_1)
        combined_flow = my_flow + best_flows[frozenset(valves_2)]
        if combined_flow > best_combined_flow:
            best_combined_flow = combined_flow
    return best_combined_flow

class Valve:
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels

run()