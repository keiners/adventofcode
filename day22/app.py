import re
def run():
    fileName = "day22/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    moves = re.findall(r"\d+|[RL]", lines[-1])
    print(moves)
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    pos = None
    dir = directions[0]
    max_len = max([len(line) for line in lines[:-1]])
    grid = [[" " for i in range(max_len)] for j in range(len(lines[:-1]))]    
    for i, line in enumerate(lines[:-1]):
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
                    print(pos)
        elif m == "R":
            dir = directions[(directions.index(dir)+1) % len(directions)]
        elif m == "L":
            dir = directions[(directions.index(dir)-1) % len(directions)]
    
def move(pos, dir, grid):
    print(pos)
    print(dir)
    x = (pos[0]+dir[0]) % len(grid[0])
    y = (pos[1]+dir[1]) % len(grid)
    print((x,y))
    return (x, y)
def valid(grid, pos):
    return grid[pos[0]][pos[1]] == "."
    
    
run()
