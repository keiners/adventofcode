def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day12/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    cave = get_cave(lines)
    queue = []
    queue.append(['start'])
    completed_paths = []
    while len(queue)>0:
        path = queue.pop()
        if path[-1] == "end":
            completed_paths.append(path)
            continue
        for c in cave[path[-1]]:
            if c.isupper():
                queue.append(path+[c])
            elif c not in path:
                queue.append(path+[c])
    return len(completed_paths)

def get_cave(lines):
    cave = {}
    for line in lines:
        a,b = line.split("-")
        if a in cave.keys():
            cave[a].append(b)
        else:
            cave[a] = [b]
        if b in cave.keys():
            cave[b].append(a)
        else:
            cave[b] = [a]
    return cave

def part2(lines):
    cave = get_cave(lines)

    queue = []
    queue.append(['start'])
    completed_paths = set()
    while len(queue)>0:
        path = queue.pop()
        if path[-1] == "end":
            completed_paths.add(tuple(path))
            continue
        for c in cave[path[-1]]:
            if c.isupper():
                queue.append(path+[c])
            else:
                visited_small_cave_twice = any(path.count(x)>1 for x in [y for y in path if y.islower()])
                if visited_small_cave_twice:
                    if c not in path:
                        queue.append(path+[c])
                elif path.count(c) < 2 and c != "start":
                    queue.append(path+[c])
    return len(completed_paths)

assert run(True) == (10, 36), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
