def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day1/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    numbers = [int(i) for i in lines]
    for i in numbers:
        if (2020 - i) in numbers:
            return (2020 - i) * i

def part2(lines):
    numbers = sorted([int(i) for i in lines])
    for n,i in enumerate(numbers):
        for j in numbers[n+1:]:
            if (i+j) > 2020: break
            if (2020 - i - j) in numbers:
                return (2020 - i - j) * i * j

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
