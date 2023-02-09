def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day25/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    pk1,pk2 = [int(i) for i in lines]
    a1 = part1(pk1, pk2)
    a2 = part2(pk1, pk2)
    
    return (a1, a2)

def part1(pk1, pk2):
    pk, loops = find_loop_size(pk1, pk2)
    return loop(pk, loops)

def find_loop_size(n1, n2):
    value = 1
    loop = 0
    while True:
        loop += 1
        value = (value * 7) % 20201227
        if value == n1:
            return (n2,loop)
        elif value == n2:
            return (n1,loop)

def loop(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject) % 20201227
    return value

def part2(pk1, pk2):
    return 0

assert run(True) == (14897079, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
