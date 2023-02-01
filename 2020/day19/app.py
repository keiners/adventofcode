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
        #print(line)
        key,val = line.split(": ")
        if val.startswith('"'):
            solved_rules[key] = val[1]
        rules[key] = val
    
    line = rules["0"]
    while True:
        if len(re.findall("\d+", line)) == 0: break
        split_line = line.split(" ")
        new_line = ""
        for s in split_line:
            if s.isdigit():
                if s in solved_rules:
                    new_line += f"<{solved_rules[s]}>"
                else:
                    new_line += f"< {rules[s]} >"
            else:
                new_line += f"{s}"
        line = new_line
    while True:
        matches = re.findall("<[ab]*>", line)
        print(matches)
        if not matches: break
        for m in set(matches):
            line = line.replace(m, m[1:-1])

    valid_words = get_valid_words(line)
    print(f"SOLUTION: {valid_words}")
    count = 0
    for line in lines[end_of_rules:]:
        #print(line)
        if line in valid_words:
            count += 1
    return count
    

def get_valid_words(line):
    words = []
    if "<" not in line:
        return [line]
    else: 
        print("SPLITTING")
        split_string = split_substring(line, line.index("<"))
        for j in [1,2]:
                new_line = split_string[0]+split_string[j]+split_string[3]
                old_line = f"{split_string[0]}<{split_string[1]}|{split_string[2]}>{split_string[3]}"
                #print(line)
                #print(old_line)
                assert old_line == line, (len(old_line), len(line))
                if ">" in new_line or "<" in new_line:
                    if new_line.index("<") > new_line.index(">"):
                        continue
                        print("## 1 ##")
                        print(split_string[0])
                        print("## 2 ##")
                        print(split_string[1])
                        print("## 3 ##")
                        print(split_string[2])
                        print("## 4 ##")
                        print(split_string[3])
                        asdf = list(new_line).count("<")
                        qwer = list(new_line).count(">")
                        assert asdf == qwer
                words += get_valid_words(new_line)
    return words

def split_substring(line, start_sub):
    if is_valid(line):
        print(line)
    else: exit()
    depth = 0
    separator = -1
    assert line[start_sub] == "<"
    for i,c in enumerate(line[start_sub+1:]):
        #print(f"{c} at depth {depth}")
        if depth == -1:
            print("HOLUP")
            exit()
        if c == "<":
            depth += 1
        elif c == "|": 
                if depth == 0:
                    separator = start_sub + i +1
                    assert line[separator] == "|"
                else: print(f"{c} at depth {depth}")
        elif c == ">":
            depth += -1
            if depth == -1:
                end_sub = start_sub + i +1
                assert line[end_sub] == ">"
                break
    #found = [line[:start_sub], line[start_sub+1:separator], line[separator+1:end_sub], line[end_sub+1:]]
    print()
    print((0,start_sub,separator,end_sub,len(line)-1))
    if separator == -1:
        print(line[start_sub:end_sub])
        print(start_sub)
        print(end_sub)
        exit()
        debugg(line, start_sub)
    return [line[:start_sub], line[start_sub+1:separator], line[separator+1:end_sub], line[end_sub+1:]]


def debugg(line, start):
    level = 0
    for c in line[start+1]:
        if level == 0:
            print(c)
        if c == "<": level += 1
        elif c == ">": level += -1
        elif c == "|" and level == 0: print("FOUND")
        if level == -1:
            print("end reached")
            break
    return 0
        
def is_valid(line):
    count = 0
    for l in line:
        if l == "<":
            count += 1
        elif l == ">":
            count += -1
        if count < 0:
            return False
    return True

def part2(lines):
    return 0

assert run(True) == (2, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
