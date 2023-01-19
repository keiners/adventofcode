def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day15/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    risk_map, cost_map = get_maps(lines)
    end_pos = len(lines[0])-1 + 1j * (len(lines)-1)
    
    queue = {0:cost_map[0]}
    visited = set()
    while len(queue) > 0:
        pos = min(queue, key=queue.get)
        current_cost = queue.pop(pos)
        visited.add(pos)
        for n in [pos+mv for mv in [1,-1,1j,-1j] if (pos+mv) in risk_map and (pos+mv) not in visited]:
            new_cost = risk_map[n] + current_cost
            if n == end_pos:
                return new_cost
            if cost_map[n] > new_cost:
                cost_map[n] = new_cost
                queue[n] = cost_map[n]
    
    return cost_map[end_pos]

def part2(lines):
    risk_map, cost_map = get_maps_extended(lines)
    end_pos = 5*len(lines)-1 + 1j * (5*len(lines)-1)
    
    queue = {0:cost_map[0]}
    visited = set()
    while len(queue) > 0:
        pos = min(queue, key=queue.get)
        current_cost = queue.pop(pos)
        visited.add(pos)
        for n in [pos+mv for mv in [1,-1,1j,-1j] if (pos+mv) in risk_map and (pos+mv) not in visited]:
            new_cost = risk_map[n] + current_cost
            if n == end_pos:
                return new_cost
            if cost_map[n] > new_cost:
                cost_map[n] = new_cost
                queue[n] = cost_map[n]
    return cost_map[end_pos]

def get_maps(lines):
    risk_map = {}
    cost_map = {}
    for y,line in enumerate(lines):
        for x,value in enumerate(line):
            risk_map[x + 1j * y] = int(value)
            cost_map[x + 1j * y] = 100000
    cost_map[0] = 0
    return risk_map, cost_map

def get_maps_extended(lines):
    risk_map = {}
    cost_map = {}
    length = len(lines)
    for y in range(length*5):
        for x in range(length*5):
            risk_increase = y//length + x//length
            value = lines[y % length][x % length]
            if (int(value) + risk_increase) > 9:
                risk_map[x + 1j * y] = 1 + (int(value) + risk_increase) % 10
            else:
                risk_map[x + 1j * y] = int(value) + risk_increase
            cost_map[x + 1j * y] = 100000
    cost_map[0] = 0
    return risk_map, cost_map

assert run(True) == (40, 315), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
