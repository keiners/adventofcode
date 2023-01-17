def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day9/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    risk_level = 0
    height_by_pos = height_map(lines)
    for k,v in height_by_pos.items():
        neighbours = [ height_by_pos[k + i] for i in [1,-1,1j,-1j] if (k + i) in height_by_pos.keys()]
        if all(v < n for n in neighbours):
            risk_level += 1 + int(v)
    return risk_level

def height_map(lines):
    height_by_pos = {}
    for y,row in enumerate(lines):
        for x,h in enumerate(row):
            height_by_pos[y + 1j * x] = int(h)
    return height_by_pos

def part2(lines):
    height_by_pos = height_map(lines)
    basin_sizes = []
    seen = set()
    for k,v in height_by_pos.items():
        if v != 9 and k not in seen:
            basin = map_basin(k, height_by_pos)
            basin_sizes.append(len(basin))
            seen |= basin
    return sorted(basin_sizes)[-1] * sorted(basin_sizes)[-2] * sorted(basin_sizes)[-3]

def map_basin(p, map_):
    queue = set([p])
    visited = set()
    while len(queue) > 0:
        pos = queue.pop()
        visited.add(pos)
        neighbours = [ (pos + i) for i in [1,-1,1j,-1j] if (pos + i) in map_.keys() and map_[pos + i] != 9]
        for n in [n for n in neighbours if n not in visited]:
            queue.add(n)
    return visited
        
assert run(True) == (15, 1134), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
