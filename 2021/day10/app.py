def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day10/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1, a2 = split_lines(lines)
    return (a1, a2)

def split_lines(lines):
    # invalid lines -> part1, incomplete lines -> part2
    new_lines = [remove_chunks(line) for line in lines]
    l1, l2 = [], []
    for line in new_lines:
        (l2, l1)[any(c in line for c in ")]}>")].append(line)
    a1 = part1(l1)
    a2 = part2(l2)
    return a1,a2

def part1(lines):
    cost_by_symbol = {")": 3, "]": 57, "}": 1197, ">": 25137}
    cost = 0
    for line in lines:
        closing_chars = [char for char in line if char in ")]}>"]
        cost += cost_by_symbol[closing_chars[0]]
    return cost

def remove_chunks(line):
    while any(chunk in line for chunk in ["()","[]","{}","<>"]): 
        for chunk in ["()","[]","{}","<>"]:
            line = line.replace(chunk, "")
    return line            

def part2(lines):
    score_by_symbol = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for line in lines:
        score = 0
        for c in line[::-1]:
            score = score * 5
            score += score_by_symbol[c]
        scores.append(score)
    return sorted(scores)[int(len(scores)/2)]

assert run(True) == (26397, 288957), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
