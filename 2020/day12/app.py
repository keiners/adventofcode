def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day12/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    directions = [1j, 1, -1j, -1]
    facing = 0
    ship = 0 + 0 * 1j
    for line in lines:
        move = line[0]
        n = int(line[1:])
        if move == "F":
            ship += n * directions[facing]
        elif move in "ESWN":
            d = "ESWN".index(move)
            ship += n * directions[d]
        elif move == "R":
            n = n/90
            facing = int((facing + n) % 4)
        elif move == "L":
            n = n/90
            facing = int((facing - n) % 4)
    return int(abs(ship.real) + abs(ship.imag))

def part2(lines):
    ship = 0 + 0 * 1j
    wayp = -1 + 10 * 1j
    for line in lines:
        move = line[0]
        n = int(line[1:])
        if move == "F":
            ship += n * wayp
        elif move in "ESWN":
            d = "ESWN".index(move)
            wayp += n * [1j, 1, -1j, -1][d]
        elif move in "RL":
            for _ in range(int(n/90)):
                wayp = rotate(wayp, move)
    return int(abs(ship.real) + abs(ship.imag))

def rotate(n, dir):
    x = n.imag
    y = n.real
    if dir=="R":
        return x - y * 1j
    else:
        return -x + y * 1j

assert run(True) == (25, 286), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
