import itertools
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day17/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = run_cycles(lines, four_dimensions=False)
    a2 = run_cycles(lines, four_dimensions=True)
    return (a1, a2)

def run_cycles(lines, four_dimensions):
    active_cubes = {}
    for y,row in enumerate(lines):
        for x,char in enumerate(row):
            if char == "#":
                if four_dimensions:
                    active_cubes[(x,y,0,0)] = True
                else:
                    active_cubes[(x,y,0)] = True
    for cycle in range(6):
        inactive_cubes_to_check = set()
        new_active_cubes = {}
        for cube in active_cubes:
            adj_cubes = get_adjacent_cubes(cube)
            count = len([n for n in adj_cubes if n in active_cubes])
            inactive_cubes_to_check.update([n for n in adj_cubes if n not in active_cubes])
            if count == 3 or count == 2:
                new_active_cubes[cube] = True
        for cube in inactive_cubes_to_check:
            adj_cubes = get_adjacent_cubes(cube)
            count = len([n for n in adj_cubes if n in active_cubes])
            if count == 3:
                new_active_cubes[cube] = True
        active_cubes = new_active_cubes
        print(f"{len(active_cubes)} active cubes after round {cycle+1}")
    return len(active_cubes)

def get_adjacent_cubes(coord):
    if len(coord) == 3:
        x,y,z = coord
        n = []
        permutations = itertools.product([-1,0,1], repeat=3)
        for p in permutations:
            if p == (0,0,0): continue
            n.append([x+p[0], y+p[1], z+p[2]])
        return [(i[0],i[1],i[2]) for i in n]
    elif len(coord) == 4:
        x,y,z,w = coord
        n = []
        permutations = itertools.product([-1,0,1], repeat=4)
        for p in permutations:
            if p == (0,0,0,0): continue
            n.append([x+p[0], y+p[1], z+p[2], w+p[3]])
        return [(i[0],i[1],i[2],i[3]) for i in n]

assert run(True) == (112, 848), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
