def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day5/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    vents = {}
    for line in lines:
        x1,y1,x2,y2 = [int(i) for i in line.replace(" -> ", ",").split(',')]
        if not (x1 == x2 or y1 == y2):
            continue
        dx = 1 if x1<=x2 else -1
        dy = 1 if y1<=y2 else -1
        for x in range(x1,x2+dx,dx):
            for y in range(y1,y2+dy,dy):
                if (x,y) in vents:
                    vents[(x,y)] += 1
                else:
                    vents[(x,y)] = 1
    return len([i for i in vents.values() if i>1])
            
def part2(lines):
    vents = {}
    for line in lines:
        x1,y1,x2,y2 = [int(i) for i in line.replace(" -> ", ",").split(',')]
        dx = 1 if x1<=x2 else -1
        dy = 1 if y1<=y2 else -1
        if x1 == x2 or y1 == y2:
            for x in range(x1,x2+dx,dx):
                for y in range(y1,y2+dy,dy):
                    if (x,y) in vents:
                        vents[(x,y)] += 1
                    else:
                        vents[(x,y)] = 1
        else:
            for i in range(abs(x1-x2)+1):
                pos = (x1+(dx*i),y1+(dy*i))
                if pos in vents:
                    vents[pos] += 1
                else:
                    vents[pos] = 1
    return len([i for i in vents.values() if i>1])

assert run(True) == (5, 12)

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
