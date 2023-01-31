import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day8/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    visited = {i:False for i in range(len(lines))}
    acc = 0
    i = 0
    while True:
        if visited[i]:
            return acc
        else:
            visited[i] = True
        op, arg = lines[i].split(" ")
        n = 1 if arg[0] == "+" else -1
        n = n * int(arg[1:])
        if op == "acc":
            acc += n
            i += 1
        elif op == "jmp":
            i += n
        else:
            i += 1

def part2(lines):
    visited = set()
    changed = set()
    acc = 0
    i = 0
    changed_op = False
    while i < len(lines):
        if i in visited:
            acc = 0
            changed_op = False
            visited = set()
            i = 0
            continue
        else:
            visited.add(i)
        op, arg = lines[i].split(" ")
        n = 1 if arg[0] == "+" else -1
        n = n * int(arg[1:])
        if not changed_op and (op == "nop" or op == "jmp") and i not in changed:
            changed_op = True
            changed.add(i)
            if op == "nop": op = "jmp"
            else: op = "nop"
        if op == "acc":
            acc += n
            i += 1
        elif op == "jmp":
            i += n
        else:
            i += 1
    return acc

assert run(True) == (5, 8), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
