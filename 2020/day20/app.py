import math
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day20/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1,a2 = run_task(lines)
    #a1 = part1(lines)
    #a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)


def run_task(lines):
    tiles = {}
    for line in lines:
        if line == "": continue
        elif line.startswith("Tile"):
            current_tile = line.split(" ")[1][:-1]
            y = 0
            tiles[current_tile] = {}
        else:
            for x,char in enumerate(line):
                tiles[current_tile][y + x * 1j] = char
            y += 1
    
    connections = connect_tiles(tiles)
    connections_by_len = {2:[], 3:[], 4:[]}
    for c in connections:
        connections_by_len[len(connections[c])].append(c)
    
    a1 = part1(connections_by_len)
    a2 = part2(tiles, connections, connections_by_len)
    return (a1,a2)

def part1(connections_by_len):
    return math.prod([int(t) for t in connections_by_len[2]])
    
def part2(tiles, connections, connections_by_len):
    grid = find_grid(connections_by_len, connections)
    #print_grid(grid, int(math.sqrt(len(connections))))
    
    #new_grid = remove_borders(tiles, grid)
    alignment = {}
    sq_len = int(math.sqrt(len(grid)))
    
    for y in range(sq_len):
        for x in range(sq_len):
            if (x,y) == (0,0):
                edges1 = get_tile_edges(tiles[grid[0,0]])
                edges2 = get_tile_edges(tiles[grid[1,0]])
                edges3 = get_tile_edges(tiles[grid[0,1]])
                intersect_12 = list(set(edges1).intersection(edges2))
                intersect_13 = list(set(edges1).intersection(edges3))
                if not intersect_12:
                    print("flipped 2")
                    edges2 = flip_edges(edges2)
                    intersect_12 = list(set(edges1).intersection(edges2))
                if not intersect_13:
                    print("flipped3")
                    edges3 = flip_edges(edges3)
                    intersect_13 = list(set(edges1).intersection(edges3))
                intersect_12_i = edges1.index(intersect_12[0])
                if edges1[(intersect_12_i + 1) % 4] == intersect_13[0]:
                    #if tile1 aligned to top left corner
                    flip_1 = False
                    rotate_1 = abs(edges1.index(intersect_12[0])-1)
                else:
                    edges1 = flip_edges(edges1)
                    edges2 = flip_edges(edges2)
                    intersect_12 = list(set(edges1).intersection(edges2))
                    flip_1 = True
                    rotate_1 = abs(edges1.index(intersect_12[0])-1)
                print(f"Flip:{flip_1}. Rotate:{rotate_1}")
                alignment[(0,0)] = (flip_1, rotate_1)
            else:
                if y == 0:
                    print((x,y))
                    adj_tile = alignment[(x-1,y)]
                    edges = get_tile_edges(tiles[grid[x-1,y]])
                    if adj_tile[0] == True:
                        edge_to_match = flip_edges(edges)[(1-adj_tile[1]) % 4]
                        print(f"e2m: {edge_to_match}")
                    else:
                        edge_to_match = edges[(1-adj_tile[1]) % 4][::-1]
                    #print(grid[x,y])
                    edges = get_tile_edges(tiles[grid[x,y]])
                    print(edges)
                    if edge_to_match in edges:
                        print(f"Rotate {grid[x,y]}")
                        edges = flip_edges(edges)
                        #print(edges)
                        rotations = 3 - edges.index(edge_to_match[::-1])
                        #print(f"rots: {rotations}")
                        alignment[(x,y)] = (True, rotations)
                    else:
                        print(f"Dont Rotate {grid[x,y]}")
                        #print("NONON")
                        #print(edges.index(edge_to_match[::-1]))
                        rotations = 3 - edges.index(edge_to_match[::-1])
                        #print(f"rots: {rotations}")
                        alignment[(x,y)] = (False, rotations)
                else:
                    print((x,y))
                    #print(alignment)
                    adj_tile = alignment[(x,y-1)]
                    edges = get_tile_edges(tiles[grid[x,y-1]])
                    if adj_tile[0] == True:
                        edge_to_match = flip_edges(edges)[(2-adj_tile[1]) % 4]
                    else:
                        edge_to_match = edges[(2-adj_tile[1]) % 4][::-1]
                    #print(f"e2m: {edge_to_match}")
                    edges = get_tile_edges(tiles[grid[x,y]])
                    if edge_to_match in edges:
                        #print(f"Rotate {grid[x,y]}")
                        edges = flip_edges(edges)
                        #print(edges)
                        rotations = abs(0 - edges.index(edge_to_match[::-1]))
                        #print(f"rots: {rotations}")
                        alignment[(x,y)] = (True, rotations)
                    else:
                        #print(f"Dont Rotate {grid[x,y]}")
                        #print("NONON")
                        #print(edges.index(edge_to_match[::-1]))
                        rotations = abs(0 - edges.index(edge_to_match[::-1]))
                        #print(f"rots: {rotations}")
                        alignment[(x,y)] = (False, rotations)
            print(f"Align {grid[x,y]} on {(x,y)} as {alignment[(x,y)]}")
                    
    print(alignment)
    return 1
    new_grid = [[1,2,3,4],
                [3,4,5,5],
                [2,7,6,6],
                [1,9,8,7]]
    new_grid = flip_and_rotate_grid(new_grid, True, 0)
    for row in new_grid:
        print(row)
    new_grid = flip_and_rotate_grid(new_grid, True, 2)
    print()
    for row in new_grid:
        print(row)
    return 1

