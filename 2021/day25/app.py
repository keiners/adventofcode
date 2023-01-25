def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day25/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    print("WARNING: VERY SLOW!")
    e_cucumbers = []
    s_cucumbers = []
    dy = len(lines)
    dx = len(lines[0])
    for y,row in enumerate(lines):
        for x,char in enumerate(row):
            if char == "v":
                s_cucumbers.append(x + y * 1j)
            elif char == ">":
                e_cucumbers.append(x + y * 1j)
    
    step = 0
    while True:
        step += 1
        moves = 0
        new_e_cucumbers = []
        new_s_cucumbers = []
        for current_pos in e_cucumbers:
            next_pos = current_pos + 1
            next_pos = complex(next_pos.real % dx, next_pos.imag % dy)
            if next_pos not in e_cucumbers + s_cucumbers:
                moves += 1
                new_e_cucumbers.append(next_pos)
            else:
                new_e_cucumbers.append(current_pos)
                
        e_cucumbers = new_e_cucumbers
        for current_pos in s_cucumbers:
            next_pos = current_pos + 1j
            next_pos = complex(next_pos.real % dx, next_pos.imag % dy)
            if next_pos not in e_cucumbers + s_cucumbers:
                moves += 1
                new_s_cucumbers.append(next_pos)
            else:
                new_s_cucumbers.append(current_pos)
        s_cucumbers = new_s_cucumbers
        if moves == 0:
            return step

def part2(lines):
    return 0

assert run(True) == (58, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
