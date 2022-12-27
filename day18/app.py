def run():
    fileName = "day18/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    cubes = []
    for line in lines:
        x,y,z = line.split(sep=",")
        cubes.append(Cube(x,y,z))

    grid_length = int(max([c.max() for c in cubes]))+2
    graph = [[[False for z in range(grid_length)] for y in range(grid_length)] for x in range(grid_length)]
    
    for c in cubes:
        graph[c.x][c.y][c.z] = True
    
    counter = 0
    for c in cubes:
        start_count_1 = counter
        x,y,z = [c.x,c.y,c.z]
        for d in [-1, 1]:
            if not graph[x+d][y][z]:
                counter += 1
            if not graph[x][y+d][z]:
                counter += 1
            if not graph[x][y][z+d]:
                counter += 1
    
    print("Answer part 1: " + str(counter))
    
    counter2 = 0
    for c in cubes:
        break
        # edge_nodes = find_edge_nodes(cube, max)
        # for each edge_node:
        #   check all 6(or 5) directions
        #   if direction found with no True
        #       counter2++
        x2,y2,z2 = [c.x,c.y,c.z]
        x_up = [graph[d][y2][z2] for d in range(x2+1, len(graph))]
        x_down = [graph[d][y2][z2] for d in range(0, x2)]
        if True not in x_up:
            counter2 += 1
        if True not in x_down:
            counter2 += 1
            
        y_up = [graph[x2][d][z2] for d in range(y2+1, len(graph))]
        y_down = [graph[x2][d][z2] for d in range(0, y2)]
        if True not in y_up:
            counter2 += 1
        if True not in y_down:
            counter2 += 1
            
        z_up = [graph[x2][y2][d] for d in range(z2+1, len(graph))]
        z_down = [graph[x2][y2][d] for d in range(0, z2)]
        if True not in z_up:
            counter2 += 1
        if True not in z_down:
            counter2 += 1
            

    print("Answer part 2: " + str(counter2)) #assert==58

class Cube:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    def max(self):
        return max([self.x, self.y, self.z])
        
run()