def remove_borders(grid):
    return [row[1:-1] for row in grid[1:-1]]
    
def flip_and_rotate_grid(grid, flip, rotations):
    if flip:
        grid = [row[::-1] for row in grid]
    for r in range(rotations):
        grid = list(zip(*grid[::-1]))
        grid = [list(row) for row in grid]
    return grid

    

def print_grid(grid, length):
    for y in range(length):
        row = []
        for x in range(length):
            row.append(grid[(x,y)])
        print(row)
    
def find_grid(connections_by_len, connections):
    grid = {(0,0): connections_by_len[2][0]}
    sq_len = int(math.sqrt(len(connections)))
    for y in range(sq_len):
        for x in range(sq_len):
            if (x,y) == (0,0): continue
            adj = []
            for p in [(x-1,y), (x,y-1)]:
                if p in grid:
                    adj.append(p)
            if len(adj) == 2:
                t1 = connections[grid[adj[0]]]
                t2 = connections[grid[adj[1]]]
                tiles = list(set(t1).intersection(t2))
            else:
                assert len(adj) == 1
                tiles = connections[grid[adj[0]]]
            con_len = 4
            if x in [0, sq_len-1]: con_len += -1
            if y in [0, sq_len-1]: con_len += -1
            grid[(x,y)] = [t for t in tiles if t not in grid.values() and t in connections_by_len[con_len]][0]
    return grid

def connect_tiles(tiles):
    connections = {}
    edges_per_tile = {}
    for t in tiles:
        connections[t] = []
        edges_per_tile[t] = []
        edges = get_tile_edges(tiles[t])
        edges_per_tile[t] += edges
        edges_per_tile[t] += flip_edges(edges)
    for t1 in tiles:
        for t2 in tiles:
            if t1 == t2 or t2 in connections[t1]: continue
            if bool(set(edges_per_tile[t1]) & set(edges_per_tile[t2])):
                connections[t1].append(t2)
                connections[t2].append(t1)
    return connections

        
def get_tile_edges(tile):
    edges = ["","","",""]
    dy = int(max(i.real for i in tile))
    dx = int(max(i.imag for i in tile))
    for y in range(dy+1):
        edges[3] += tile[y + 0 * 1j]
        edges[1] += tile[y + dx * 1j]
    for x in range(dx+1):
        edges[0] += tile[0 + x * 1j]
        edges[2] += tile[dy + x * 1j]
    edges[2] = edges[2][::-1]
    edges[3] = edges[3][::-1]
    return edges

def flip_edges(edges):
    f = [e[::-1] for e in edges]
    return [f[0], f[3], f[2], f[1]]
    
assert run(True) == (20899048083289, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
