import queue
def run(test=False):
    fileName = "day18/input.txt" if not test else "day18/test_input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    cubes = []
    grid_length = 0
    for line in lines:
        position = [int(i) for i in line.split(sep=",")]
        if max(position) > grid_length:
            grid_length = max(position)
        cubes.append(Cube(position[0],position[1],position[2]))
    grid_length += 1
    
    lava = [[[False for z in range(grid_length)] for y in range(grid_length)] for x in range(grid_length)]
    for c in cubes:
        lava[c.x][c.y][c.z] = True
    
    answer_1 = 0
    c: Cube
    for c in cubes:
        x,y,z = [c.x,c.y,c.z]
        for d in [-1, 1]:
            if not is_lava(lava,x+d,y,z):
                answer_1 += 1
            if not is_lava(lava,x,y+d,z):
                answer_1 += 1
            if not is_lava(lava,x,y,z+d):
                answer_1 += 1
    
    if not test: print(f"Answer part 1: {answer_1}")
    
    # BFS from edge of graph to map all air pockets
    surface = find_surface(lava)
    
    answer_2 = 0
    c: Cube
    for c in cubes:
        adjacent_cubes = c.get_adjacent_positions()
        for cube in adjacent_cubes:
            x,y,z = cube
            if any(i not in range(0,grid_length) for i in [x,y,z]):
                # if cube is outside graph => surface
                answer_2 += 1
            elif surface[x][y][z]:
                answer_2 += 1
    
    if not test: print(f"Answer part 2: {answer_2}")
    
    return answer_1, answer_2

def is_lava(lava, x, y, z):
    if any(i not in range(0,len(lava)) for i in [x,y,z]):
        return False
    else: return lava[x][y][z]

def find_surface(lava):
    """BFS from all outermost non-lava cubes in the graph, visiting every adjacent non-lava cube"""
    grid_length = len(lava)
    surface = [[[False for z in range(grid_length)] for y in range(grid_length)] for x in range(grid_length)]
    q = queue.Queue()
    for i in range(1, grid_length-1):
        for j in range(1, grid_length-1):
            for d in [0, grid_length-1]:
                if not lava[i][j][d]:
                    q.put((i,j,d))
                if not lava[i][d][j]:
                    q.put((i,d,j))
                if not lava[d][i][j]:
                    q.put((d,i,j))
    while not q.empty():
        next = q.get()
        c = Cube(next[0],next[1],next[2])
        if not surface[c.x][c.y][c.z]:
            surface[c.x][c.y][c.z] = True
            for adjacent_cube in c.get_adjacent_positions():
                x,y,z = adjacent_cube
                if any((i not in range(0, grid_length)) for i in [x,y,z]):
                    continue
                if not surface[x][y][z] and not lava[x][y][z]:
                    q.put((x,y,z))
    return surface

class Cube:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    def get_adjacent_positions(self):
        x,y,z = self.x, self.y, self.z
        return [(x+1,y,z), (x,y+1,z), (x,y,z+1),
                (x-1,y,z), (x,y-1,z), (x,y,z-1)]

assert run(test=True) == (64,58)
run()
