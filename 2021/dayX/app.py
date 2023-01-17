def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/dayX/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    return 0

def part2(lines):
    return 0

assert run(True) == (0, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
