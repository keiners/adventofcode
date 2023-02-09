def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day23/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    cups = [int(i) for i in list(lines[0])]
    for i in range(100):
        cups = move(cups)
    index_1 = cups.index(1)
    cups = shift(cups, index_1)
    print(cups)
    return "".join(str(i) for i in cups[1:])

def move(cups):
    hold = cups[1:4]
    target = cups[0] - 1
    while target not in cups or target in hold:
        target += -1
        if target < min(cups):
            target = max(cups)
    target_index = cups.index(target)
    return cups[4:target_index+1] + hold + cups[target_index+1:] + [cups[0]]

def shift(seq, n):
    return seq[n:]+seq[:n]

def part2(lines): #TODO: Too slow
    cups = [int(i) for i in list(lines[0])]
    cups2 = [int(i) for i in range(max(cups)+1, 1000000+1)]
    cups = cups + cups2
    for i in range(10000000):
        print(i)
        cups = move_2(cups)
    index_1 = cups.index(1)
    #print(cups[index_1-10:index_1+10])
    return cups[index_1+1] * cups[index_1+2]

def move_2(cups):
    hold = cups[1:4]
    target = cups[0] - 1
    while target in hold or target == 0:
        target += -1
        if target < 1:
            target = len(cups)
    target_index = cups.index(target)
    return cups[4:target_index+1] + hold + cups[target_index+1:] + [cups[0]]

assert run(True) == ("67384529", 149245887792), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
