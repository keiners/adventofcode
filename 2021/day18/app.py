import re, math
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day18/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    current_line = lines[0]
    for line in lines[1:]:
        new_line = add(current_line, line)
        new_line = explode_and_split(new_line)
        current_line = new_line
    return get_magnitude(current_line)

def part2(lines):
    max_magnitude = 0
    for line1 in lines:
        for line2 in lines:
            if line1 == line2:
                continue
            new_line = explode_and_split(add(line1,line2))
            magnitude = get_magnitude(new_line)
            max_magnitude = max(max_magnitude,magnitude)
    return max_magnitude

def add(left, right):
    return f"[{left},{right}]"

def explode_and_split(line):
    while True:
        nest = 0
        exploded = False
        split = False
        for i,c in enumerate(line):
            if nest > 4:
                assert c != "[" and c != "]"
                end_of_pair = i + line[i:].index("]") + 1
                line = explode(line[:i-1],
                                line[i-1:end_of_pair],
                                line[end_of_pair:])
                exploded = True
                break
            elif c == "[":
                nest += 1
            elif c == "]":
                nest += -1
        if not exploded:
            matches = re.findall("\d{2,}", line)
            if matches:
                to_split = matches[0]
                index = line.find(to_split)
                x,y = [math.floor(int(to_split) / 2), math.ceil(int(to_split) / 2)]
                line = line[:index] + f"[{x},{y}]" + line[index + len(to_split):]
                split = True
        if not exploded and not split:
            return line

def explode(start, pair, end):
    x,y = eval(pair)
    matches = re.findall("\d+", start)
    if matches:
        n_left = matches[-1]
        index = start.rfind(n_left)
        start = start[:index] + str(int(n_left) + int(x)) + start[index + len(n_left):]
    matches = re.findall("\d+", end)
    if matches:
        n_right = matches[0]
        index = end.find(n_right)
        end = end[:index] + str(int(n_right) + int(y)) + end[index + len(n_right):]
    pair = "0"
    return start+pair+end

def get_magnitude(line):
    while True:
        matches = re.findall("\d+,\d+", line)
        if len(matches) == 0:
            break
        for match in matches:
            x,y = [int(i) for i in match.split(",")]
            line = line.replace(f"[{match}]", str(3*x + 2*y))
    return int(line)

assert run(True) == (4140, 3993), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
