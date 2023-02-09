def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day24/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    tiles = map_tiles(lines)
    a1 = part1(tiles)
    a2 = part2(tiles)

    return (a1, a2)

def map_tiles(lines):
    tiles = {} #True=Black, start white
    for line in lines:
        position = 0 + 0 * 1j
        i = 0
        while i < len(line):
            if line[i] == 'n' or line[i] == 's':
                dy = 1 if line[i] == 's' else -1
                dx = 1j if line[i+1] == 'e' else -1j
                i += 2
            else:
                dy = 0
                dx = 2j if line[i] == 'e' else -2j
                i += 1
            position = position + dx + dy
        tiles[position] = not tiles[position] if position in tiles else True
    return tiles

def part1(tiles):
    return list(tiles.values()).count(True)

def part2(tiles):
    days = 100
    for d in range(days):
        # Add missing relevant white tiles to grid
        for black_tile in [k for k,v in tiles.items() if v]:
            for adj_tile in get_adjacent(black_tile):
                if adj_tile not in tiles:
                    tiles[adj_tile] = False
        # Find tiles to flip
        tiles_to_flip = []
        for k,v in tiles.items():
            black_adj = 0
            for adj_tile in get_adjacent(k):
                if adj_tile in tiles and tiles[adj_tile]:
                    black_adj += 1
            if v and (black_adj == 0 or black_adj > 2):
                tiles_to_flip.append(k)
            elif not v and black_adj == 2:
                tiles_to_flip.append(k)
        # Flip tiles
        for t in tiles_to_flip:
            tiles[t] = not tiles[t]
    return list(tiles.values()).count(True)

def get_adjacent(pos):
    adj = [(2*1j + pos), (-2*1j + pos)]
    for y in [-1,1]:
        for x in [-1,1]:
            adj.append((pos+y+x*1j))
    return adj

assert run(True) == (10, 2208), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
