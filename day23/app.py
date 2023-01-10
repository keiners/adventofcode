import copy
def run():
    fileName = "day23/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    map = []
    for line in lines:
        map.append(list(line))
    
    print("!!VERY SLOW!!") #TODO
    part1_map = simulate(copy.deepcopy(map), 10)
    part1 = calculate_answer(part1_map)
    print(f"Answer part 1: {part1}")
    part2 = simulate(copy.deepcopy(map), 10, True)
    print(f"Answer part 2: {part2}")

def simulate(map, rounds, part_2 = False):
    if part_2: rounds = 100000
    directions = ["N", "S", "W", "E"]
    for i in range(rounds):
        map = extend_map(map)
        elfs = elf_coords(map)
        rejected_moves = []
        accepted_moves = {}
        # 1. Plan Moves
        for elf in elfs:
            if alone(elf, elfs):
                continue
            else:
                for d in range(4):
                    direction = directions[(i+d) % 4]
                    if free_space(elf, elfs, direction):
                        move_to = move(elf, direction)
                        if move_to in rejected_moves:
                            pass
                        elif move_to in accepted_moves.keys():
                            accepted_moves.pop(move_to)
                            rejected_moves.append(move_to)
                        else:
                            accepted_moves[move_to] = elf
                        break
                        
        # 2. Do Moves
        if part_2 and len(accepted_moves) == 0:
            return i+1
        for new, old in accepted_moves.items():
            map[new[0]][new[1]] = "#"
            map[old[0]][old[1]] = "."
    return map
    

def move(elf, direction):
    mv = {"N":(-1, 0), "S":(1, 0), "W":(0, -1), "E":(0, 1)}
    return (elf[0] + mv[direction][0], elf[1] + mv[direction][1])
def elf_coords(map):
    out = []
    for x,row in enumerate(map):
        for y,char in enumerate(row):
            if char == "#":
                out.append((x,y))
    return out
def free_space(e, elfs, direction):
    if direction in ("N", "S"):
        row = (e[0] - 1) if direction == "N" else (e[0] + 1)
        for i in range(-1,2):
            if (row, e[1]+i) in elfs:
                return False
    else:
        col = (e[1] - 1) if direction == "W" else (e[1] + 1)
        for i in range(-1,2):
            if (e[0]+i, col) in elfs:
                return False
    return True
def alone(e, elfs):
    coords = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            coords.append((i,j))
    coords.remove((0,0))
    coords = [(e[0]+i, e[1]+j) for i,j in coords]
    shared_coord = bool(set(coords) & set(elfs))
    return not shared_coord
def extend_map(map):
    rows = len(map)
    cols = len(map[0])
    N = "#" in map[0]
    S = "#" in map[rows-1]
    W = "#" in [map[i][0] for i in range(rows)]
    E = "#" in [map[i][cols-1] for i in range(rows)]
    if W or E:
        for i in range(rows):
            if E: map[i].insert(cols, ".")
            if W: map[i].insert(0, ".")
    if S: map.insert(rows, ["." for _ in range(cols+(W,E).count(True))])
    if N: map.insert(0, ["." for _ in range(cols+(W,E).count(True))])
    return map

def calculate_answer(map):
    elfs = elf_coords(map)
    min1 = min([elf[0] for elf in elfs])
    max1 = max([elf[0] for elf in elfs])
    min2 = min([elf[1] for elf in elfs])
    max2 = max([elf[1] for elf in elfs])
    return ((max1-min1+1) * (max2-min2+1)) - len(elfs)


run()
