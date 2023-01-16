import re
def run():
    fileName = "day22/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    moves = re.findall(r"\d+|[RL]", lines[-1])
    
    a1 = run_part_1(lines[:-2], moves)
    print(f"Answer part 1: {a1}")
    
    a2 = run_part_2(lines[:-2], moves)
    print(f"Answer part 2: {a2}")
    
def run_part_1(map, moves):
    pos = None
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    dir = directions[0]
    max_len = max([len(line) for line in map])
    grid = [[" " for i in range(max_len)] for j in range(len(map))]    
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if pos is None and char == ".":
                pos = (i,j)
            grid[i][j] = char

    for m in moves:
        if m.isdigit():
            for i in range(int(m)):
                new_pos = move(pos, dir, grid)
                while grid[new_pos[0]][new_pos[1]] == " ":
                    new_pos = move(new_pos, dir, grid)
                if valid(grid, new_pos):
                    pos = new_pos
                    #print(f"New position: {pos}")
        elif m == "R":
            dir = directions[(directions.index(dir)+1) % len(directions)]
        elif m == "L":
            dir = directions[(directions.index(dir)-1) % len(directions)]
    part_1_answer = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + directions.index(dir)
    return part_1_answer

def run_part_2(map, moves):
    pos = None
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    dir = directions[0]
    max_len = max([len(line) for line in map])
    grid = [[" " for i in range(max_len)] for j in range(len(map))]    
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if pos is None and char == ".":
                pos = (i,j)
            grid[i][j] = char

    for m in moves:
        if m.isdigit():
            for i in range(int(m)):
                new_pos, new_dir = move_cube(pos, dir, grid) #TODO: Wrap around cube
                if pos == (19, 50): #FIXME: Debug code
                    print(f"Moving from (19,50) to {new_pos}")
                    exit()
                if valid(grid, new_pos):
                    pos = new_pos
                    dir = new_dir
                    print(f"New position: {pos}")
        elif m == "R":
            dir = directions[(directions.index(dir)+1) % len(directions)]
        elif m == "L":
            dir = directions[(directions.index(dir)-1) % len(directions)]
    
    part_2_answer = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + directions.index(dir)
    return part_2_answer
    
def move(pos, dir, grid):
    x = (pos[0]+dir[0]) % len(grid)
    y = (pos[1]+dir[1]) % len(grid[0])
    return (x, y)
def valid(grid, pos):
    return grid[pos[0]][pos[1]] == "."
def move_cube(pos, dir, grid):
    x = (pos[0]+dir[0])
    y = (pos[1]+dir[1])
    if (0 <= x < len(grid)
            and 0 <= y < len(grid[x])
            and grid[x][y] != " "):
        return (x, y), dir
    else:
        raise NotImplementedError("Wrapping around cube")

    
run()
