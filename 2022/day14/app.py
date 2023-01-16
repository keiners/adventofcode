def run(test=False):
    fileName = "day14/test_input.txt" if test else "day14/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    rocks = set()
    for line in lines:
        coords = [list(map(int, pos.split(","))) for pos in line.strip().split(" -> ")]
        for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    rocks.add((x, y))

    a = simPart1(set(rocks))
    b = simPart2(set(rocks))
    return (a,b)
    
def simPart1(rocks):
    abyss = max([y for _, y in rocks]) + 1
    sandPos = (500, 0)
    sand = 0
    while True:
        if sandPos[1] >= abyss:
            print("PART 1: "+str(sand))
            return sand
        if airBelow(sandPos, rocks):
            sandPos = (sandPos[0], sandPos[1]+1)
            continue
        elif airLeft(sandPos, rocks):
            sandPos = (sandPos[0]-1, sandPos[1]+1)
            continue
        elif airRight(sandPos, rocks):
            sandPos = (sandPos[0]+1, sandPos[1]+1)
            continue
        else:
            rocks.add(sandPos)
            sand += 1
            sandPos = (500,0)
            continue

def simPart2(rocks):
    floor = max([y for _, y in rocks]) + 1
    sandPos = (500, 0)
    sand = 0
    while True:
        if notHitBottom(sandPos, floor):
            if airBelow(sandPos, rocks):
                sandPos = (sandPos[0], sandPos[1]+1)
                continue
            elif airLeft(sandPos, rocks):
                sandPos = (sandPos[0]-1, sandPos[1]+1)
                continue
            elif airRight(sandPos, rocks):
                sandPos = (sandPos[0]+1, sandPos[1]+1)
                continue
            else:
                if sandPos == (500,0):
                    sand += 1
                    print("Part 2: "+str(sand))
                    return sand
                else:
                    rocks.add(sandPos)
                    sand += 1
                    sandPos = (500,0)
                    continue
        else:
            rocks.add(sandPos)
            sand += 1
            sandPos = (500,0)
            continue
    
def airBelow(pos, map):
    return (pos[0], pos[1]+1) not in map
def airLeft(pos, map):
    return (pos[0]-1, pos[1]+1) not in map
def airRight(pos, map):
    return (pos[0]+1, pos[1]+1) not in map
def notHitBottom(pos, floor):
    return pos[1] < floor

run()
