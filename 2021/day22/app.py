import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day22/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    steps = []
    for line in lines:
        step = [line[1]=="n"] + [int(i) for i in re.findall(r"-?\d+", line)]
        steps.append(step)
    cubes = {}
    for switch,x1,x2,y1,y2,z1,z2 in steps:
        for x in range(max(-50,x1),min(51,x2+1)):
            for y in range(max(-50,y1),min(51,y2+1)):
                for z in range(max(-50,z1),min(51,z2+1)):
                    cubes[x,y,z] = switch
    return len([cube for cube in cubes.values() if cube == True])

def part2(lines):
    steps = []
    for line in lines:
        step = [line[1]=="n"] + [int(i) for i in re.findall(r"-?\d+", line)]
        steps.append(step)
    return 0

class Square:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
    def volume(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)


assert run(True) == (474140, 2758514936282235), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
