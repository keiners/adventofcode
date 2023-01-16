def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day7/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]

    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    positions = [int(i) for i in lines[0].split(",")]
    
    fuel_cost = []
    for i in range(min(positions), max(positions)+1):
        sum = 0
        for p in positions:
            sum += abs(i-p)
        fuel_cost.append(sum)
    return min(fuel_cost)

def part2(lines):
    positions = [int(i) for i in lines[0].split(",")]
    
    fuel_cost = []
    min_sum = None
    for i in range(min(positions), max(positions)+1):
        sum_ = 0
        for p in positions:
            if min_sum is not None and sum_ > min_sum:
                break
            steps = abs(i-p)
            sum_ += sum(range(steps+1))
        fuel_cost.append(sum_)
        if min_sum is None or sum_ < min_sum:
            min_sum = sum_
    return min(fuel_cost)

print("!! Slowish with large data sets !!") #FIXME
assert run(True) == (37, 168)

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
