import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day3/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    return slope(lines, 3, 1)

def part2(lines):
    answer = 1
    for i,j in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        answer = answer * slope(lines, i, j)
    return answer

def slope(lines, dx, dy):
    my = len(lines)
    mx = len(lines[0])
    x,y = 0,0
    trees = 0
    while y < my:
        if lines[y][x] == "#":
            trees += 1
        x = (x + dx) % mx
        y = y + dy
    return trees

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
