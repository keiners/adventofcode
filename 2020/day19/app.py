import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day19/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    rules = {}
    solved_rules = {}
    for i,line in enumerate(lines):
        if line == "": 
            end_of_rules = i
            break
        key,val = line.split(": ")
        if val.startswith('"'):
            solved_rules[key] = val[1]
        rules[key] = val
    
    line = rules["0"]
    while re.findall("\d+", line):
        split_line = line.split(" ")
        new_line = ""
        for s in split_line:
            if s.isdigit():
                if s in solved_rules:
                    new_line += f"{solved_rules[s]}"
                else:
                    new_line += f"< {rules[s]} >"
            else:
                new_line += f"{s}"
        line = new_line
    
    while re.findall("<[ab]*>", line):
        for m in set(re.findall("<[ab]*>", line)):
            line = line.replace(m, m[1:-1])

    valid_words = get_valid_words(line)    
    count = 0
    for line in lines[end_of_rules:]:
        if line in valid_words:
            count += 1
    return count

def get_valid_words(line):
    words = []
    if "<" not in line:
        return [line]
    else: 
        split_string = split_substring(line, line.index("<"))
        if len(split_string) == 3:
            new_line = split_string[0]+split_string[1]+split_string[2]
            words += get_valid_words(new_line)
        else:
            for j in [1,2]:
                    new_line = split_string[0]+split_string[j]+split_string[3]
                    words += get_valid_words(new_line)
    return words

def split_substring(line, start_sub):
    depth = 0
    separator = -1
    for i,c in enumerate(line[start_sub+1:]):
        if c == "<":
            depth += 1
        elif c == "|" and depth == 0: 
            separator = start_sub + i +1
        elif c == ">":
            depth += -1
            if depth == -1:
                end_sub = start_sub + i +1
                break
    if separator == -1:
        return [line[:start_sub], line[start_sub+1:end_sub], line[end_sub+1:]]
    else:
        return [line[:start_sub], line[start_sub+1:separator], line[separator+1:end_sub], line[end_sub+1:]]


def part2(lines):
    return 0

assert run(True) == (2, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
