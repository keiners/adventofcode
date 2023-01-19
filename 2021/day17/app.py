import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day17/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    # Max initial y-velocity is equal y-distance to bottom of target are - 1
    _,_,y1,_ = [int(i) for i in re.findall(r"-?\d+", lines[0])]
    return sum(range(abs(y1)))

def part2(lines):
    x1,x2,y1,y2 = [int(i) for i in re.findall(r"-?\d+", lines[0])]
    
    # Find min and max initial velocity
    for i in range(x1):
        if sum(range(i+1)) >= x1:
            x_min = i
            break
    x_max = x2
    y_min = y1
    y_max = abs(y1)-1
    
    # Find max y velocity to reach area
    hits = set()
    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            init_velocity = x + 1j * y
            prev_pos,curr_pos = 0, init_velocity
            while True:
                if curr_pos.real > x2 or curr_pos.imag < y1:
                    # Missed area
                    break
                elif curr_pos.real < x1 or curr_pos.imag > y2:
                    # Not yet reached area
                    prev_pos,curr_pos = curr_pos, get_next_pos(prev_pos, curr_pos)
                else:
                    # Hit target
                    hits.add(init_velocity)
                    break
    return len(hits)

def get_next_pos(start, end):
    speed = end - start
    if speed.real == 0:
        speed += 1
    return end + speed - 1 - 1j        

assert run(True) == (45, 112), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
