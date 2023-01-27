def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day6/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    groups = {0:set()}
    group_n = 0
    for line in lines:
        if line == "":
            group_n += 1
            groups[group_n] = set()
        else:
            for c in line:
                groups[group_n].add(c)
    return sum([len(i) for i in groups.values()])

def part2(lines):
    groups = {0:[]}
    group_n = 0
    for line in lines:
        if line == "":
            group_n += 1
            groups[group_n] = []
        else:
            person = set()
            for c in line:
                person.add(c)
            groups[group_n].append(person)
    return sum([len(set.intersection(*groups[i])) for i in groups])


a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
