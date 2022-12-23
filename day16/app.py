import re

def run():
    fileName = "day16/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    valves = {}
    for line in lines:
        valveCodes = re.findall(r'([A-Z][A-Z])', line)
        name = valveCodes[0]
        tunnels = valveCodes[1:]
        flow = int(re.findall(r'\d+', line)[0])
        valves[name] = Valve(name, flow, tunnels)
    
    dist = find_dist(valves)
    key_rooms = {v for v in valves if valves[v].flow > 0 or v == "AA"}
    answer_part_1 = find_best_flow(valves, dist, targets=key_rooms)
    print("Answer part 1: " + str(answer_part_1))
    
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
    
def find_dist(valves):
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

class Valve:
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels
        
run()