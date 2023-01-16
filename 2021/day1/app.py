def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day1/{fileName}", "r")
    lines = [int(line.replace("\n", "")) for line in f.readlines()]
    
    a1 = count_increases(lines)
    a2 = part2(lines)
    return (a1, a2)

def count_increases(lines):
    start = lines[0]
    count = 0
    for line in lines[1:]:
        if line > start:
            count += 1
        start = line
    return count

def part2(lines):
    sums = [lines[i]+lines[i+1]+lines[i+2] for i in range(0, len(lines)-2)]
    return count_increases(sums)
    
assert run(True) == (7, 5)

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
