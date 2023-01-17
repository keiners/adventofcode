def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day11/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    energy_map = map_energy(lines)
    flashes = 0
    for i in range(100):
        flashed = set()
        energy_map = {k:v+1 for k,v in energy_map.items()}
        flash_queue = set([k for k,v in energy_map.items() if v > 9])
        while len(flash_queue) > 0:
            flashes += 1
            current = flash_queue.pop()
            flashed.add(current)
            neighbours = [current + y + x * 1j for y in [-1,0,1] for x in [-1,0,1] ]
            neighbours = [n for n in neighbours if n in energy_map.keys() and n not in flashed]
            for n in neighbours:
                if energy_map[n] < 9:
                    energy_map[n] += 1
                else:
                    flash_queue.add(n)
        for f in flashed:
            energy_map[f] = 0
    return flashes

def map_energy(lines):
    energy = {}
    for y,row in enumerate(lines):
        for x,h in enumerate(row):
            energy[y + 1j * x] = int(h)
    return energy

def part2(lines):
    energy_map = map_energy(lines)
    flashes = 0
    step = 0
    
    while True:
        step += 1
        flashed = set()
        energy_map = {k:v+1 for k,v in energy_map.items()}
        flash_queue = set([k for k,v in energy_map.items() if v > 9])
        while len(flash_queue) > 0:
            current = flash_queue.pop()
            flashed.add(current)
            flashes += 1
            neighbours = [ (current + y + x * 1j) for y in [-1,0,1] for x in [-1,0,1] ]
            neighbours = [n for n in neighbours if n in energy_map.keys() and n not in flashed]
            for n in neighbours:
                if energy_map[n] < 9:
                    energy_map[n] += 1
                else:
                    flash_queue.add(n)
        if len(flashed) == len(energy_map):
            return step
        for f in flashed:
            energy_map[f] = 0

assert run(True) == (1656, 195), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
