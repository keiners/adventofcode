import itertools
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day17/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    map = {}
    for x,row in enumerate(lines):
        for y,char in enumerate(row):
            cube = Cube(x,y,0)
            state = True if char == "#" else False
            map[cube] = state
    print("IN MAP")
    for m in map:
        if map[m]: print(m.print())
    for i in range(1):
        for m in map:
            count = 0
            nodes = m.n()
            for n in nodes:
                if n == Cube(1,2,0):
                    print("Match")
                print(n.print())
                if n in map and map[n]:
                    print()
                    count += 1
            #print((m.__str__(), count))
    return 0

def part2(lines):
    return 0

class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def n(self):
        a,b,c = self.x,self.y,self.z
        n = []
        permutations = itertools.product([-1,0,1], repeat=3)
        for p in permutations:
            if p == (0,0,0): continue
            n.append([a+p[0], b+p[1], c+p[2]])
        return [Cube(i[0], i[1], i[2]) for i in n]
    def print(self):
        return f"{self.x} {self.y} {self.z}"


assert run(True) == (0, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
