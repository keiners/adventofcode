def run():
    fileName = "day24/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    Storm.len_x = len(lines) - 2
    Storm.len_y = len(lines[0]) - 2
    storms = []
    for i, line in enumerate(lines[1:-1]):
        for j, char in enumerate(list(line)[1:-1]):
            if char != ".":
                storms.append(Storm(i,j,char))

    start = (-1, list(lines[0]).index(".") - 1)
    end = (len(lines)-2, list(lines[-1]).index(".") - 1)
    inner_start = (start[0] + 1, start[1])
    inner_end = (end[0] - 1, end[1])
    
    time1 = travel(start, storms, inner_end)
    print(f"Trip 1: {time1}")
    time2 = travel(end, storms, inner_start)
    print(f"Trip 2: {time2}")
    time3 = travel(start, storms, inner_end)
    print(f"Trip 3: {time3}")
    print(f"Total: {time1+time2+time3}")

def travel(pos, storms, end):
    time = 0
    positions = {pos}
    moves = ((0,0),(0,1),(0,-1),(1,0),(-1,0))
    while True:
        time += 1
        if end in positions:
            move_storms(storms)
            return time
        move_storms(storms)
        storm_cords = {(s.x,s.y) for s in storms}
        
        new_positions = set()
        for px,py in positions:
            if (px,py) == (-1,0):
                new_positions.update({(0,0), (-1,0)})
            elif (px,py) == (Storm.len_x, Storm.len_y-1):
                new_positions.update({(px,py), (px-1,py)})
            else:
                if (px,py) == (0,0):
                    new_positions.update({(-1,0)})
                foo = {(px+dx, py+dy) for dx,dy in moves if 0<=(px+dx)<Storm.len_x and 0<=(py+dy)<Storm.len_y}
                new_positions.update(foo)
        
        positions = new_positions - storm_cords

def move_storms(storms):
    for s in storms:
        s.move()

def print_map(storms, positions={}):
    coords = [(s.x, s.y) for s in storms]
    for i in range(Storm.len_x):
        row = []
        for j in range(Storm.len_y):
            if (i,j) in positions:
                row.append("X")
            elif (i,j) in coords:
                row.append("#")
            else:
                row.append(".")
        print(row)

class Storm:
    len_x = 0
    len_y = 0
    def __init__(self, x, y, dir) -> None:
        self.x = x
        self.y = y
        self.dir = dir
    def move(self):
        mv = {"<":(0,-1),
              ">":(0,1),
              "v":(1,0),
              "^":(-1,0)}
        self.x = (self.x + mv[self.dir][0]) % Storm.len_x
        self.y = (self.y + mv[self.dir][1]) % Storm.len_y

run()
