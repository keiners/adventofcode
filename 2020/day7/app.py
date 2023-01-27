def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day7/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    rules = {}
    for line in lines:
        args = line.split(" ")
        key = f"{args[0]} {args[1]}"
        rules[key] = []
        for i in range(4, len(args), 4):
            rules[key].append(f"{args[i+1]} {args[i+2]}")
    valids = set()
    while True:
        before = len(valids)
        for bag,bags in rules.items():
            if "shiny gold" in bags:
                valids.add(bag)
            else:
                for indirect_bag in [b for b in valids]:
                    if indirect_bag in bags:
                        valids.add(bag)
        after = len(valids)
        if before == after:
            return after

def part2(lines):
    rules = {}
    for line in lines:
        args = line.split(" ")
        key = f"{args[0]} {args[1]}"
        rules[key] = []
        for i in range(4, len(args), 4):
            rules[key].append(f"{args[i]} {args[i+1]} {args[i+2]}")    
    return get_bag(rules, "shiny gold")-1

def get_bag(rules, bag):
    weight = 1
    if rules[bag] != ['no other bags.']:
        for b in rules[bag]:
            inner_line = b.split(" ")
            n = int(inner_line[0])
            inner_bag = f"{inner_line[1]} {inner_line[2]}"
            extra_w = n * (get_bag(rules, inner_bag))
            weight += extra_w
    return weight

assert run(True) == (4, 32), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
