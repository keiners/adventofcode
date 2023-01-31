def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day10/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    numbers = sorted([int(i) for i in lines])
    numbers = [0] + numbers + [max(numbers)+3]
    diff = {1: 0, 2: 0, 3: 0}
    for i,j in [(numbers[i], numbers[i+1]) for i in range(len(numbers)-1)]:
        diff[j-i] += 1
    return diff[1] * diff[3]

def part2(lines):
    numbers = sorted([int(i) for i in lines])
    numbers = [0] + numbers + [max(numbers)+3]
    
    paths_to = {k:0 for k in numbers}
    paths_to[0] = 1
    for i,n in enumerate(numbers[1:]):
        paths_to[n] = 0
        for j in [n - 1, n - 2, n - 3]:
            if j in numbers[:i+1]:
                paths_to[n] += paths_to[j]
    return paths_to[max(numbers)]

assert run(True) == (220, 19208), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
