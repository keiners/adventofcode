def run():
    fileName = "day12/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    map = []
    start = (0,0)
    end = (0,0)
    y = 0
    for line in lines:
        lineArray = []
        x = 0
        for c in line:
            if c == "S":
                start = (y,x)
            elif c == "E":
                end = (y,x)
            lineArray.append(Node(c, y, x))
            x += 1
        map.append(lineArray)
        y += 1
    map = NodeMap(map)

    map = run_part_1(map, start)
    print("Part 1: "+str(map.get_node(end[0], end[1]).distance))
    map = run_part_2(map)
    print("Part 2: "+str(map.get_node(end[0], end[1]).distance))
    
def run_part_1(map, start):
    """Update shortest path from input start position"""
    queue = [map.get_node(start[0],start[1])]
    while len(queue)>0:
        node = queue.pop(0)
        neighbours = map.get_neighbours(node)
        for n in neighbours:
            if n.distance > node.distance + 1:
                n.distance = node.distance + 1
                queue.append(n)
    return map

def run_part_2(map):
    """Update shortest path from multiple starting positions"""
    queue = []
    for row in map.nodes:
        for node in row:
            if node.distance == 0:
                queue.append(node)
                
    while len(queue)>0:
        node = queue.pop(0)
        neighbours = map.get_neighbours(node)
        for n in neighbours:
            if n.distance > node.distance + 1:
                n.distance = node.distance + 1
                queue.append(n)
    return map
    
class NodeMap:
    def __init__(self, nodes) -> None:
       self.nodes = nodes
    def get_neighbours(self,node):
        """Return neighbour nodes reachable from input node"""
        y = node.y
        x = node.x
        neighbours = []
        foo = [(y,x+1),(y,x-1),(y+1,x),(y-1,x)]
        for (y2,x2) in foo:
            if (0 <= y2 < len(self.nodes)) and 0 <= x2 < len(self.nodes[0]):
                neighbour = self.get_node(y2,x2)
                if neighbour.get_height() <= node.get_height() + 1:
                    neighbours.append(neighbour)
        return neighbours
    def get_node(self,y,x):
        return self.nodes[y][x]

class Node:
    def __init__(self, height, y, x):
        self.distance = 999
        if height == "S" or height == "a":
            height = "a"
            self.distance = 0
        elif height == "E":
            height = "z"
        self.height = ord(height)
        self.y = y
        self.x = x
    def get_height(self):
        return self.height

run()