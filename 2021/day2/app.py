def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day2/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    return (a1, a2)

def part1(lines):
    movement = {"forward":0, "down":0, "up":0}
    for line in lines:
        dir,value = line.split(" ")
        movement[dir] += int(value)
    return movement["forward"] * (movement["down"] - movement["up"])

def part2(lines):
    aim = 0
    pos = 0
    depth = 0
    for line in lines:
        dir,value = line.split(" ")
        value = int(value)
        if dir == "down":
            aim += value
        elif dir == "up":
            aim -= value
        else:
            pos += value
            depth += aim * value
    return pos * depth

assert run(True) == (150, 900)

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
